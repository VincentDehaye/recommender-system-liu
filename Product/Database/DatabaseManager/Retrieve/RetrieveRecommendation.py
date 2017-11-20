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

    def retrieve_watched_and_not_watched(self):
        """
        Author: John Andree Lidquist, Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve data from the recommendation table and count how many of the recommended movies have been
        watched and how many that have not been watched
        """
        number_watched = self.session.query(Recommendation.watched).filter_by(watched=1).count()
        number_not_watched = self.session.query(Recommendation).count() - number_watched
        self.session.close()
        return number_watched, number_not_watched

    def retrieve_average_user_experience(self):
        """
        Author: John Andree Lidquist, Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve data from the recommendation table and count how many of the recommended movies have been
        watched and how many that have not been watched for each user and then the average is returned
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
