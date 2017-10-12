from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, MovieInGenre, Genre
import csv

# This part handles adding the different genres to the database
# List of all genres that can be seen in the movie lens dataset
genreList = ["Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
             "Drama", "Fantasy", "Film-Noir", "Horror","IMAX", "Musical", "Mystery", "Romance", "Sci-Fi",
             "Thriller", "War", "Western", "(no genres listed)"]


# Add the genres to the db
for genre in genreList:
    new_genre = Genre(name=genre)
    session.add(new_genre)

# This part handles adding the movies of the dataset into the database
# Read the movie.csv file to add data into database
# Columns in the ratings.csv: movieID, titleAndYear, Genres
with open('movies.csv', 'rt') as f:
    reader = csv.reader(f)

    # Iterates through each row in the file and take column one (id) and column 2 (title)
    for row in reader:
        new_movie=Movie(id=row[0], title=row[1])
        session.add(new_movie)

    # Need to commit before filling with movies-genre due to foreign key
    session.commit()
    f.close()

with open('movies.csv', 'rt') as f:
    reader = csv.reader(f)

    for row in reader:
        for counter, column in enumerate(row):
            if counter == 0:
                movie_id = column

            if counter == 2:
                genres = column.split("|")

                # loop through all genres for the movie
                for new_genre in genres:
                    new_movie_genre = MovieInGenre(movie_id=movie_id, genre=new_genre)
                    session.add(new_movie_genre)


# Commit the added link between movies and their genres
session.commit()

# Close the csv file
f.close()



