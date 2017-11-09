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


class Create_session:
    def __init__(self):
        session = Session()
        return session

class Retrieve:

    def __init__(self):
        print("created")

    def get_titles_and_scores(self, query, session):
        titles_and_scores = {}
        for entry in query:
            movieId = entry.movie_id
            movie = session.query(Movie).filter_by(id=movieId).first()
            title = movie.title
            score = entry.total_score
            titles_and_scores[title] = score

        result = dict(sorted(titles_and_scores.items(), key=operator.itemgetter(1)))
        return result

    def get_trending(self, numOfTitles=None):
        session = self.create_session()

        if numOfTitles is None:
            return session.query(TrendingScore).all()

        query = session.query(TrendingScore).order_by(desc(TrendingScore.total_score)).limit(numOfTitles)
        return self.get_titles_and_scores(query, session)

    def get_trending_twitter(self, numOfTitles):
        session = self.create_session()
        query = session.query(TrendingScore).order_by(desc(TrendingScore.twitter_score)).limit(numOfTitles)
        return self.get_titles_and_scores(query, session)

    def get_trending_youtube(self, numOfTitles):
        session = self.create_session()
        query = session.query(TrendingScore).order_by(desc(TrendingScore.youtube_score)).limit(numOfTitles)
        return self.get_titles_and_scores(query, session)


class Insert:

    def add_trend_score(self, movie_id, total_score, youtube_score, twitter_score):
        session = self.create_session()
        movie = TrendingScore(movie_id=movie_id, total_score=total_score, youtube_score=youtube_score,
                              twitter_score=twitter_score)
        session.add(movie)
        session.commit()


class Alter:

    def update_trend_score(self, movie_id, total_score=None, youtube_score=None, twitter_score=None):
        session = self.create_session()
d = Retrieve()
print(d.get_trending(4))
print(d.get_trending_twitter(3))
print(d.get_trending_youtube(2))