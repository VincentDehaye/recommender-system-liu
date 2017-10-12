from Product.TrendManager.TrendingController import TrendingController
from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, MovieInGenre, Genre, TrendingScore

# 1. Query movies from database
# 2. Get new score for that movie
# 3. If current trend score is different from the newly fetched score - Update score in database, else go to step 1
# 4. Goto step 1


trendController = TrendingController()
scoredMovie = trendController.get_trending_content("pirates")

new = TrendingScore(movie_id=scoredMovie.id, total_score=scoredMovie.score, youtube_score=, twitter_score=)

session.add()
