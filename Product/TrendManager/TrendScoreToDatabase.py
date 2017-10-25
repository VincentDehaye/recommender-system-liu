from Product.TrendManager.TrendingController import TrendingController
from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, TrendingScore

# 1. Query movies from database
# 2. Get new score for that movie
# 3. If current trend score is different from the newly fetched score - Update score in database, else go to step 1
# 4. Goto step 1

trendController = TrendingController()

resMovie = session.query(Movie).all()
resScore = session.query(TrendingScore).all()

# Below are two solutions to the same problem, in the first solution the full resScore table is fetched and then
# it is iterated over and compared. In the second solution there is a query for each trendingscore seperately for
# each movie. We believed querying it for each movie seperetaly had a great impact on the time it took to complete
# but it seems to be the the get trending score that takes time. Try commenting away that part and se it to static
# 100 and vice versa. The differense is due to get trending content maninly and not the query.I would suggest solution
# 2 since it scales better with large databases

# New solution

for movie in resMovie:
    in_db = False
    # try first with set totscore and then comment it away and try with fetching totscore
    newTotScore = 100
    #newTotScore = trendController.get_trending_content(movie.title) #gets new score
    print("THis is movie id:")
    print(movie.id)

    # Loop over each scoredMovie in resScore and see if movie is in it. if it is break check if it is a new totalscore
    # or not and break the loop.
    for scoredMovie in resScore:
        if scoredMovie.movie_id == movie.id:
            print(scoredMovie.total_score)
            if newTotScore != scoredMovie.total_score:
                print("NOT THE SAME SCORES - UPDATE")
                scoredMovie.total_score = newTotScore
            else:
                print("SAME SCORES - DO NOTHING")
            in_db = True
            break

    # If it goes through whole loop then we know it is a new movie and it can be put into the trending table
    if not in_db:
        print("No such id in TrendingScore table")
        movie = TrendingScore(movie_id=movie.id, total_score=newTotScore, youtube_score=0, twitter_score=0)
        session.add(movie)

session.commit()

# Old solution
"""
for movie in resMovie:


    resScore = session.query(TrendingScore).filter_by(movie_id=movie.id).first()

    # try first with set totscore and then comment it away and try with fetching totscore
    newTotScore = 100
    #newTotScore = trendController.get_trending_content(movie.title) #gets new score
    print("THis is movie id:")
    print(movie.id)

    if resScore:
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

"""

