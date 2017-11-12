from Product.DataManager.TopTrending.RetrieveTopTrending import RetrieveTopTrending


class RetrieveTopTrendingTwitter(RetrieveTopTrending):

    def get_top_trending(self, number_of_titles):
        top_trend=self.trender.get_trending_twitter(number_of_titles)
        return self.get_title_and_score(top_trend)

    def get_score(self, entry):
        return entry.twitter_score
