import os
import Product
from Product.Database.DbFillMovieLens.DBFillMovies import FillMovies
from Product.Database.DbFillMovieLens.DBFillRatings import FillRatings
from Product.Database.DbFillMovieLens.DBFillUsers import FillUsers
from Product.Database.DbFillMovieLens.DBFillLinks import FillLinks

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)

# 1. Create the a new database (by running DBConn)
# The import is grayed out, but will run anyway.
import Product.Database.DBConn

# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)
useSmallDataSet = False
u = FillUsers()
f = FillMovies(useSmallDataSet)
r = FillRatings(useSmallDataSet)

# Not used at the moment and therefore 
# l = FillLinks()

