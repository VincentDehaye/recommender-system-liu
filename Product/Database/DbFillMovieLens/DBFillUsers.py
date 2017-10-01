from Product.Database.DBConn import session
from Product.Database.DBConn import User

# Adds 700 users as is used in the Movielens data set. Due to no csv file with user they are just added by a loop

for i in range(699):
    new_user = User()
    session.add(new_user)

session.commit()