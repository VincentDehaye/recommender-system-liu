from Product.TrendManager.TrendingController import TrendingController
from Product.Database.DatabaseManager import Insert, Retrieve, Alter
from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, TrendingScore
from apscheduler.schedulers.background import BackgroundScheduler
import threading


class TrendingToDB(object):
    # Call the trending to db to start filling the trend table in the database. This will be ran in the background
    # as long as the application is running

    def __init__(self, background=True, continuous=True, daily=False):
        # Background=True means that the application will be ran in daemon mode and other things can be ran
        # simultaneously.
        # continous=True means that the application will not be shut down after the first iteration
        # daily=True means that it will be ran every 24h only works if cont is also True
        self.continous = continuous
        self.stop = False
        self.daily = daily
        self.insert = Insert()
        self.retrieve = Retrieve()
        self.alter = Alter()

        if daily & continuous:
            # if set to daily, it creates a scheduler and sets the interval to 1 day
            self.scheduled = BackgroundScheduler()
            self.scheduled.add_job(self.run, 'interval', days=1)
            self.scheduled.start()
        else:
            # creates the thread that will make the method run parallel. Sets daemon to true so that it will allow
            # the app to be terminated and will terminate with it
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = background
            thread.start()

    def run(self):
        # This is the actual method that will run until the application is shut down, it is done in the
        # following steps
        # 1. Query movies from database
        # 2. Get new score for that movie
        # 3. If current trend score is different from the newly fetched score - Update score in database,
        # else go to step 1
        # 4. Go to step 1
        trend_controller = TrendingController()

        result = session.query(TrendingScore).all()

        while True:
            if self.stop:
                break
            res_movie = session.query(Movie).all()

            for movie in res_movie:
                if self.stop:
                    break
                res_score = session.query(TrendingScore).filter_by(movie_id=movie.id).first()

                new_tot_score = trend_controller.get_trending_content(movie.title)  # gets new score

                print("Movie ID:", movie.id)

                if res_score:

                    if new_tot_score != res_score.total_score:
                        # If score is new
                        res_score.total_score = new_tot_score
                        Alter.update_trend_score()
                else:
                    # If movie is not in TrendingScore table
                    self.insert.add_trend_score(movie_id=movie.id, total_score=new_tot_score, youtube_score=0, twitter_score=0)

                # The commit is in the loop for now due to high waiting time but could be moved outside to lower
                # total run time

            if not self.continous:
                break;

        # Used to stop the thread if background is false or for any other reason it needs to be stopped.
    def terminate(self):
        # Stops the scheduler
        self.stop = True
        if self.daily:
            self.scheduled.shutdown()

