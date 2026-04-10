"""Configuration for the GenAI News Bot."""

import os

# Google Cloud / Vertex AI Configuration
PROJECT_ID = os.getenv('PROJECT_ID', 'gcp-wow-wiq-success-ai-dev')
GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT', 'gcp-wow-wiq-success-ai-dev')
LOCATION = os.getenv('LOCATION', 'global')
GOOGLE_CLOUD_LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION', 'global')

# Google Chat Webhook
GOOGLE_CHAT_WEBHOOK = os.getenv('GOOGLE_CHAT_WEBHOOK')

# News Sources - Active Medium Publications + Professional AI News
NEWS_SOURCES = [
    # Medium Publications (User's Digest - Active only)
    {
        'name': 'Data Science Collective',
        'url': 'https://medium.com/feed/data-science-collective',
        'type': 'rss'
    },

    # Professional AI News & Product Releases
    {
        'name': 'OpenAI Blog',
        'url': 'https://openai.com/blog/rss.xml',
        'type': 'rss'
    },
    {
        'name': 'Google Gemini Blog',
        'url': 'https://blog.google/products/gemini/rss/',
        'type': 'rss'
    },
    {
        'name': 'Anthropic News',
        'url': 'https://www.anthropic.com/news/rss.xml',
        'type': 'rss'
    },
    {
        'name': 'DeepMind Blog',
        'url': 'https://deepmind.google/blog/rss.xml',
        'type': 'rss'
    },
]

# Bot Settings
MAX_ARTICLES_TO_ANALYZE = 50  # Total articles to fetch from all sources
TOP_ARTICLES_TO_SEND = 10     # Number of best articles to include in the message
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
