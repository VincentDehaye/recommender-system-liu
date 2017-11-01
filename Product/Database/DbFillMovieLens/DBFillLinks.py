from Product.Database.DBConn import session
from Product.Database.DBConn import MovieLinks
import csv

# Read the movie_id.csv file to add data into database.
# Columns in the ratings.csv: movieId, imdbID, tmdbID
with open('Product/Database/DbFillMovieLens/links.csv', 'rt') as f:
    reader = csv.reader(f)

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
                new_linking = MovieLinks(movie_id=new_movie_id, imdb_id=new_imdb_id, tmdb_id=new_tmdb_id)
                session.add(new_linking)


# Commit the added ratings
session.commit()

# Close the csv file
f.close()