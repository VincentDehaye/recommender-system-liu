from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendations


class InsertTrending(Insert):
    def insert_recommendation(self, movie_id, user_id):

        new_recommendation = Recommendations(movie_id=movie_id, user_id=user_id)
        self.session.add(new_recommendation)
        self.session.commit()
        self.session.close()
