from Product.Database.DbFillMovieLens.DBConn import User
from Product.Database.DbFillMovieLens.DBConn import session

# Adds 700 users as is used in the Movielens data set.
# Due to no csv file with user they are just added by a loop for now

for i in range(1,701):
    new_user = User(id=i)
    session.add(new_user)

session.commit()