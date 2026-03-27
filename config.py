"""Configuration for the GenAI News Bot."""

import os

# Google Cloud / Vertex AI Configuration
PROJECT_ID = os.getenv('PROJECT_ID', 'gcp-wow-wiq-success-ai-dev')
GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT', 'gcp-wow-wiq-success-ai-dev')
LOCATION = os.getenv('LOCATION', 'global')
GOOGLE_CLOUD_LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION', 'global')

# Google Chat Webhook
GOOGLE_CHAT_WEBHOOK = os.getenv('GOOGLE_CHAT_WEBHOOK')

# News Sources - RSS Feeds (Credible publications only)
NEWS_SOURCES = [
    # Major AI News Outlets
    {
        'name': 'MIT Technology Review - AI',
        'url': 'https://www.technologyreview.com/topic/artificial-intelligence/feed',
        'type': 'rss'
    },
    {
        'name': 'VentureBeat AI',
        'url': 'https://venturebeat.com/category/ai/feed/',
        'type': 'rss'
    },
    {
        'name': 'TechCrunch AI',
        'url': 'https://techcrunch.com/category/artificial-intelligence/feed/',
        'type': 'rss'
    },
    {
        'name': 'The Verge AI',
        'url': 'https://www.theverge.com/ai-artificial-intelligence/rss/index.xml',
        'type': 'rss'
    },

    # Company AI Blogs
    {
        'name': 'Google AI Blog',
        'url': 'https://blog.google/technology/ai/rss/',
        'type': 'rss'
    },
    {
        'name': 'Google Cloud Blog',
        'url': 'https://cloudblog.withgoogle.com/rss/',
        'type': 'rss'
    },
    {
        'name': 'OpenAI Blog',
        'url': 'https://openai.com/blog/rss.xml',
        'type': 'rss'
    },
    {
        'name': 'Anthropic News',
        'url': 'https://www.anthropic.com/news/rss.xml',
        'type': 'rss'
    },

    # Data Science Publications (curated)
    {
        'name': 'Towards Data Science',
        'url': 'https://towardsdatascience.com/feed',
        'type': 'rss'
    },
    {
        'name': 'KDnuggets',
        'url': 'https://www.kdnuggets.com/feed',
        'type': 'rss'
    },

    # Australian Tech News
    {
        'name': 'InnovationAus',
        'url': 'https://www.innovationaus.com/feed/',
        'type': 'rss'
    },
    {
        'name': 'Australian Financial Review - Technology',
        'url': 'https://www.afr.com/rss/technology',
        'type': 'rss'
    },

    # Enterprise AI & Retail Tech
    {
        'name': 'AI Business',
        'url': 'https://aibusiness.com/rss.xml',
        'type': 'rss'
    },
]

# Bot Settings
MAX_ARTICLES_TO_ANALYZE = 50  # Total articles to fetch from all sources
TOP_ARTICLES_TO_SEND = 5      # Number of best articles to include in the message
DAYS_LOOKBACK = 7              # Only consider articles from the past N days

# Gemini API Settings
GEMINI_MODEL = os.getenv('SYNTHESIS_LLM_MODEL', 'gemini-2.5-flash')
MAX_TOKENS = 1024

# Keywords to prioritize (ordered by priority)
PRIORITY_KEYWORDS = [
    # High priority - specific to user interests
    'australia',
    'australian',
    'google',
    'gemini',
    'vertex ai',
    'claude',
    'anthropic',
    'retail',
    'e-commerce',
    'ecommerce',
    'supply chain',
    'customer experience',
    'woolworths',
    'supermarket',

    # Medium priority - general AI topics
    'generative ai',
    'genai',
    'gen ai',
    'large language model',
    'llm',
    'machine learning',
    'deep learning',
    'data science',
    'artificial intelligence',
    'neural network',
    'gpt',
    'transformer',
    'natural language processing',
    'nlp',
    'computer vision',
    'reinforcement learning',
]
