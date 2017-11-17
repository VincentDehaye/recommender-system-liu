from Product.Database.DatabaseManager.Insert.InsertUser import InsertUser


class InsertNewUser(object):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update:
    Purpose: Make Insert of Feedback to the database
    """
    @staticmethod
    def insert_user(age, gender, occupation=None):
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
        InsertUser().insert_user(age=age, gender=gender,occupation=occupation)
