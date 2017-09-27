from Product.DBConn import UserTest
from Product.DBConn import session

# The below is an example
# Create new objects
new_user = UserTest(name='marten', password='bolin')
new_user2 = UserTest(name='ariyan', password='abdulla')

# Add the object to the session
session.add(new_user)
session.add(new_user2)

# Commit to the database
session.commit()

# Get Ariyan out of db
slim_shady = session.query(UserTest).filter_by(id='1').first()



print(slim_shady)