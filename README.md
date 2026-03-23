# GenAI News Bot

A weekly bot that curates the best data science and generative AI news articles and sends them to Google Chat.

## Features

- Fetches articles from Medium, Australian tech news, and other sources
- Uses Google Gemini AI (via Vertex AI) to analyze and rank articles by quality and relevance
- Sends weekly digest to Google Chat
- Runs automatically via GitHub Actions (free hosting)

## Setup

### 1. Get Required Credentials

**Google Cloud Service Account:**
1. Go to https://console.cloud.google.com/
2. Select project: `gcp-wow-wiq-success-ai-dev`
3. Go to IAM & Admin → Service Accounts
4. Create or use existing service account with Vertex AI permissions
5. Create a JSON key and download it

**Google Chat Webhook:**
1. Open your Google Chat space
2. Click the space name → Manage webhooks
3. Create a new webhook
4. Copy the webhook URL

### 2. Configure GitHub Secrets

1. Go to your GitHub repository → Settings → Secrets and variables → Actions
2. Add two secrets:
   - `GCP_SA_KEY`: Your Google Cloud service account JSON key (entire file contents)
   - `GOOGLE_CHAT_WEBHOOK`: Your Google Chat webhook URL

### 3. Enable GitHub Actions

1. Go to the Actions tab in your repository
2. Enable workflows if prompted

### 4. Test the Bot

**Manual Test (requires Google Cloud authentication):**
```bash
# Clone the repo
git clone <your-repo-url>
cd genai-news-bot

# Install dependencies
pip install -r requirements.txt

# Authenticate with Google Cloud
gcloud auth application-default login --project=gcp-wow-wiq-success-ai-dev

# Set environment variables
export PROJECT_ID="gcp-wow-wiq-success-ai-dev"
export GOOGLE_CLOUD_PROJECT="gcp-wow-wiq-success-ai-dev"
export LOCATION="global"
export GOOGLE_CHAT_WEBHOOK="your_webhook_url_here"

# Run the bot
python main.py
```

**Test via GitHub Actions:**
1. Go to Actions → Weekly GenAI News Bot
2. Click "Run workflow" → "Run workflow"

## Configuration

Edit `config.py` to customize:
- News sources (RSS feeds)
- Number of articles to send
- Keywords to prioritize
- How far back to look for articles

## Schedule

The bot runs every Monday at 9 AM UTC. To change the schedule, edit `.github/workflows/weekly-news.yml` and modify the cron expression:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Min Hour Day Month Weekday
```

Examples:
- Every Sunday at 8 AM: `0 8 * * 0`
- Every day at 6 PM: `0 18 * * *`
- First day of month: `0 9 1 * *`

## Cost

- **GitHub Actions:** Free for public repos (2000 minutes/month)
- **Vertex AI (Gemini):** Paid by Woolworths via project `gcp-wow-wiq-success-ai-dev`
- **Google Chat:** Free

**Estimated monthly cost:** $0 (company pays for Vertex AI)

## Troubleshooting

**Bot not sending messages:**
1. Check GitHub Actions logs for errors
2. Verify secrets are set correctly
3. Test manually with local environment

**No articles found:**
- Check RSS feeds are accessible
- Adjust `DAYS_LOOKBACK` in config.py

**Poor article selection:**
- Adjust `PRIORITY_KEYWORDS` in config.py
- Increase `MAX_ARTICLES_TO_ANALYZE`
