from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Rating


class InsertRecommendation(Insert):
    """
    Author: John Andree Lidquist
    Date: 14/11/2017
    Last update: 14/11/2017
    Purpose: Make Insert to the database that has to do with recommendations
    """
    def insert_recommendation(self, movie_list, user_id):
        """
        Author: John Andree Lidquist
        Date: 14/11/2017
        Last update: 14/11/2017
        Purpose: Make Inserts to the recommendation table in the database
        """
        print(movie_list)
        # TODO there is an error here when the corresponding user_id and movie_id already
        # TODO exists in the database, how should that be fixed?
        # TODO broken by Alexander Dahl
        for rec in movie_list:
            print(rec['id'])
            new_recommendation = Rating(movie_id=rec['id'], user_id=user_id, rating=None)
        #print(new_recommendation)
            self.session.add(new_recommendation)
            self.session.commit()
        self.session.close()
