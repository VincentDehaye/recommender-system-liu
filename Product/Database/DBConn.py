from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os

# More info about database is in educational folder on drive
# Get the path and create the sqlite engine. Echo false means that we do not see generated SQL.
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'app.db'), echo=True)

# Used for the declarative part where we create the model
Base = declarative_base()


# The declarative part that describes the tables. This is and example of a User class.
# Do not forget to import type if you want to use other than integer or string
# The __repr__ returns a string that describes the object

#### EXAMPLE BELOW ####

class UserTest(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (
            self.name, self.password)

#### TRENDING TEAM BELOW ####

#### RECOMMENDATIONS TEAM BELOW ####

#### VISUALIZATION TEAM BELOW ####


#### DO NOT CHANGE BELOW ####

# Creates the tables in the database
Base.metadata.create_all(engine)

# Creating a session binded to the engine. The sessions is used for queries and inserts to db. Remember to import it
# to the file in which you want to do such
Session = sessionmaker(bind=engine)
session = Session()