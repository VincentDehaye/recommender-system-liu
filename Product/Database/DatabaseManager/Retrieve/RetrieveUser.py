"""
Purpose: Retrieve users from table in database
"""
from Product.Database.DBConn import User,Rating
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve


class RetrieveUser(Retrieve):
    """
    Author:Alexander Dahl
    Date: 2017-11-14
    Last update: 2017-11-14
    Purpose: Retrieve users from table in database
    """
    def retrieve_all_users(self):
        """
        Author: Alexander Dahl
        Date: 2017-11-14
        Last update: 2017-11-14
        Purpose: retrieve users from table
        :return users : list of class User
        """
        users = self.session.query(User).all()
        self.session.close()
        return users

    def check_if_user_in_rating(self, user_id):
        # TODO and check so that rating is not null, return boolean instead of object.
        return self.session.query(Rating).filter_by(user_id=user_id).first()


