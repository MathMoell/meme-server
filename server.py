from flask import Flask, render_template
import os
from datetime import datetime, timedelta
import pytz

app = Flask(__name__, static_folder="memes")

MEME_FOLDER = "memes"

@app.route("/")
def home():
    memes = [f for f in os.listdir(MEME_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not memes:
        return "Mingeid meme faile ei leitud kaustas memes!"

    est = pytz.timezone("Europe/Tallinn")
    now = datetime.now(est)

    meme_index = (now - datetime(now.year, now.month, now.day, tzinfo=est)).days % len(memes)
    meme_file = memes[meme_index]

    next_day = datetime(now.year, now.month, now.day, tzinfo=est) + timedelta(days=1)

    return render_template(
        "index.html", 
        meme_file=meme_file, 
        meme_number=meme_index + 1,
        total_memes=len(memes),
        next_day_iso=next_day.isoformat()  # ISO string JavaScripti jaoks
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
