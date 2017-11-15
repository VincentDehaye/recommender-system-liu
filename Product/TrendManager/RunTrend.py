"""
Running TrendManager to get trending score for movies in database
"""
from Product.TrendManager.TrendScoreToDatabase import TrendingToDB
import Product.Database.DBFillSmallSet
import time
# TrendingToDB has two in parameters, daily which sets it to run once daily and daemon which if
# True will make the TrendingToDB to terminate when the application is done
# trending_run.terminate() will stop the TrendingToDB
trending_run = TrendingToDB(daily=False)
# time.sleep(150)
# trending_run.terminate()
