from Product.DataManager.TopTrending.RetrieveTopTrending import RetrieveTopTrending

class RetrieveTopTrendingTotal(RetrieveTopTrending):

    def get_top_trending(self, number_of_titles):
        top_trend=self.trender.retrieve_trend_score(number_of_titles=number_of_titles)
        return self.get_title_and_score(top_trend)
