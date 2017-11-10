class TopTrending:
    def __init__(self, list_of_movies, list_of_scores):
        self.list_of_movies=list_of_movies
        self.list_of_scores=list_of_scores

    def print(self):
        for (movie,score) in zip(self.list_of_movies,self.list_of_scores):
            print("The movie",movie,"scored",score,".")