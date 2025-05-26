import requests
import os

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if not webhook_url:
    print("DISCORD_WEBHOOK_URL environment variable not set.")
    exit(1)

data = {
    "content": "[Railway Test] Discord webhook test from Railway"
}

response = requests.post(webhook_url, json=data)
if response.status_code == 204:
    print("Discord webhook test sent successfully!")
else:
    print(f"Failed to send Discord webhook test. Status code: {response.status_code}")
