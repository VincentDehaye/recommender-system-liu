from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import Rating


class RetrieveRating(Retrieve):
    """
    Author: Alexander Dahl
    Date: 2017-11-14
    Last update: 2017-11-14
    Purpose: Retrieve data from rating table in database
    """
    # TODO the logic to get 80% or 10% of the ratings should be done here and not in gets_from_db
    def retrieve_ratings(self):
        ratings = self.session.query(Rating.user_id, Rating.movie_id, Rating.rating).all()

        self.session.close()
        return ratings
