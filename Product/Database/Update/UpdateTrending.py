from Product.Database.Update import Update

class UpdateTrending(Update):
    def update_trend_score(self, movie_id, total_score=None, youtube_score=None, twitter_score=None):
        self.session