from Product.Database.DBConn import session
from Product.Database.DBConn import User

# Adds 700 users as is used in the Movielens data set.
# Due to no csv file with user they are just added by a loop for now

class FillUsers:
    def __init__(self):
        self.Fill()

    def Fill(self):
        for i in range(1,701):
            new_user = User(id=i)
            session.add(new_user)
        session.commit()