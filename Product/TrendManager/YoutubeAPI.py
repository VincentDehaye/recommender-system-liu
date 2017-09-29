from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from dateutil import parser
from datetime import datetime, time, timedelta

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

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="snippet",
        maxResults=options.max_results
    ).execute()


    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    # Add if statement with current date, show only last weeks uploads?


    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            dateString = search_result["snippet"]["publishedAt"]
            datetime_object = datetime.datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S.%f")
            condi = datetime.now()- timedelta(days=30)
            print(datetime_object)
            if search_result["snippet"]["publishedAt"]:
                    videos.append("%s (%s)" % (search_result["snippet"]["title"],
                        search_result["snippet"]["publishedAt"]))

                    print("Videos:\n", "\n".join(videos), "\n")






if __name__== "__main__":
    argparser.add_argument("--q", help="Search term", default="IT movie")
    argparser.add_argument("--max-results", help="Max results", default=10)
    args = argparser.parse_args()

    try:
        youtube_search(args)
    except HttpError as e:
        print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))