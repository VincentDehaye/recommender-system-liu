from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal
from Product.DataManager.TopTrending.RetrieveTopTrendingYoutube import RetrieveTopTrendingYoutube
from Product.DataManager.TopTrending.RetrieveTopTrendingTwitter import RetrieveTopTrendingTwitter

# This file is only for our own testing of the RetreiveTopTrending files

trender = RetrieveTopTrendingTotal()
Trends = trender.get_top_trending(10)
print("This is total:")
Trends.print()

# Youtube
trender = RetrieveTopTrendingYoutube()
Trends = trender.get_top_trending(10)
print("This is youtube:")
Trends.print()

# Twitter
trender = RetrieveTopTrendingTwitter()
Trends = trender.get_top_trending(10)
print("This is Twitter:")
Trends.print()
print(Trends.dict())
