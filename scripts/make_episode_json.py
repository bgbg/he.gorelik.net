import feedparser
import json
import os


rss_url = "https://anchor.fm/s/432ffb50/podcast/rss"
feed = feedparser.parse(rss_url)
dir_this = os.path.dirname(os.path.abspath(__file__))
dir_data = os.path.abspath(os.path.join(dir_this, "../_data"))
os.makedirs(dir_data, exist_ok=True)

episodes = []
for entry in feed.entries:
    episode = {
        "title": entry.title,
        "audio_url": entry.enclosures[0].href if entry.enclosures else None,
        "published": entry.published,
        "duration": entry.get("itunes_duration", ""),
        "description": entry.description,
        "link": entry.link,
    }
    episodes.append(episode)

# Save to a Jekyll-friendly _data file
with open(os.path.join(dir_data, "episodes.json"), "w", encoding="utf-8") as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)

print("Saved episodes to _data/episodes.json")
