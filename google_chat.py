"""Send messages to Google Chat via webhook."""

import requests
import json
from datetime import datetime
import config


def format_message(articles):
    """Format articles into a Google Chat message."""
    if not articles:
        return {
            "text": "Hi team! 👋\n\nNo new articles found this week, but stay tuned for next Friday's update!"
        }

    # Create card message with greeting
    header = {
        "title": f"Weekly GenAI & Data Science News - {datetime.now().strftime('%B %d, %Y')}",
        "subtitle": f"Happy Friday! Here's the latest AI news 🚀"
    }

    sections = []

    for i, article in enumerate(articles, 1):
        # Format date
        pub_date = article['published'].strftime('%b %d, %Y')

        # Create article section
        section = {
            "widgets": [
                {
                    "textParagraph": {
                        "text": f"<b>{i}. {article['title']}</b>"
                    }
                },
                {
                    "textParagraph": {
                        "text": f"<i>{article['source']} - {pub_date}</i>"
                    }
                },
                {
                    "textParagraph": {
                        "text": article['summary'][:300] + "..." if len(article['summary']) > 300 else article['summary']
                    }
                },
                {
                    "buttons": [
                        {
                            "textButton": {
                                "text": "READ ARTICLE",
                                "onClick": {
                                    "openLink": {
                                        "url": article['link']
                                    }
                                }
                            }
                        }
                    ]
                }
            ]
        }
        sections.append(section)

    # Build card
    message = {
        "cards": [
            {
                "header": header,
                "sections": sections
            }
        ]
    }

    return message


def send_to_google_chat(articles):
    """Send formatted articles to Google Chat."""
    if not config.GOOGLE_CHAT_WEBHOOK:
        raise ValueError("GOOGLE_CHAT_WEBHOOK not set")

    message = format_message(articles)

    try:
        response = requests.post(
            config.GOOGLE_CHAT_WEBHOOK,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=json.dumps(message)
        )

        if response.status_code == 200:
            print("Message sent successfully to Google Chat!")
            return True
        else:
            print(f"Failed to send message. Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"Error sending message to Google Chat: {e}")
        return False
