from Product.TrendManager.TrendingController import TrendingController
from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, MovieInGenre, Genre, TrendingScore

# 1. Query movies from database
# 2. Get new score for that movie
# 3. If current trend score is different from the newly fetched score - Update score in database, else go to step 1
# 4. Goto step 1

trendController = TrendingController()

resMovie = session.query(Movie).all()
resScore = session.query(TrendingScore.movie_id).all()
print("This is resscore:")
for score in resScore:
    print(score.movie_id)

for movie in resMovie:

    newTotScore = trendController.get_trending_content(movie.title) #gets new score

    if movie.id in resScore:
        print(resScore.total_score)
        if newTotScore != resScore.total_score:
            print("NOT THE SAME SCORES - UPDATE")
            resScore.total_score = newTotScore
        else:
            print("SAME SCORES - DO NOTHING")
    else:
        print("No such id in TrendingScore table")
        movie = TrendingScore(movie_id=movie.id, total_score=newTotScore, youtube_score=0, twitter_score=0)
        session.add(movie)

session.commit()



