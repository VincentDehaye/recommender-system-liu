from Product.Database.DBConn import session
from Product.Database.DBConn import Rating
import csv

# Read the movie_id.csv file to add data into database.
# Columns in the ratings.csv: userId, movieId, rating, timestamp
class FillRatings:
    def __init__(self, smallDataSet):
        self.Fill(smallDataSet)

    def Fill(self, smallDataSet):

        if smallDataSet:
            path = 'smallRatings.csv'
            print("Filling ratings from small dataset")
        else:
            path = 'ratings.csv'
            print("Filling ratings from BIG dataset")

        with open(path, 'rt') as f:
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
                        session.add(new_rating)
                        # There is also a timestamp in the dataset which is not used

        # Commit the added ratings
        session.commit()

        # Close the csv file
        f.close()