"""
Purpose: Retrieve users from table in database
"""
from Product.Database.DBConn import User
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
