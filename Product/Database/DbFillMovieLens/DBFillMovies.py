from Product.Database.DBConn import session
from Product.Database.DBConn import Movie, MovieInGenre
import csv

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
# Close the csv file
f.close()




