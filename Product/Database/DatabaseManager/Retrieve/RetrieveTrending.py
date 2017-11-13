"""
RetrieveTrending Class, is supposed to provide data from the Trending table in the database
"""
from sqlalchemy import desc
from Product.Database.DBConn import TrendingScore
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve


class RetrieveTrending(Retrieve):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 9/11/2017
    Last update: 10/11/2017
    Purpose: Supposed to Retrieve data from trending table in database
    """
    def retrieve_trend_score(self, movie_id=None, number_of_titles=None):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update:
        Purpose: Supposed to retrieve the Trending score from database
        :param movie_id : the id of the movie that should be retrieved (optional)
        :param number_of_titles : the number of titles with the highest total score to be returned
        :return TrendingScore : of type TrendingScore
        """
        if movie_id:
            trend = self.session.query(TrendingScore).filter_by(movie_id=movie_id).first()
        elif number_of_titles:
            trend = self.session.query(TrendingScore).order_by(desc(TrendingScore.total_score)).limit(number_of_titles)
        else:
            trend = self.session.query(TrendingScore).all()
        self.session.close()
        return trend

    def get_trending_twitter(self, numOfTitles):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update:
        Purpose: Supposed to retrieve the Trending score from database
        :param number_of_titles : the number of titles with the highest twitter score to be returned
        :return TrendingScore : of type TrendingScore
        """
        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.twitter_score)).limit(numOfTitles)
        return query

    def get_trending_youtube(self, numOfTitles):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update:
        Purpose: Supposed to retrieve the Trending score from database
        :param number_of_titles : the number of titles with the highest twitter score to be returned
        :return TrendingScore : of type TrendingScore
        """
        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.youtube_score)).limit(numOfTitles)
        return query
