from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal
from Product.DataManager.TopTrending.RetrieveTopTrendingYoutube import RetrieveTopTrendingYoutube
from Product.DataManager.TopTrending.RetrieveTopTrendingTwitter import RetrieveTopTrendingTwitter
# It is problems at the moment due to in get_title_and_score it uses total_score
# Total
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
