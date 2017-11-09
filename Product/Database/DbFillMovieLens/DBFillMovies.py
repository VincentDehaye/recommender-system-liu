from Product.Database.DBConn import session, Movie, MovieInGenre, Genre
import csv, re, os.path

class FillMovies:

    def __init__(self, smallDataSet):
        self.fill(smallDataSet)

    def fill(self, smallDataSet):

        # This part handles adding the different genres to the databas
        # List of all genres that can be se en in the movie lens dataset
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
        if smallDataSet:
            fullpath = 'DbFillMovieLens/smallMovies.csv'
            path = os.path.abspath(fullpath)
            # /home/marbo914/PycharmProjects/Software/Product/Database/DbFillMovieLens/smallMovies.csv
            print("Starting to fill movies from small data set..")
        else:
            fullpath = 'DbFillMovieLens/movies.csv'
            path = os.path.abspath(fullpath)
            print("Starting to fill movies from BIG data set..")

        with open(path, 'rt', encoding="utf-8") as f:
            reader = csv.reader(f)

            # Iterates through each row in the file and take column one (id) and column 2 (title)
            for row in reader:

                # Search the title string of row[1] of occurances for (yyyy) and (yyyy-) for series
                # Then checks length if it was found and puts it in the new_movie if year is
                # not found it goes into the else statement and no year is inputted to the creation
                searchForYear = re.split(r" \(([0-9][0-9][0-9][0-9])+\)", row[1])
                searchForYearSeries = re.split(r"\(([0-9][0-9][0-9][0-9]-)+\)", row[1])
                if len(searchForYear)>1:
                    new_movie=Movie(id=row[0], title=searchForYear[0], year=searchForYear[1])
                elif len(searchForYearSeries)>1:
                    new_movie=Movie(id=row[0], title=searchForYearSeries[0], year=searchForYearSeries[1])
                else:
                    new_movie=Movie(id=row[0], title=row[1])
                session.add(new_movie)

            # Need to commit before filling with movies-genre due to foreign key
            session.commit()
            f.close()

        with open(path, 'rt', encoding="utf-8") as f:
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
        print("DONE - Movies added")

        # Close the csv file
        f.close()



