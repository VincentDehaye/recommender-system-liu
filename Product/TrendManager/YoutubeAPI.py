"""
Search module for the YouTube API
"""
import datetime

import pytz as pytz
from googleapiclient.discovery import build

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyAncPk0ysVz0IO4S0fQLaG-0_NP42mgucU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class YoutubeAPI:

    def __init__(self):
        # self.options = self.get_arguments(30,10)
        self.maxresults = 10
        self.categoryid = 30
        self.type = "video"
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                             developerKey=DEVELOPER_KEY)

    def get_youtube_data(self, keyword):
        """
        Getting the the result from the search with keyword
        :param keyword: keyword, e.g. movie-title
        :return:
        """
        search_response = self.youtube.search().list(
            q=keyword,
            part="snippet",
            type=self.type,
            videoCategoryId=self.categoryid,
            maxResults=self.maxresults,
            publishedAfter=self.get_date(30)
        ).execute()
        return search_response

    def get_youtube_count(self, keyword):
        """
        Getting the viewCount for the selected videoId´s
        :param keyword: keyword, e.g. movie-title
        :return:
        """
        search_response = self.youtube.videos().list(
            part="statistics, snippet",
            id=self.get_video_id(keyword)
        ).execute()
        totalviews = 0
        for video in search_response.get("items", []):
            totalviews += int(video["statistics"]["viewCount"])
        return totalviews

    def get_video_id(self, keyword):
        """
        Getting the videoId´s from the query
        :param keyword: keyword, e.g. movie-title
        :return:
        """
        id = ""
        idList = ""
        for search_result in self.get_youtube_data(keyword).get("items", []):
            id = search_result["id"]["videoId"]
            idList = id + ", " + idList
        return idList

    def get_date(self, days):
        """
        Getting the date for the inputted number of days ago
        :param days: number of days ago
        :return:
        """
        date = datetime.datetime.utcnow() - datetime.timedelta(days=days)
        date_with_timezone = date.replace(tzinfo=pytz.UTC)
        return date_with_timezone.isoformat()


def main():
    """
    Main method.
    :return:
    """
    #arguments = get_arguments(30, 10)

    #try:
    #    youtube_search(arguments)
    #except HttpError as error:
    #    print("An HTTP error %d occurred:\n%s" % (error.resp.status, error.content))


if __name__ == "__main__":
    main()
