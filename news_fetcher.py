"""Fetches and processes news articles from various sources."""

import feedparser
import requests
from datetime import datetime, timedelta
from dateutil import parser as date_parser
import vertexai
from vertexai.generative_models import GenerativeModel
from langdetect import detect, LangDetectException
from bs4 import BeautifulSoup
import config


def clean_html(text):
    """Remove HTML tags from text."""
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text(separator=' ', strip=True)


def is_english(text):
    """Check if text is in English."""
    try:
        # Combine title and summary for better detection
        lang = detect(text)
        return lang == 'en'
    except LangDetectException:
        # If detection fails, assume English
        return True


def fetch_articles_from_rss(feed_url, days_lookback=7):
    """Fetch articles from an RSS feed."""
    articles = []
    cutoff_date = datetime.now() - timedelta(days=days_lookback)

    try:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            try:
                # Parse publication date
                pub_date = date_parser.parse(entry.get('published', entry.get('updated', '')))

                # Skip old articles
                if pub_date.replace(tzinfo=None) < cutoff_date:
                    continue

                # Clean HTML from summary
                raw_summary = entry.get('summary', entry.get('description', ''))
                clean_summary = clean_html(raw_summary)

                # Check if article is in English
                text_to_check = entry.get('title', '') + ' ' + clean_summary
                if not is_english(text_to_check):
                    continue

                article = {
                    'title': entry.get('title', 'No title'),
                    'link': entry.get('link', ''),
                    'summary': clean_summary,
                    'published': pub_date,
                    'source': feed.feed.get('title', feed_url)
                }
                articles.append(article)
            except Exception as e:
                # Skip articles with parsing errors
                continue

    except Exception as e:
        print(f"Error fetching feed {feed_url}: {e}")

    return articles


def fetch_all_articles():
    """Fetch articles from all configured news sources."""
    all_articles = []

    for source in config.NEWS_SOURCES:
        print(f"Fetching from {source['name']}...")
        articles = fetch_articles_from_rss(source['url'], config.DAYS_LOOKBACK)
        all_articles.extend(articles)
        print(f"  Found {len(articles)} recent articles")

    # Sort by publication date (newest first)
    all_articles.sort(key=lambda x: x['published'], reverse=True)

    # Limit to max articles
    return all_articles[:config.MAX_ARTICLES_TO_ANALYZE]


def rank_articles_with_gemini(articles):
    """Use Gemini to analyze and rank articles by relevance and quality."""
    # Initialize Vertex AI
    vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)

    model = GenerativeModel(config.GEMINI_MODEL)

    # Prepare articles summary for Gemini
    articles_text = ""
    for i, article in enumerate(articles, 1):
        articles_text += f"\n{i}. {article['title']}\n"
        articles_text += f"   Source: {article['source']}\n"
        articles_text += f"   Summary: {article['summary'][:200]}...\n"
        articles_text += f"   Link: {article['link']}\n"

    prompt = f"""You are analyzing news articles about AI, generative AI, data science, and agentic AI systems.

Here are {len(articles)} recent articles:
{articles_text}

Your task:
1. **STRICT FILTERING** - ONLY select articles that are:
   - Directly about AI, generative AI (GenAI), machine learning, data science, or agentic AI systems
   - From credible news sources and publications (not blog spam or promotional content)
   - Newsworthy with actual substance (not just tutorials or opinion pieces)

   **REJECT articles about:**
   - General technology not related to AI/ML/data science
   - Clickbait, promotional content, or product marketing
   - Basic tutorials or "how-to" guides
   - Opinion pieces without technical depth
   - Topics unrelated to AI/data science (blockchain, crypto, web dev, etc.)

2. **PRIORITY RANKING** - From the qualifying articles, prioritize:

   **HIGHEST PRIORITY**:
   - AI in retail, e-commerce, or supply chain
   - Google AI (Gemini, Vertex AI, Cloud AI platforms)
   - Claude, Anthropic, or other leading LLMs
   - Australian AI developments or companies
   - Agentic AI systems and frameworks

   **MEDIUM PRIORITY**:
   - Generative AI breakthroughs and new models
   - Enterprise AI applications and case studies
   - Practical AI/ML tools, frameworks, and techniques
   - Data science innovations and methodologies
   - AI research with practical implications

3. **Quality criteria**:
   - Credible, reputable source
   - Substantial technical or business content
   - Significant developments or practical applications
   - Likely to be widely discussed in AI/data science community

Return ONLY a comma-separated list of up to {config.TOP_ARTICLES_TO_SEND} article numbers (e.g., "3,7,12,15,22").
If fewer than {config.TOP_ARTICLES_TO_SEND} articles meet the strict criteria, return only those that qualify.
Do not include any explanation, just the numbers."""

    try:
        response = model.generate_content(prompt)

        # Parse Gemini's response
        response_text = response.text.strip()
        selected_indices = [int(x.strip()) - 1 for x in response_text.split(',')]

        # Return selected articles
        top_articles = [articles[i] for i in selected_indices if i < len(articles)]
        return top_articles

    except Exception as e:
        print(f"Error ranking articles with Gemini: {e}")
        # Fallback: return first N articles
        return articles[:config.TOP_ARTICLES_TO_SEND]


def get_top_articles():
    """Main function to fetch and rank articles."""
    print("Fetching articles...")
    articles = fetch_all_articles()

    if not articles:
        print("No articles found")
        return []

    print(f"\nAnalyzing {len(articles)} articles with Gemini...")
    top_articles = rank_articles_with_gemini(articles)

    print(f"\nSelected {len(top_articles)} top articles")
    return top_articles
