import os
import Product
from Product.Database.DbFillMovieLens.DBFillMovies import FillMovies
from Product.Database.DbFillMovieLens.DBFillRatings import FillRatings
from Product.Database.DbFillMovieLens.DBFillUsers import FillUsers
from Product.Database.DbFillMovieLens.DBFillLinks import FillLinks



# The imports are grayed out, but they will run anyway.

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)

# 1. Create the a new database (by running DBConn)
import Product.Database.DBConn

# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)
u = FillUsers()
f = FillMovies(True)
r = FillRatings(True)
#l = FillLinks

#import Product.Database.DbFillMovieLens.DBFillUsers
#import Product.Database.DbFillMovieLens.DBFillMovies
#import Product.Database.DbFillMovieLens.DBFillRatings
#import Product.Database.DbFillMovieLens.DBFillLinks

