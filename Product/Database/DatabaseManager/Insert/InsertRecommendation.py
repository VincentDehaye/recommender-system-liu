from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendation


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
        Last update: 2017-11-16
        Purpose: Make Inserts to the recommendation table in the database
        """

        for rec in movie_list:
            new_recommendation = Recommendation(movie_id=rec['id'], user_id=user_id)
            self.session.add(new_recommendation)
            print('added movie')
        self.session.commit()
        print('commited for user %s' % user_id)
        self.session.close()