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

    def getTrending(self, numOfTitles=None):
        session = self.createSession()

        if numOfTitles is None:
            return session.query(TrendingScore).all()

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

    def addTrendScore(self, movie_id, total_score, youtube_score, twitter_score):
        session = self.createSession()
        movie = TrendingScore(movie_id=movie_id, total_score=total_score, youtube_score=youtube_score,
                                          twitter_score=twitter_score)
        session.add(movie)
        session.commit()


d = DatabaseManager()
print(d.getTrending(4))