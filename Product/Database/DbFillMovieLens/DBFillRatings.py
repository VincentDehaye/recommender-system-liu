import csv
import os.path
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Rating

'''
Author: John Andree Lidquist, Marten Bolin
Date: 12/10/2017
Last update: 9/11/2017
Purpose: Read the ratings.csv/smallRatings.csv file and loads it into the database.
Columns in the are rating csv files are: userId, movieId, rating, timestamp
'''


class FillRatings:
    def __init__(self, small_data_set):
        self.session = create_session()
        self.fill(small_data_set)

    def fill(self, small_data_set):
        if small_data_set:
            path = 'DbFillMovieLens/smallRatings.csv'
            abspath = os.path.abspath(path)
            # If run in gitlab runner change to correct path
            try:
                f = open(abspath, 'rt', encoding="utf-8")
                f.close()
            except FileNotFoundError:
                path = 'Product/Database/DbFillMovieLens/smallRatings.csv'
                abspath = os.path.abspath(path)
            print("Starting to fill ratings from small data set..")

        else:
            path = 'DbFillMovieLens/ratings.csv'
            abspath = os.path.abspath(path)
            # If run in gitlab runner change to correct path
            try:
                f = open(abspath, 'rt', encoding="utf-8")
                f.close()
            except FileNotFoundError:
                path = 'Product/Database/DbFillMovieLens/smallRatings.csv'
                abspath = os.path.abspath(path)
            print("Starting to fill ratings from BIG data set..")

        with open(abspath, 'rt') as f:
            reader = csv.reader(f)

            # Iterates through each row in the file
            for row in reader:

                # Iterates through each column
                for counter, column in enumerate(row):

                    if counter == 0:
                        user_id = column

                    if counter == 1:
                        movie_id = column

                    if counter == 2:
                        rating = column
                        new_rating = Rating(movie_id=movie_id, user_id=user_id, rating=rating)
                        self.session.add(new_rating)
                        # There is also a timestamp in the dataset which is not used

        # Commit the added ratings
        self.session.commit()
        print("DONE - Ratings added")

        # Close the csv file
        f.close()
