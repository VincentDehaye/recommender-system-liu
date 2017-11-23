"""
Class for inserting success rate to database
"""
from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import SuccessRate
from Product.Database.DBConn import Recommendation


class InsertSuccessRate(Insert):
    """
    Author: Alexander Dahl, John Andree Lidquist
    Date: 2017-11-22
    Last update: 2017-11-22
    Purpose: Make Insertions of success rate into the database
    """
    def insert_success_rate(self, average_user_success_rate):
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

        watched = self.session.query(Recommendation.watched).filter_by(watched=1).count()
        not_watched = self.session.query(Recommendation).count() - watched

        success_rate = SuccessRate(watched=watched,
                                   not_watched=not_watched,
                                   average_user_success_rate=average_user_success_rate)
        self.session.add(success_rate)
        self.session.commit()
        self.session.close()
