from Product.Database.DBConn import session
#!/bin/bash
import csv

genreList = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary",
             "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
             "Thriller", "War", "Western", "no genres listed"]

for genre in genreList:
    session.add(genre)

with open('movies.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)