from Product.TrendManager.TrendingController import TrendingController
from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, TrendingScore
import threading



class TrendingToDB(object):
    # Call the trending to db to start filling the trend table in the database. This will be ran in the background
    # as long as the application is running

    def __init__(self, background = True, continuous = True):
        self.continous = continuous
        # creates the thread that will make the method run parallel. Sets daemon to true so that it will allow
        # the app to be terminated and will terminate with it
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = background
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

        res_movie = session.query(Movie).all()

        for movie in res_movie:

            res_score = session.query(TrendingScore).filter_by(movie_id=movie.id).first()

            new_tot_score = trend_controller.get_trending_content(movie.title)  # gets new score

            if res_score:
                # if not the same
                if new_tot_score != res_score.total_score:
                    res_score.total_score = new_tot_score
            else:
                # if movie is not in trendingscore
                movie = TrendingScore(movie_id=movie.id, total_score=new_tot_score, youtube_score=0,
                                      twitter_score=0)
                session.add(movie)
            # The commit is in the loop for now due to high waiting time but could be moved outside to lower
            # total run time
            session.commit()

        while self.continous:

            res_movie = session.query(Movie).all()

            for movie in res_movie:

                res_score = session.query(TrendingScore).filter_by(movie_id=movie.id).first()

                new_tot_score = trend_controller.get_trending_content(movie.title)  # gets new score
                print(movie.id)

                if res_score:
                    if new_tot_score != res_score.total_score:
                        # If score is new
                        res_score.total_score = new_tot_score
                else:
                    # If movie is not in TrendingScore table
                    movie = TrendingScore(movie_id=movie.id, total_score=new_tot_score, youtube_score=0,
                                          twitter_score=0)
                    session.add(movie)
                # The commit is in the loop for now due to high waiting time but could be moved outside to lower
                # total run time
                session.commit()