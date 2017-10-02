import os

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)

# 1. Create the a new database (by running DBConn)
import Product.Database.DBConn

# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)
import Product.Database.DbFillMovieLens.DBFillUsers
import Product.Database.DbFillMovieLens.DBFillMovies
import Product.Database.DbFillMovieLens.DBFillRatings
import Product.Database.DbFillMovieLens.DBFillLinks
