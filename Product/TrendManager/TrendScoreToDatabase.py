"""
Author: John Andree Lidquist, Marten Bolin
Date:
Last update:
Purpose: Gets movie from database and stores a trending score
"""

from datetime import datetime
import threading

from apscheduler.schedulers.background import BackgroundScheduler
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Insert.InsertTrending import InsertTrending
from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending
from Product.Database.DatabaseManager.Update.UpdateTrending import UpdateTrending
from Product.TrendManager.TrendingController import TrendingController


class TrendingToDB(object):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date:
    Last update: 2017-11-13
    Purpose: This class handles collecting all the trending scores so that they can
    be stored in the database.
    The class is using threads and will be abel to run in the background continuously
    """
    def __init__(self, daemon=False, daily=False):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: Instantiates the class, and based on the params an be run in different ways.
        :param daemon: True - makes the process terminate when app is finished.
        False - The process will not terminate until finished or terminated.
        :param daily: True - Will make the process run once every day.
        False - Will only run the process once.
        """
        #self.daemon = daemon
        self.stop = False
        self.daily = daily
        self.insert_trend = InsertTrending()
        self.retrieve_trend = RetrieveTrending()
        self.alter_trend = UpdateTrending()
        self.retrieve_movie = RetrieveMovie()

        if daily:
            # if set to daily, it creates a scheduler and sets the interval to 1 day
            self.scheduled = BackgroundScheduler()
            if not daemon:
                self.scheduled.daemon = False
            self.scheduled.add_job(self.run, 'interval', seconds=50, id="1")
            self.scheduled.start()
            self.scheduled.modify_job(job_id="1", next_run_time=datetime.now())
        else:
            # creates the thread that will make the method run parallel.
            # Sets daemon to true so that it will allow
            # the app to be terminated and will terminate with it.
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = daemon
            thread.start()

    def run(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: The method where which will fetch all the scores by the
        TrendingController which communicate with the Youtube and Twitter API.
        """

        # Fllowing steps are done:
        # 1. Query movies from database
        # 2. Get new score for that movie
        # 3. If current trend score is different from the newly
        # fetched score - Update score in database, else go to step 1
        # 4. Go to step 1
        trend_controller = TrendingController()
        res_movie = self.retrieve_movie.retrieve_movie()

        for movie in res_movie:
            if self.stop:
                break

            res_score = self.retrieve_trend.retrieve_trend_score(movie.id)

            scores = trend_controller.get_trending_content(movie.title)
            new_tot_score = scores[0]  # Gets total score
            new_youtube_score = scores[1]  # Gets Youtube score
            new_twitter_score = scores[2]  # Gets Twittwer score

            print("Movie ID:", movie.id)

            if res_score:

                if new_tot_score != res_score.total_score:
                    # If score is new
                    res_score.total_score = new_tot_score
                    self.alter_trend.update_trend_score(movie_id=movie.id,
                                                        total_score=new_tot_score,
                                                        youtube_score=new_youtube_score,
                                                        twitter_score=new_twitter_score)
            else:
                # If movie is not in TrendingScore table
                self.insert_trend.add_trend_score(movie_id=movie.id,
                                                  total_score=new_tot_score,
                                                  youtube_score=new_youtube_score,
                                                  twitter_score=new_twitter_score)

                # The commit is in the loop for now due to high waiting time but
                # could be moved outside to lower total run time

        # Used to stop the thread if background is false
        # or for any other reason it needs to be stopped.
    def terminate(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: Terminates the process
        """
        print("Shutting down TrendScoreToDatabase..")
        self.stop = True
        if self.daily:
            self.scheduled.shutdown()
