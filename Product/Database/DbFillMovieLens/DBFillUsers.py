from Product.Database.DBConn import User
from Product.Database.DBConn import create_session
import csv
import os
import sys
'''
Author: Eric Petersson, Vincent Dehaye
Date: 21/11/2017
Last update: 21/11/2017
Purpose: Adds 700 users with mock metadata to the database.
'''


class FillUsers:
    def __init__(self):
        self.session = create_session()
        self.fill()

    def fill(self):
        filepath = (os.path.dirname(sys.modules['__main__'].__file__))
        filepath += '/MockData/users_with_mock_metadata.csv'
        with open(filepath) as csvfile_users:
            reader = csv.reader(csvfile_users)

            print("Filling database with mock metadata.")
            for line in reader:
                new_user = User(age=int(line[0]), gender=line[1], occupation=line[2])
                self.session.add(new_user)
            self.session.commit()
            print("DONE - Users added")
