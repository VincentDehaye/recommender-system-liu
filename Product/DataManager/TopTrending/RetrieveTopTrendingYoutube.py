from Product.DataManager.TopTrending.RetrieveTopTrending import RetrieveTopTrending

class RetrieveTopTrendingYoutube(RetrieveTopTrending):

    def get_top_trending(self, number_of_titles):
        top_trend=self.trender.get_trending_youtube(number_of_titles)
        return self.get_title_and_score(top_trend)