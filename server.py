from flask import Flask, render_template
import os
from datetime import datetime, timedelta
import pytz

app = Flask(__name__, static_folder="memes")

MEME_FOLDER = "memes"

@app.route("/")
def home():
    memes = [f for f in os.listdir(MEME_FOLDER)
             if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]

    if not memes:
        return "Mingeid memesid ei leitud!"

    est = pytz.timezone("Europe/Tallinn")
    now = datetime.now(est)

    # Tänase päeva indeks
    start_of_year = datetime(now.year, 1, 1, tzinfo=est)
    days_passed = (now - start_of_year).days

    meme_index = days_passed % len(memes)
    meme_file = memes[meme_index]

    # Järgmine vahetus = järgmine kesköö Eesti aja järgi
    next_day = datetime(now.year, now.month, now.day, tzinfo=est) + timedelta(days=1)

    return render_template(
        "index.html",
        meme_file=meme_file,
        meme_number=meme_index + 1,
        total_memes=len(memes),
        next_day_iso=next_day.isoformat()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
