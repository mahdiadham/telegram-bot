import os

app_token = os.environ.get('BOT_TOKEN')

if not app_token:
    raise ValueError("❌ BOT_TOKEN environment variable is not set!")
