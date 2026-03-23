#!/usr/bin/env python3
"""Test script to see what articles would be sent (without actually sending)."""

from news_fetcher import get_top_articles
from datetime import datetime


def main():
    """Test the news bot locally."""
    print("=" * 60)
    print("GenAI News Bot - Local Test")
    print("=" * 60)

    try:
        # Fetch and rank articles
        top_articles = get_top_articles()

        if not top_articles:
            print("\nNo articles found.")
            return

        # Display the articles that would be sent
        print(f"\n{'=' * 60}")
        print(f"TOP {len(top_articles)} ARTICLES - {datetime.now().strftime('%B %d, %Y')}")
        print(f"{'=' * 60}\n")

        for i, article in enumerate(top_articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']}")
            print(f"   Date: {article['published'].strftime('%b %d, %Y')}")
            print(f"   Link: {article['link']}")
            print(f"   Summary: {article['summary'][:200]}...")
            print()

        print("=" * 60)
        print("Test completed successfully!")
        print("These articles would be sent to Google Chat.")
        print("=" * 60)

    except Exception as e:
        print(f"\nError during test: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
