#!/usr/bin/env python3
"""Main script for the GenAI News Bot."""

from news_fetcher import get_top_articles
from google_chat import send_to_google_chat


def main():
    """Run the news bot."""
    print("=" * 60)
    print("GenAI News Bot - Starting Weekly Update")
    print("=" * 60)

    try:
        # Fetch and rank articles
        top_articles = get_top_articles()

        if not top_articles:
            print("\nNo articles to send.")
            return

        # Send to Google Chat
        print("\nSending to Google Chat...")
        success = send_to_google_chat(top_articles)

        if success:
            print("\n" + "=" * 60)
            print("Weekly update completed successfully!")
            print("=" * 60)
        else:
            print("\nFailed to send update.")
            exit(1)

    except Exception as e:
        print(f"\nError running bot: {e}")
        exit(1)


if __name__ == "__main__":
    main()
