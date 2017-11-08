from Product.Database.DBConn import Session, TrendingScore, Movie
from sqlalchemy import desc
import operator

'''
Top 10 most trending content (title + score)
Top 10 most trending on twitter (title + score)
Top 10 most trending on Youtube (title + score)
(OPTIONAL) Possibility to search for a specific movie
(OPTIONAL)Trending score over time
'''
class DatabaseManager():
    def __init__(self):
       print("created")

    def createSession(self):
        session = Session()
        return session

    def getTrending(self, numOfTitles):
        session = self.createSession()
        query = session.query(TrendingScore).order_by(desc(TrendingScore.total_score)).limit(numOfTitles)
        return self.getTitlesAndScores(numOfTitles, query, session)

    def getTrendingTwitter(self, numOfTitles):
        session = self.createSession()
        query = session.query(TrendingScore).order_by(desc(TrendingScore.twitter_score)).limit(numOfTitles)
        return self.getTitlesAndScores(numOfTitles, query, session)

    def getTrendingYoutube(self, numOfTitles):
        session = self.createSession()
        query = session.query(TrendingScore).order_by(desc(TrendingScore.youtube_score)).limit(numOfTitles)
        return self.getTitlesAndScores(numOfTitles, query, session)

    def getTitlesAndScores(self, numOfTitles, query, session):
        titlesAndScores = {}
        for entry in query:
            movieId = entry.movie_id
            movie = session.query(Movie).filter_by(id=movieId).first()
            title = movie.title
            score = entry.total_score
            titlesAndScores[title] = score

        result = dict(sorted(titlesAndScores.items(), key=operator.itemgetter(1)))
        return result

d = DatabaseManager()
print(d.getTrending(5))