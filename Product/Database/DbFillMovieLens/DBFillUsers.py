from Product.Database.DBConn import User
from Product.Database.DBConn import create_session

'''
Author: John Andree Lidquist, Marten Bolin
Date: 12/10/2017
Last update: 9/11/2017
Purpose: Adds 700 users to the database to be used together
with the Movielens data set.
'''

import random

# Adds 700 users as is used in the Movielens data set.
# Due to no csv file with user they are just added by a loop for now
class FillUsers:
    def __init__(self):
        self.session = create_session()
        self.fill()

    # def fill(self):
    #     print("Starting to fill 700 users, not based on big or small data set..")
    #     for i in range(1, 701):
    #         new_user = User(id=i)
    #         self.session.add(new_user)
    #     self.session.commit()
    #     print("DONE - Users added")
    def fill(self):
        def GenerateUser(id):
            occupation_set = ['secretary',
                              'artist',
                              'doctor',
                              'teacher',
                              'engineer',
                              'executive',
                              'nurse',
                              'lawyer',
                              'librarian',
                              'none',
                              'programmer',
                              'retired',
                              'salesman',
                              'scientist',
                              'student',
                              'model',
                              'politician']

            occupation_set_female = ['secretary',
                                     'artist',
                                     'doctor', 'doctor',
                                     'teacher',
                                     'engineer', 'engineer', 'engineer', 'engineer',
                                     'engineer', 'engineer', 'engineer', 'engineer',
                                     'executive',
                                     'nurse',
                                     'lawyer', 'lawyer',
                                     'librarian',
                                     'none',
                                     'programmer', 'programmer', 'programmer',
                                     'programmer', 'programmer', 'programmer',
                                     'retired',
                                     'salesman',
                                     'scientist',
                                     'student', 'student', 'student', 'student',
                                     'model',
                                     'politician', 'politician', 'politician', 'politician']

            occupation_set_male = ['secretary', 'secretary', 'secretary', 'secretary',
                                   'secretary', 'secretary', 'secretary', 'secretary',
                                   'artist',
                                   'doctor',
                                   'teacher',
                                   'engineer',
                                   'executive',
                                   'nurse', 'nurse', 'nurse', 'nurse', 'nurse',
                                   'nurse', 'nurse', 'nurse', 'nurse', 'nurse',
                                   'lawyer',
                                   'librarian',
                                   'none',
                                   'programmer',
                                   'retired',
                                   'salesman',
                                   'scientist',
                                   'student',
                                   'model', 'model', 'model', 'model', 'model',
                                   'model', 'model', 'model', 'model', 'model',
                                   'politician']

            gender_set = ['Unknown', 'Other', 'Male', 'Female']
            gender = random.choice(gender_set)
            age = random.randint(0, 100)
            if (age < 18):
                occupation = 'student'
            elif (age > 65):
                occupation = 'retired'
            else:
                if (gender == 'Female'):
                    occupation = random.choice(occupation_set_female)
                elif (gender == 'Male'):
                    occupation = random.choice(occupation_set_male)
                else:
                    occupation = random.choice(occupation_set)

            new_user = User(id=id, age=age, gender=gender, occupation=occupation)

            return new_user
        print("Filling database with mock metadata.")
        for i in range(1, 701):
            new_user = GenerateUser(i)
            self.session.add(new_user)
        self.session.commit()
        print("DONE - Users added")
