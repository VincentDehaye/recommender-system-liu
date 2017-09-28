from Product.Database.DBConn import session
from Product.Database.DBConn import Genre
#!/bin/bash
import csv

# List of all genres
genreList = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary",
             "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
             "Thriller", "War", "Western", "no genres listed"]
# This list is put into the database
for genre in genreList:
    new_genre = Genre(name=genre)
    session.add(new_genre)
session.commit()

# To see how to read from csv files
with open('movies.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)