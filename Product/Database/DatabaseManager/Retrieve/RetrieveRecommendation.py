"""
Class for retrieving recommendations from database
"""
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import User
import numpy as np


class RetrieveRecommendation(Retrieve):
    """
    Author: John Andree Lidquist, Alexander Dahl
    Date: 2017-11-20
    Last update: 2017-11-20
    Purpose: Retrieve data from the recommendation table
    """

    def retrieve_watched_ratio(self):
        """
        Author: John Andree Lidquist, Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve data from the recommendation table and count how many of the recommended
        movies have been watched divided by the number of movies not watched
        :return Number of watched movies divided by the number of movies not watched
        """
        number_watched = self.session.query(Recommendation.watched).filter_by(watched=1).count()
        number_of_recommended = self.session.query(Recommendation).count()
        self.session.close()
        if number_of_recommended == 0:
            return 0
        return number_watched/number_of_recommended

    def retrieve_average_user_experience(self):
        """
        Author: John Andree Lidquist, Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve data from the recommendation table and count how many of the recommended
        movies have been watched and how many that have not been watched for each user and then the
        average is returned
        :return The average of the ratios of movies watched divided by movies not watched
        by each user
        """
        users = self.session.query(User).all()

        ratio_list = []
        for user in users:
            recommendations = self.session.query(Recommendation).filter_by(user_id=user.id).all()
            num_watched = 0
            num_recommended = 0
            for rec in recommendations:
                num_recommended += 1
                if rec.watched == 1:
                    num_watched += 1
            if num_recommended != 0:
                ratio_list.append(num_watched/num_recommended)
        self.session.close()

        return np.mean(ratio_list)
