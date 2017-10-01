from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, MovieInGenre, Genre
import csv

# This part handles adding the different genres to the database
# List of all genres that can be seen in the movie lens dataset
genreList = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary",
             "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
             "Thriller", "War", "Western", "no genres listed"]

# Add the genres to the db
for genre in genreList:
    new_genre = Genre(name=genre)
    session.add(new_genre)


# This part handles adding the movies of the dataset into the database
# Read the movie.csv file to add data into database
# Columns in the ratings.csv: movieID, titleAndYear, Genres
with open('movies.csv', 'rt') as f:
    reader = csv.reader(f)

    # Iterates through each row in the file
    for row in reader:

        # Iterates through each column
        for counter, column in enumerate(row):

            if counter == 0:
                movie_id = column

            if counter == 1:
                new_movie = Movie(id = movie_id, title = column)
                session.add(new_movie)

            if counter == 2:
                genres = column.split("|")

                # loop through all genres for the movie
                for new_genre in genres:
                    new_genre = MovieInGenre(movie=movie_id, genre=new_genre)
                    session.add(new_genre)

# Commit the added movies and their genres
session.commit()

# Close the csv file
f.close()




