from Product.Database.DatabaseManager.Insert.InsertFeedback import InsertFeedback


class Feedback(object):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update:
    Purpose: Make Insert of sent Feedback
    """
    @staticmethod
    def insert_feedback(user_id, movie_id, watched=None, rating=None):
            """
            Author: Alexander Dahl, Marten Bolin
            Date: 2017-11-17
            Last update:
            Purpose: Make Insert of Feedback to the database
            :param user_id : The id of the user that has made the rating or watched
            :type int
            :param movie_id : The id of the movie that has been rated or watched
            :type int
            :param watched : 1 if has watched (optional)
            :type int
            :param rating : the rating that was made, 1-5 (optional)
            :type float
            """
            InsertFeedback().insert_feedback(user_id, movie_id, watched, rating)

# Feedback.insert_feedback(user_id=1,movie_id=24,watched=None, rating=276)
