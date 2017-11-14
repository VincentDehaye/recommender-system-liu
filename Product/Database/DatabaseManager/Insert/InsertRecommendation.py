from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendations


class InsertRecommendation(Insert):
    """
    Author: John Andree Lidquist
    Date: 14/11/2017
    Last update: 14/11/2017
    Purpose: Make Insert to the database that has to do with recommendations
    """
    def insert_recommendation(self, movie_id, user_id):
        """
        Author: John Andree Lidquist
        Date: 14/11/2017
        Last update: 14/11/2017
        Purpose: Make Inserts to the recommendation table in the database
        """
        new_recommendation = Recommendations(movie_id=movie_id, user_id=user_id)
        self.session.add(new_recommendation)
        self.session.commit()
        self.session.close()
