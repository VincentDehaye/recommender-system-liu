from Product.Database.DBConn import session
from Product.Database.DBConn import Genre, Movie, MovieInGenre
#!/bin/bash
import csv
import re

# List of all genres
#genreList = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary",
#             "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
#             "Thriller", "War", "Western", "no genres listed"]
# This list is put into the database
#for genre in genreList:
#    new_genre = Genre(name=genre)
#    session.add(new_genre)
#session.commit()

# To see how to read from csv files
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

            session.commit()

#Close the csv file
f.close()

