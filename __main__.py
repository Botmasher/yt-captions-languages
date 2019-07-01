from yt_auth import youtube
import argparse

# Parse channel from cl args
print("Parsing args for channel id...")
argparser = argparse.ArgumentParser()
argparser.add_argument("--channel", help="YouTube channel id (not channel name)")
args = argparser.parse_args()

# Read data from YT API
def get_videos(youtube, channel_id, max_results=50):
    videos = youtube().search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        q="*",
        type="video"
    ).execute()

    titles = list(map(
        lambda v: (
            v['items']['id']['videoId'],
            v['items']['snippet']['title']
        ),
        videos
    ))
    return titles

print("Fetching channel data...")
data = get_videos(youtube, args.channel)
print(data)
