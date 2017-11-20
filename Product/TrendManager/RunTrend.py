"""
Author: Marten Bolin
Date: 2017-10-28
Last update: 2017-11-20
Purpose: Running TrendManager to get trending score for movies in database
"""

# Do NOT remove or comment away the import below, it is used by docker.
import Product.Database.DBFillSmallSet
from Product.TrendManager.TrendScoreToDatabase import TrendingToDB


# TrendingToDB has two in parameters, daily which sets it to run once daily and daemon which if
# True will make the TrendingToDB to terminate when the application is done
# trending_run.terminate() will stop the TrendingToDB
TRENDING_RUN = TrendingToDB(daily=False)
