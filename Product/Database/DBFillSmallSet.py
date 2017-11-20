import os
import Product
from Product.Database.DbFillMovieLens.DBFillMovies import FillMovies
from Product.Database.DbFillMovieLens.DBFillRatings import FillRatings
from Product.Database.DbFillMovieLens.DBFillUsers import FillUsers
from Product.Database.DbFillMovieLens.DBFillLinks import FillLinks
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser

'''
Author: John Andree Lidquist, Marten Bolin
Date: 12/10/2017
Last update: 9/11/2017
Purpose: Fills the database with the small data set (40 movies) made for testing
'''

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)

# 1. Create the a new database (by running DBConn)
# The import is grayed out, but will run anyway.
import Product.Database.DBConn

retriever = RetrieveUser()
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies, DBFillRatings and DBFillLinks)
if retriever.check_if_user_in_rating(1) is None:
    useSmallDataSet = True
    u = FillUsers()
    print("Fyllt users en gang.")
    f = FillMovies(useSmallDataSet)
    r = FillRatings(useSmallDataSet)
    print("No links added (not necessary)")
    # There are no Links created for the small data set
else:
    print("There is already an existing database.")

