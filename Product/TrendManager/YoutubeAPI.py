import datetime

import pytz as pytz
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyAncPk0ysVz0IO4S0fQLaG-0_NP42mgucU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Setting date for the last 30 days
    def get_date():
        d = datetime.datetime.utcnow() - datetime.timedelta(days=30)
        d_with_timezone = d.replace(tzinfo=pytz.UTC)
        return d_with_timezone.isoformat()

    # Call the search.list method to retrieve results matching the specified
    #  query term.
    search_response = youtube.search().list(
        q=options.q,
        part="snippet",
        type=options.type,
        videoCategoryId=options.video_category_id,
        maxResults=options.max_results,
        publishedAfter=get_date()
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s published: %s" %
                          (search_result["snippet"]["title"],
                           search_result["snippet"]["publishedAt"]))

    print("Videos:\n", "\n".join(videos), "\n")


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="frozen")
    argparser.add_argument("--type", help="Type", default="video")
    argparser.add_argument("--video-category-id",
                           help="Video Category Id", default=30)
    argparser.add_argument("--max-results", help="Max results", default=10)
    argparser.add_argument("--publishedAfter",
                           help="Date condition", default="")
    arguments = argparser.parse_args()

    try:
        youtube_search(arguments)
    except HttpError as error:
        print("An HTTP error %d occurred:\n%s" % (error.resp.status, error.content))
