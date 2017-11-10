from Product.Database.DBConn import User
from Product.Database.DBConn import create_session

'''
Author: John Andree Lidquist, Marten Bolin
Date: 12/10/2017
Last update: 9/11/2017
Purpose: Adds 700 users to the database to be used together
with the Movielens data set.
'''


class FillUsers:
    def __init__(self):
        self.session = create_session()
        self.fill()

    def fill(self):
        print("Starting to fill 700 users, not based on big or small data set..")
        for i in range(1, 701):
            new_user = User(id=i)
            self.session.add(new_user)
        self.session.commit()
        print("DONE - Users added")
