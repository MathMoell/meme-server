from flask import Flask, render_template
import os
from datetime import datetime
import pytz

app = Flask(__name__, static_folder="memes")

MEME_FOLDER = "memes"
ALLOWED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp")

@app.route("/")
def home():
    # Leia kõik pildid
    memes = [
        f for f in os.listdir(MEME_FOLDER)
        if f.lower().endswith(ALLOWED_EXTENSIONS)
    ]

    if not memes:
        return "Kaustas 'memes' pole ühtegi pilti!"

    # Võta pildi index 20-sekundilise tsükli järgi
    now = datetime.now(pytz.timezone("Europe/Tallinn"))
    seconds_today = now.hour * 3600 + now.minute * 60 + now.second
    meme_index = (seconds_today // 20) % len(memes)

    meme_file = f"{MEME_FOLDER}/{memes[meme_index]}"

    return render_template(
        "index.html",
        meme_file=meme_file,
        meme_number=meme_index + 1,
        total_memes=len(memes)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
