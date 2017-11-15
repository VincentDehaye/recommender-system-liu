"""
TopTrendingList Class
"""


class TopTrendingList(object):
    """
    Author: Marten Bolin
    Date: 2017-11-10
    Last update:
    Purpose:
    The list that will be sent to the APIManager
    """
    def __init__(self, list_of_movies, list_of_scores):
        """
        Author: Marten Bolin
        Date: 2017-11-10
        Last update:
        Purpose:
        The constructor of the TopTrendingList, creates a movie list and a score list
        """
        self.list_of_movies = list_of_movies
        self.list_of_scores = list_of_scores

    def print(self):
        """
        Author: Marten Bolin
        Date: 2017-11-10
        Last update:
        Purpose:
        Prints the list
        """
        for (movie, score) in zip(self.list_of_movies, self.list_of_scores):
            print("The movie", movie, "scored", score)

    def dict(self):
        """
        Author: Marten Bolin
        Date: 2017-11-10
        Last update:
        Purpose:
        Returns the list as a dict
        """
        tmp = []
        for title, score in zip(self.list_of_movies, self.list_of_scores):
            tmp.append({"title": title, "score": score})
        return {"list": tmp}
