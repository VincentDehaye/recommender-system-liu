from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import Rating


class InsertFeedback(Insert):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update:
    Purpose: Make Insert of Feedback to the database
    """
    def insert_feedback(self, user_id, movie_id, watched=None, rating=None):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 2017-11-17
        Last update:
        Purpose: Make Feedback inserts to the database
        :param user_id : The id of the user that has made the rating or watched
        :type int
        :param movie_id : The id of the movie that has been rated or watched
        :type int
        :param watched : 1 if has watched (optional)
        :type int
        :param rating : the rating that was made, 1-5 (optional)
        :type float
        """
        current_recommendation = self.session.query(Recommendation).filter_by(movie_id=movie_id, user_id=user_id).first()
        if watched and current_recommendation:
            current_recommendation.watched = watched
        if rating:
            current_rating = self.session.query(Rating).filter_by(movie_id=movie_id, user_id=user_id).first()
            if not current_rating:
                new_rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
                self.session.add(new_rating)
            else:
                current_rating.rating = rating

        self.session.commit()
        print('committed for user %s' % user_id)
        self.session.close()
