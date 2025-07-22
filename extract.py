import pandas as pd
from googleapiclient.discovery import build
from tqdm import tqdm
import time

# CONFIG
API_KEY = "API_KEY"   
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Search Terms
SEARCH_TERMS = [
    "sony music india", "old hindi songs", "sufi songs", "kishore kumar songs",
    "indipop songs 90s", "hindi music", "hindi bollywood songs", "punjabi songs",
    "artist:sajjad ali", "channel: nescafe basement", "playlist: coke studio pakistan",
    "album: coke studio", "ghazals", "artist:mustafa zahid", "emraan hashmi songs",
    "artist:atif aslam", "artist:rahat fateh ali khan", "T-Series", "sony music india",
    "tips official", "yrf", "zeemusiccompany", "malayalam songs", "bengali songs",
    "marathi songs", "gujarati songs", "haryanvi songs", "odia songs", "bhojpuri songs",
    "assamese songs", "rajasthani songs", "urdu songs", "english songs", "hindi songs",
    "tamil songs", "telugu songs", "kannada songs", "english songs", "artist: The Weeknd"
]

# Functions
def search_videos(query, max_results=20):
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=max_results,
        type="video"
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]
    return video_ids

def get_video_details(video_ids):
    video_response = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    ).execute()

    video_data = []
    for item in video_response['items']:
        snippet = item['snippet']
        stats = item.get('statistics', {})

        video_entry = {
            'Video ID': item['id'],
            'Video Title': snippet['title'],
            'Video Description': snippet.get('description', ''),
            'Channel Title': snippet['channelTitle'],
            'Channel ID': snippet['channelId'],
            'Published Date': snippet['publishedAt'],
            'View Count': stats.get('viewCount', 0),
            'Like Count': stats.get('likeCount', 0),
            'Comment Count': stats.get('commentCount', 0),
            'Comments': get_video_comments(item['id'])
        }
        video_data.append(video_entry)
    return video_data

def get_video_comments(video_id, max_comments=20):
    comments = []
    try:
        comment_response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText"
        ).execute()

        for item in comment_response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

    except Exception as e:
        # Comments may be disabled, skip
        pass

    return " || ".join(comments)  # Combine comments into 1 string for CSV

# Main Collection Loop
all_video_data = []

for term in tqdm(SEARCH_TERMS):
    print(f"Searching for: {term}")
    try:
        video_ids = search_videos(term, max_results=10)  # Tune this (10–50 per term)

        if video_ids:
            video_data = get_video_details(video_ids)
            all_video_data.extend(video_data)

        # Be nice to API limits
        time.sleep(2)

    except Exception as e:
        print(f"Error with term {term}: {e}")

# Save to CSV
df = pd.DataFrame(all_video_data)
df.to_csv("youtube_music_dataset.csv", index=False, encoding='utf-8-sig')

print("Done! Dataset saved as youtube_music_dataset.csv")
