import os
import Product


# The imports are grayed out, but they will run anyway.

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)

# 1. Create the a new database (by running DBConn)
import Product.Database.DBConn

# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)
import Product.Database.DbFillMovieLensGitLab.DBFillUsers
import Product.Database.DbFillMovieLensGitLab.DBFillMovies
import Product.Database.DbFillMovieLensGitLab.DBFillRatings
import Product.Database.DbFillMovieLensGitLab.DBFillLinks

