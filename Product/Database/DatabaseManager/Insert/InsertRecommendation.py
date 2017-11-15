from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendation
from sqlalchemy import exists

class InsertRecommendation(Insert):
    """
    Author: John Andree Lidquist
    Date: 14/11/2017
    Last update: 14/11/2017
    Purpose: Make Insert to the database that has to do with recommendations
    """
    def insert_recommendation(self, movie_list, user_id):
        """
        Author: Alexander Dahl
        Date: 2017-11-15
        Last update: 2017-11-15
        Purpose: Make Inserts to the recommendation table in the database
        """
        for rec in movie_list:
            new_recommendation = Recommendation(movie_id=rec['id'], user_id=user_id)
            self.session.add(new_recommendation)
            self.session.commit()
        self.session.close()
