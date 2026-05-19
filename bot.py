import os
import time
import feedparser
import requests

# tiktok to telegram bot
BOT_TOKEN = os.environ.get("270876265:AAHUL5nLj4WvNZyICdjDUQHaIcGVhZ0wl78")
CHANNEL_ID = os.environ.get("@TikTokJourneyByJplolo")
TIKTOK_RSS = os.environ.get("https://rss.app/feeds/KVLA6Z9XzoDz5Gu9.xml")

def get_latest_video():
    feed = feedparser.parse(TIKTOK_RSS)
    if feed.entries:
        return feed.entries[0].link
    return None

def send_to_telegram(video_url):
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": f"New video dropped: {video_url}"
    }
    requests.post(api_url, json=payload)

def main():
    last_url = None
    while True:
        current_url = get_latest_video()
        if current_url and current_url != last_url:
            if last_url is not None:
                send_to_telegram(current_url)
            last_url = current_url
        time.sleep(300)

if __name__ == "__main__":
    main()
