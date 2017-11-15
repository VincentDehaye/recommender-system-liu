import os
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
'''
Author: John Andree Lidquist, Marten Bolin
Date: 12/10/2017
Last update: 9/11/2017
Purpose: Creates the database and the database model
'''

# More info about database is in educational folder on drive
# Get the path and create the sqlite engine. Echo false means that we do not see generated SQL.
basedir = os.path.abspath(os.path.dirname(__file__))

try:
    PRODUCTION_DATABASE = os.environ['PRODUCTION_DATABASE'] == '1'
except KeyError:
    PRODUCTION_DATABASE = False
finally:
    if not PRODUCTION_DATABASE:
        engine = create_engine('sqlite:///' + os.path.join(basedir, 'app.db'), connect_args={'check_same_thread': False}, echo=False)
        # Used to turn foreign keys on in SQLite since this is by default
        @event.listens_for(engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
    else:
        DATABASE = os.environ["DATA_DATABASE_HOST"]
        engine = create_engine('mysql+pymysql://root:example@' + DATABASE + '/main')


# Used for the declarative part where we create the model
Base = declarative_base()


# The declarative part that describes the tables. This is and example of a User class.
# Do not forget to import type if you want to use other than integer or string
# The __repr__ returns a string that describes the object

# EXAMPLE BELOW

class UserTest(Base):
    __tablename__ = 'testusers'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    password = Column(String(200))

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (
            self.name, self.password)

# This Model is for Genres
class Genre(Base):
    __tablename__ = 'genres'

    name = Column(String(100), primary_key=True)

    def __repr__(self):
        return "<Genre(name='%s')>" % (
            self.name)


# This class is for movies
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    year = Column(Integer)

    def __repr__(self):
        return "<Movie(id='%s', title='%s', year='%s)>" % (
            self.id, self.title, self.year)


# This class contains the trending scores of the movies. movie_id is a foreign key referencing the Movie table
# total_score is a float that represents the total trending score. youtube_score and twitter_score are floats that
# represent the trending scores of these seperate factors


class TrendingScore(Base):
    __tablename__ = 'trendingscores'
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    total_score = Column(Float)
    youtube_score = Column(Float)
    twitter_score = Column(Float)

    def __eq__(self, other):
        return self == other


# This class is for users
class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    age = Column(Integer, default=-1)
    gender = Column(String(30), default="Unknown")
    occupation = Column(String(30), default="Unknown")

    def __repr__(self):
        return "<User(id='%s', age='%s', gender='%s', occupation='%s')>" % (
            self.id, self.age, self.gender, self.occupation)


# Class for the relation between Movies and Users, in this case ratings.
# Foreign key to User table and Movie table
class Rating(Base):
    __tablename__ = 'ratings'
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    rating = Column(Float)

    def __repr__(self):
        return "<Rated(user='%s', rated='%s', rating='%s')>" % (
            self.user_id, self.movie_id, self.rating)


# Class for movies in genres. Foreign key references to Movie and Genre.
class MovieInGenre(Base):
    __tablename__ = 'movieingenre'
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    genre = Column(String(100), ForeignKey(Genre.name), primary_key=True)

    def __repr__(self):
        return "<Genre(movie_id='%s', genre='%s')>" % (
            self.movie_id, self.genre)


# Class for link between IMDB, TMDB and the id for a movie in the MovieLens data set.
# First column is movie_id id
# Second column is imdb id and last column is tmdb id.
class MovieLinks(Base):
    __tablename__ = 'movielinks'
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    imdb_id = Column(Integer)
    tmdb_id = Column(Integer)

    def __repr__(self):
        return "<Genre(movie_id id='%s', imdb id='%s', tmdb id='%s')>" % (
            self.movie_id, self.imdb_id, self.tmdb_id)


# DO NOT CHANGE BELOW
def create_session():
    # Creates the tables in the database
    Base.metadata.create_all(engine)

    # Creating a session binded to the engine. The sessions is used for queries and inserts to db. Remember to import it
    # to the file in which you want to do such
    Session = sessionmaker(bind=engine)
    return Session()

session=create_session()
