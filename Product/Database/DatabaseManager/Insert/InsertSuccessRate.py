from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import SuccessRate


class InsertSuccessRate(Insert):
    """
    Author: Alexander Dahl, John Andre Lidquist
    Date: 2017-11-22
    Last update: 2017-11-22
    Purpose: Make Insertions of successrate into the database
    """
    def insert_success_rate(self, average_total, average_user_experience):
        """
        Author: Alexander Dahl, John Andree Lidquist
        Date: 2017-11-22
        Last update: 2017-11-22
        Purpose: Make Insertions of successrate into the database
        """

        success_rate = SuccessRate(average_total=average_total,
                                   average_user_experience=average_user_experience)
        self.session.add(success_rate)
        self.session.commit()
        self.session.close()