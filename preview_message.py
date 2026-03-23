#!/usr/bin/env python3
"""Preview what the Google Chat message will look like."""

from news_fetcher import get_top_articles
from google_chat import format_message
import json


def main():
    """Preview the Google Chat message."""
    print("=" * 60)
    print("Fetching articles for preview...")
    print("=" * 60)

    try:
        # Fetch and rank articles
        top_articles = get_top_articles()

        if not top_articles:
            print("\nNo articles found.")
            return

        # Format the message
        message = format_message(top_articles)

        # Display the formatted message
        print("\n" + "=" * 60)
        print("GOOGLE CHAT MESSAGE PREVIEW")
        print("=" * 60)
        print("\nThis is the JSON payload that will be sent:")
        print(json.dumps(message, indent=2))

        print("\n" + "=" * 60)
        print("VISUAL REPRESENTATION")
        print("=" * 60)

        if 'cards' in message:
            card = message['cards'][0]
            header = card['header']

            print(f"\n📰 {header['title']}")
            print(f"   {header['subtitle']}")
            print("\n" + "-" * 60)

            for i, section in enumerate(card['sections'], 1):
                widgets = section['widgets']

                # Extract title, source, description from widgets
                title_widget = widgets[0]['textParagraph']['text']
                source_widget = widgets[1]['textParagraph']['text']
                desc_widget = widgets[2]['textParagraph']['text']

                print(f"\n{title_widget}")
                print(f"{source_widget}")
                print(f"\n{desc_widget}")
                print(f"\n[READ ARTICLE] button")

                if i < len(card['sections']):
                    print("-" * 60)

        print("\n" + "=" * 60)

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
