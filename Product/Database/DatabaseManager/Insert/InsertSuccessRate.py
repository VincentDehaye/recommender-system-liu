"""
Class for inserting success rate to database
"""
from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import SuccessRate
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import User
import numpy as np


class InsertSuccessRate(Insert):
    """
    Author: Alexander Dahl, John Andree Lidquist
    Date: 2017-11-22
    Last update: 2017-11-22
    Purpose: Make Insertions of success rate into the database
    """
    def insert_success_rate(self):
        """
        Author: Alexander Dahl, John Andree Lidquist
        Date: 2017-11-22
        Last update: 2017-11-22
        Purpose: Make Insertions of success rate into the database
        :param average_total: The number of watched movies divided of the number of recommended
         movies for all users
        :type average_total: float
        :param average_user_experience: The average number of watched movies divided by the
        number of recommended movies for each users
        :type average_user_experience: float
        """
        # TODO change docstring to match params
        # Calculate watched and not watched up until now
        watched = self.session.query(Recommendation.watched).filter_by(watched=1).count()
        not_watched = self.session.query(Recommendation).count() - watched

        # Calculate average user success rate up until now
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
        average_user_success_rate = np.mean(ratio_list)

        success_rate = SuccessRate(watched=watched,
                                   not_watched=not_watched,
                                   average_user_success_rate=average_user_success_rate)
        self.session.add(success_rate)
        self.session.commit()
        self.session.close()
