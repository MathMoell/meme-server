import os
import requests

MEME_FOLDER = "../memes"
REDDIT_URL = "https://www.reddit.com/r/memes/top.json?limit=50&t=day"
HEADERS = {"User-Agent": "MemeBot/0.1"}

def fetch_daily_meme():
    res = requests.get(REDDIT_URL, headers=HEADERS)
    data = res.json()
    for post in data["data"]["children"]:
        url = post["data"]["url"]
        if url.endswith((".jpg", ".png", ".gif")):
            filename = os.path.join(MEME_FOLDER, os.path.basename(url))
            if not os.path.exists(filename):
                with open(filename, "wb") as f:
                    f.write(requests.get(url).content)
                print(f"Downloaded: {filename}")
                return filename
    print("No new meme found today.")

if __name__ == "__main__":
    fetch_daily_meme()
