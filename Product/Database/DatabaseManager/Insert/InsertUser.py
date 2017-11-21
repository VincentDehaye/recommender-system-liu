from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import User


class InsertUser(Insert):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update:
    Purpose: Make Insert of Feedback to the database
    """

    def insert_user(self, age, gender, occupation=None):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 2017-11-17
        Last update:
        Purpose: Make Feedback inserts to the database
        :param age : The age of the user
        :type int
        :param gender : The gender of the user
        :type String
        :param occupation : The occupation of the user (Optional)
        :type String
        """
        if occupation:
            new_user = User(age=age, gender=gender, occupation=occupation)
        else:
            new_user = User(age=age, gender=gender, occupation=occupation)
        self.session.add(new_user)
        self.session.commit()
        print('commited for user %s' % gender)
        self.session.close()