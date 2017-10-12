from Product.TrendManager import TrendingController
from Product.TrendManager import ScoredMovie

trendController = TrendingController()
scoredMovie = trendController.get_trending_content("pirates")
print(scoredMovie.score)