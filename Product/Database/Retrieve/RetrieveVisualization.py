import operator
from sqlalchemy import desc
from Product.Database.Retrieve import Retrieve
from Product.Database.DBConn import TrendingScore, Movie

class RetrieveVisualization(Retrieve):

    #Ska flyttas till DataManager
    def get_titles_and_scores(self, query):
        titles_and_scores = {}
        for entry in query:
            movieId = entry.movie_id
            movie = self.session.query(Movie).filter_by(id=movieId).first()
            title = movie.title
            score = entry.total_score
            titles_and_scores[title] = score

        result = dict(sorted(titles_and_scores.items(), key=operator.itemgetter(1)))
        return result

    def get_trending(self, numOfTitles=None):
        if numOfTitles is None:
            return self.session.query(TrendingScore).all()

        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.total_score)).limit(numOfTitles)
        return self.get_titles_and_scores(query)

    def get_trending_twitter(self, numOfTitles):
        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.twitter_score)).limit(numOfTitles)
        return self.get_titles_and_scores(query)

    def get_trending_youtube(self, numOfTitles):
        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.youtube_score)).limit(numOfTitles)
        return self.get_titles_and_scores(query)