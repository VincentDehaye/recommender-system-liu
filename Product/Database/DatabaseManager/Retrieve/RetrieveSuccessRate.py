"""
Class for retrieving recommendations from database
"""
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import User
from Product.Database.DBConn import SuccessRate
import numpy as np


class RetrieveSuccessRate(Retrieve):
    """
    Author: John Andree Lidquist, Alexander Dahl
    Date: 2017-11-20
    Last update: 2017-11-23
    Purpose: Retrieve data from the recommendation table
    """
    def get_simple_success_rate(self):
        """
        Author: John Andree Lidquist, Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-23
        Purpose: Retrieve data from the recommendation table and count how many of the recommended
        movies have been watched divided by the number of movies not watched
        :return Number of watched movies divided by the number of movies not watched
        """
        return self.session.query(SuccessRate).all()

    def get_average_user_success_rate(self):
        """
        Author: John Andree Lidquist, Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-23
        Purpose: Retrieve data from the recommendation table and count how many of the recommended
        movies have been watched and how many that have not been watched for each user and then the
        average is returned
        :return The average of the ratios of movies watched divided by movies not watched
        by each user
        """
        return self.session.query(SuccessRate).all()
