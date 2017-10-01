import os

# This script will
# 1. Delete the old database app.db
# 2. Create the a new one (by running DBConn)
# 3. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings)


# 1. Delete the old database app.db
os.remove("../Database/app.db")

# 2. Create the a new one (by running DBConn)
import Product.Database.DBConn

# 3. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings)
import Product.Database.DbFillMovieLens.DBFillUsers
import Product.Database.DbFillMovieLens.DBFillMovies
import Product.Database.DbFillMovieLens.DBFillRatings
