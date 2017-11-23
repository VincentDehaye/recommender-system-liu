from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import SuccessRate


class RetrieveSuccessRate(Retrieve):
    """
    Author: John Andree Lidquist
    Date: 2017-11-23
    Last update:
    Purpose: Retrieve data from SuccessRate table in database
    """

    def retrieve_success_rate(self):
        """
        Author: John Andree Lidquist
        Date: 2017-11-23
        Last update:
        Purpose: Retrieve all success rates over time from table in database
        :return All the success rates
        """
        return self.session.query(SuccessRate).all()
