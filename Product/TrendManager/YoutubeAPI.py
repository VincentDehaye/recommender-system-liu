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
        self.max_results = 10
        self.category_id = 24
        self.type = "video"
        self.published = 30
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
            videoCategoryId=self.category_id,
            maxResults=self.max_results,
            publishedAfter=self.get_date(self.published)
        ).execute()
        return search_response

    def get_youtube_score(self, keyword):
        """
        Getting video statistics for the selected videoId´s
        and calculating total trending score
        :param keyword: keyword, e.g. movie-title
        :return: the total trending score for keyword
        """
        keyword = self.add_search_words(keyword)

        search_response = self.youtube.videos().list(
            part="statistics, snippet",
            id=self.get_video_id(keyword)
        ).execute()

        total_results = self.get_total_search_result(keyword)

        total_score = 0

        for video in search_response.get("items", []):
            view_count = self.get_view_count(video)
            like_ratio = self.get_like_count(video)
            publication_date = self.get_publication_date(video)

            score = 1

            if view_count != 0:
                score *= view_count
            if like_ratio != 0:
                score *= like_ratio
            if publication_date != 0:
                score *= publication_date

            total_score += score
        total_score *= total_results
        total_score = int(round(total_score))
        return total_score

    def add_search_words(self, keyword):
        """
        Takes the movie title and adds more words to the search of the API
        :param keyword: keyword e.g. movie-title
        :return: new search term
        """
        search_term = keyword + " movie trailer"
        return search_term

    def get_view_count(self, video):
        """
        Getting view count
        :param video: search result from API response
        :return: number of views
        """
        views = video.get("statistics").get("viewCount")
        if views is None:
            return 0
        return int(views)

    def get_like_count(self, video):
        """
        Getting like and dislike count and calculates the ratio
        :param video: search result from API response
        :return: ratio of dislikes/likes
        """
        likes = 0
        get_likes = video.get("statistics").get("likeCount")
        if not get_likes is None:
            likes = int(get_likes)

        dislikes = 0
        get_dislikes = video.get("statistics").get("dislikeCount")
        if not get_dislikes is None:
            dislikes = int(get_dislikes)

        if likes != 0 and dislikes != 0:
            ratio = 1 - (dislikes / likes)
        elif likes != 0:
            ratio = 1
        else:
            ratio = 0

        return ratio

    def get_total_search_result(self, keyword):
        """
        Getting the total number of results for a movie search and then
        dividing it by max result (1 000 000) to get a percentage to use in
        trending calculations
        :param keyword: kyeword, e.g. movie-title
        :return: totalResult ratio
        """
        total_result = self.get_youtube_data(keyword).get("pageInfo").get("totalResults")
        result_ratio = total_result / 1000000
        return result_ratio


    def get_publication_date(self, video):
        """
        Getting the date when a video was uploaded
        :param keyword: keyword, e.g. movie-title
        :return: int representing how many days ago a video was uploaded
        """
        curr_date = datetime.datetime.today()

        date = video.get("snippet").get("publishedAt")
        published_at = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

        days_ago_datetime = curr_date - published_at
        days_ago = int(days_ago_datetime.days)

        return 1 - (days_ago / self.published)


    def get_video_id(self, keyword):
        """
        Getting the videoId´s from the query
        :param keyword: keyword, e.g. movie-title
        :return:
        """
        id = ""
        idList = ""
        for search_result in self.get_youtube_data(keyword).get("items", []):
            id = search_result.get("id").get("videoId")
            if id:
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
