from Product.TrendManager.TrendingController import TrendingController
from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, TrendingScore
import threading
import time


class TrendingToDB(object):
    # Call the trending to db to start filling the trend table in the database. This will be ran in the background
    # as long as the application is running

    def __init__(self):
        # creates the thread that will make the method run parallel. Sets daemon to true so that it will allow
        # the app to be terminated and will terminate with it
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        # This is the actual method that will run forever until the application is shut down, it is done in the
        # following steps
        # 1. Query movies from database
        # 2. Get new score for that movie
        # 3. If current trend score is different from the newly fetched score - Update score in database,
        # else go to step 1
        # 4. Go to step 1
        trend_controller = TrendingController()
        while True:

            res_movie = session.query(Movie).all()

            for movie in res_movie:

                res_score = session.query(TrendingScore).filter_by(movie_id=movie.id).first()

                # try first with set totscore and then comment it away and try with fetching totscore
                # new_tot_score = 100
                new_tot_score = trend_controller.get_trending_content(movie.title)  # gets new score
                print("THis is movie id:")
                print(movie.id)

                if res_score:
                    if new_tot_score != res_score.total_score:
                        print("NOT THE SAME SCORES - UPDATE")
                        res_score.total_score = new_tot_score
                    else:
                        print("SAME SCORES - DO NOTHING")
                else:
                    print("No such id in TrendingScore table")
                    movie = TrendingScore(movie_id=movie.id, total_score=new_tot_score, youtube_score=0,
                                          twitter_score=0)
                    session.add(movie)

            session.commit()

# To test the code above see the code below. It will start the trendingtodb, and will then wait for 10 seconds
# before first checkpoint and then wait another 10 before terminating. During this you can see that is db is
# filled and then the method is terminated when the application is finished.
trendingExample = TrendingToDB()
time.sleep(10)
print("Checkpoint")
time.sleep(10)
print("App is shutting down..")

# This solution was only to show that it is the trendingcontroller that is the limiting part
"""

            for movie in resMovie:
                in_db = False
                # try first with set totscore and then comment it away and try with fetching totscore
                # newTotScore = 100
                newTotScore = trend_controller.get_trending_content(movie.title) #gets new score
                print("THis is movie id:")
                print(movie.id)

                # Loop over each scoredMovie in resScore and see if movie is in it. if it is break check if it is a
                # new total score
                # or not and break the loop.
                for scoredMovie in resScore:
                    if scoredMovie.movie_id == movie.id:
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
"""
