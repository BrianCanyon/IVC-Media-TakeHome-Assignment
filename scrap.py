import requests
import os

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
def send_message_to_slack(channel, text):
    url = 'https://hooks.slack.com/services/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'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_TOKEN}'
    }
    data = {
        'channel': channel,
        'text': text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")

send_message_to_slack('social', 'bing bong')