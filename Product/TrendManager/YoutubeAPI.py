"""
Search module for the YouTube API
"""
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
    """
    Performs a YouTube search and creates a list of results
    :param options:
    :return:
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    #  query term.

    def get_youtube_data(keyword):
        search_response = youtube.search().list(
            q=keyword,
            part="snippet",
            type=options.type,
            videoCategoryId=options.video_category_id,
            maxResults=options.max_results,
            publishedAfter=get_date()
        ).execute()
        return search_response

    def get_youtube_count(keyword):
        search_response = youtube.videos().list(
            part="statistics, snippet",
            id=get_video_id(keyword)
        ).execute()
        for search_result in search_response.get("items", []):
            search_result["statistics"]["viewCount"]
        return search_response

    def get_video_id(keyword):
        id = ""
        idList = ""
        for search_result in get_youtube_data(keyword).get("items", []):
            id = search_result["id"]["videoId"]
            idList = id + ", " + idList
            print(idList)
        return idList



def get_date(days):
    """
    Getting the date for the inputted number of days ago
    :param days: number of days ago
    :return:
    """
    date = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    date_with_timezone = date.replace(tzinfo=pytz.UTC)
    return date_with_timezone.isoformat()


def get_arguments(category_id, max_results):
    """
    Gets arguments (currently hard coded)
    :param category_id:
    :param max_results:
    :return:
    """
    argparser.add_argument("--q", help="Search term", default="frozen")
    argparser.add_argument("--type", help="Type", default="video")
    argparser.add_argument("--video-category-id",
                           help="Video Category Id", default=category_id)
    argparser.add_argument("--max-results", help="Max results", default=max_results)
    argparser.add_argument("--publishedAfter",
                           help="Date condition", default="")
    return argparser.parse_args()


def main():
    """
    Main method.
    :return:
    """
    arguments = get_arguments(30, 10)

    try:
        youtube_search(arguments)
    except HttpError as error:
        print("An HTTP error %d occurred:\n%s" % (error.resp.status, error.content))


if __name__ == "__main__":
    main()
