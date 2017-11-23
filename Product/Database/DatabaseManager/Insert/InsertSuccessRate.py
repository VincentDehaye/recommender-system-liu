"""
Class for inserting success rate to database
"""
from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import SuccessRate


class InsertSuccessRate(Insert):
    """
    Author: Alexander Dahl, John Andree Lidquist
    Date: 2017-11-22
    Last update: 2017-11-22
    Purpose: Make Insertions of success rate into the database
    """
    def insert_success_rate(self, average_total, average_user_experience):
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

        success_rate = SuccessRate(average_total=average_total,
                                   average_user_experience=average_user_experience)
        self.session.add(success_rate)
        self.session.commit()
        self.session.close()
