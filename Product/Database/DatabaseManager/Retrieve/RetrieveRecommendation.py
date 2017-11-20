from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import Recommendation


class RetrieveRecommendation(Retrieve):
    """
    Author: John Andree Lidquist, Alexander Dahl
    Date: 2017-11-20
    Last update: 2017-11-20
    Purpose: Retrieve data from the recommendation table and count how many of the recommended movies have been watched
    """

    def retrieve_watched(self):
        number_watched = self.session.query(Recommendation.watched).filter_by(watched=1).count()
        number_not_watched = self.session.query(Recommendation).count() - number_watched
        self.session.close()
        return number_watched, number_not_watched
