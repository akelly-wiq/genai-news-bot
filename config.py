"""Configuration for the GenAI News Bot."""

import os

# Google Cloud / Vertex AI Configuration
PROJECT_ID = os.getenv('PROJECT_ID', 'gcp-wow-wiq-success-ai-dev')
GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT', 'gcp-wow-wiq-success-ai-dev')
LOCATION = os.getenv('LOCATION', 'global')
GOOGLE_CLOUD_LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION', 'global')

# Google Chat Webhook
GOOGLE_CHAT_WEBHOOK = os.getenv('GOOGLE_CHAT_WEBHOOK')

# News Sources - RSS Feeds
NEWS_SOURCES = [
    # Medium AI/ML tags
    {
        'name': 'Medium - Artificial Intelligence',
        'url': 'https://medium.com/feed/tag/artificial-intelligence',
        'type': 'rss'
    },
    {
        'name': 'Medium - Machine Learning',
        'url': 'https://medium.com/feed/tag/machine-learning',
        'type': 'rss'
    },
    {
        'name': 'Medium - Data Science',
        'url': 'https://medium.com/feed/tag/data-science',
        'type': 'rss'
    },
    # Australian tech news
    {
        'name': 'InnovationAus - AI',
        'url': 'https://www.innovationaus.com/feed/',
        'type': 'rss'
    },
    {
        'name': 'Australian Financial Review - Technology',
        'url': 'https://www.afr.com/rss/technology',
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

# Keywords to prioritize
PRIORITY_KEYWORDS = [
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
