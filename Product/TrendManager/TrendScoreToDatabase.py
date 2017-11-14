"""
Gets movie from database and stores a trending score
"""

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
    Last update: 13/11/2017
    Purpose: This class handles collecting all the trending scores so that they can
    be stored in the database.
    The class is using threads and will be abel to run in the background continuously
    """
    def __init__(self, background=False, continuous=False, daily=False):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: Instantiates the class, and based on the params an be run in different ways.
        :param background: True - makes the process run on a thread in the background.
        False - The process will not run on a thread.
        :param daily: True - Will make the process run once every day.
        False - Will only run the process once.
        """
        self.continous = continuous
        self.stop = False
        self.daily = daily
        self.insert_trend = InsertTrending()
        self.retrieve_trend = RetrieveTrending()
        self.alter_trend = UpdateTrending()
        self.retrieve_movie = RetrieveMovie()

        if daily & continuous:
            # if set to daily, it creates a scheduler and sets the interval to 1 day
            self.scheduled = BackgroundScheduler()
            self.scheduled.add_job(self.run, 'interval', days=1)
            self.scheduled.start()
        else:
            # creates the thread that will make the method run parallel.
            # Sets daemon to true so that it will allow
            # the app to be terminated and will terminate with it.
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = background
            thread.start()

    def run(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: The method where which will fetch all the scores by the
        TrendingController which communicatewith the Youtube and Twitter API.
        """

        # Fllowing steps are done:
        # 1. Query movies from database
        # 2. Get new score for that movie
        # 3. If current trend score is different from the newly
        # fetched score - Update score in database, else go to step 1
        # 4. Go to step 1
        trend_controller = TrendingController()

        while True:
            if self.stop:
                break
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

            if not self.continous:
                break

        # Used to stop the thread if background is false or for any other
        # reason it needs to be stopped.
    def terminate(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: Terminates the process
        """
        self.stop = True
        if self.daily:
            self.scheduled.shutdown()
