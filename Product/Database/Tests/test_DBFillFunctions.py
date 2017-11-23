"""
Test file to test files in DbFillMovieLens
"""
from Product.Database.DBConn import User
from Product.Database.DBConn import Movie
from Product.Database.DBConn import Genre
from Product.Database.DBConn import MovieInGenre
from Product.Database.DBConn import Rating
from Product.Database.DBConn import create_session

# This is the file to unit test the four DBFill files (DBFillUsers, DBFillMovies, DBFillRatings,
# DBFillLinks). Before the test is run the db should have been created and the four files runned
# (you can do this by running the "DBFillMovieLens" which will run the four files). This test
# file will make sure that the first and last entries in the corresponding csv files has been
# successfully entered into the db. We check this by doing queries and asserting the result
# is the expected.


def test_DBFillUsers():
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-11
    Last Updated:
    Purpose: Assert that users are loaded into the database correctly
    """
    session = create_session()
    result = session.query(User).filter_by(id=1).first()
    assert result.id == 1
    session.close()


# Tests for DBFillMovies
def test_DBFillMovies():
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-11
    Last Updated:
    Purpose: Assert that movies are loaded into the database correctly
    """
    session = create_session()
    result = session.query(Genre).filter_by(name='Action').first()
    assert result.name == 'Action'

    result = session.query(Movie).filter_by(id=1).first()
    assert result.title == "Toy Story"
    assert result.year == 1995

    result = session.query(MovieInGenre).filter_by(movie_id=1).all()
    for counter, res in enumerate(result):
        if counter == 0:
            assert res.genre == "Adventure"
        if counter == 1:
            assert res.genre == "Animation"
        if counter == 2:
            assert res.genre == "Children"
        if counter == 3:
            assert res.genre == "Comedy"
        if counter == 4:
            assert res.genre == "Fantasy"
    session.close()


def test_DBFillRatings():
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-11
    Last Updated:
    Purpose: Assert that ratings are loaded into the database correctly
    """
    session = create_session()
    result = session.query(Rating).filter_by(user_id=1, movie_id=13).first()
    session.close()
    assert result.rating == 5.0
