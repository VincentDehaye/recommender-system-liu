from Product.Database.Retrieve.RetrieveMovie import RetrieveMovie

from Product.DataManager.TopTrending.TopTrendingList import TopTrendingList
from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending


class RetrieveTopTrending:
    def __init__(self):
        self.trender = RetrieveTrending()
        self.movie_getter = RetrieveMovie()

    def get_title_and_score(self, list_of_trending_movies):
        title_list = []
        score_list = []
        for entry in list_of_trending_movies:
            movie = self.movie_getter.retrieve_movie(entry.movie_id)
            title_list.append(movie.title)
            score_list.append(self.get_score(entry))
        return TopTrendingList(title_list, score_list)

    # This method gets overridden in RetrieveTopTrendingYoutube/Twitter so that the right score is added
    def get_score(self, entry):
        return entry.total_score
