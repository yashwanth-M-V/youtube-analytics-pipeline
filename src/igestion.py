import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def extract_video_id(url: str):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    return query.get("v", [""])[0]

def fetch_comments(video_id: str, max_comments: int = 100):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=min(100, max_comments - len(comments)),
            pageToken=next_page_token,
            textFormat="plainText",
        )
        response = request.execute()

        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "author": snippet.get("authorDisplayName"),
                "text": snippet.get("textDisplay"),
                "like_count": snippet.get("likeCount", 0),
                "published_at": snippet.get("publishedAt")
            })

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    df = pd.DataFrame(comments)

    if not df.empty:
        df["published_at"] = pd.to_datetime(df["published_at"])

    return df
