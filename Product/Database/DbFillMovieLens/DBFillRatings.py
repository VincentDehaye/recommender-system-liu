from Product.Database.DBConn import session
from Product.Database.DBConn import Rating
import csv

# Read from the csv file. Columns in the ratings.csv: userId,movieId,rating,timestamp
with open('ratings.csv', 'rt') as f:
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
                new_rating = Rating(movie=movie_id, user=user_id, rating=rating)
                session.add(new_rating)

# Commit the added ratings
session.commit()

# Close the csv file
f.close()
