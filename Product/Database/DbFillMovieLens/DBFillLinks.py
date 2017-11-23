"""
Class to fill the database with links to imdb and tmdb IDs
"""
import csv
import os
from Product.Database.DBConn import MovieLinks, create_session


class FillLinks:
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 12-10-2017
    Last update: 9-11-2017
    Purpose: Fill the database with links to imdb and tmdb IDs
    """

    def __init__(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 12-10-2017
        Last update: 9-11-2017
        Purpose: Initiate the class and call the fill method
        """
        self.session = create_session()
        self.fill()

    def fill(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 12-10-2017
        Last update: 9-11-2017
        Purpose: Read the links.csv file and load it into the database.
        """
        # Columns in the are link csv files: movie_id, IMDB_id, TMDB_id
        print("Starting to fill links for the Big data set..")

        path = 'DbFillMovieLens/links.csv'
        abspath = os.path.abspath(path)

        # If run in gitlab runner change to correct path
        try:
            file = open(abspath, 'rt', encoding="utf-8")
            file.close()
        except FileNotFoundError:
            path = 'Product/Database/DbFillMovieLens/smallRatings.csv'
            abspath = os.path.abspath(path)

        with open(abspath, 'rt') as file:
            reader = csv.reader(file)
            # Iterates through each row in the file
            for row in reader:
                # Iterates through each column
                for counter, column in enumerate(row):
                    if counter == 0:
                        new_movie_id = column
                    if counter == 1:
                        new_imdb_id = column
                    if counter == 2:
                        new_tmdb_id = column
                        new_linking = MovieLinks(movie_id=new_movie_id, imdb_id=new_imdb_id,
                                                 tmdb_id=new_tmdb_id)
                        self.session.add(new_linking)

        # Commit the added ratings
        self.session.commit()
        print("DONE - Links added")

        # Close the csv file
        file.close()
