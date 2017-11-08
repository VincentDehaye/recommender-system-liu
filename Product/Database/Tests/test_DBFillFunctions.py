from Product.Database.DBConn import User, Movie, Genre, MovieInGenre, Rating, MovieLinks
from Product.Database.DBConn import session

# This is the file to unit test the four DBFill files (DBFillUsers, DBFillMovies, DBFillRatings, DBFillLinks)
# Before the test is run the db should have been created and the four files runned (you can do this by running
# the "DBFillMovieLens" which will run the four files). This test file will make sure that the first and last
# entries in the corresponding csv files has been successfully entered into the db. We check this by doing queries
# and asserting the result is the expected


# Tests for DBFillUsers
def test_DBFillUsers():
    result = session.query(User).filter_by(id=1).first()
    assert result.id == 1


# Tests for DBFillMovies
def test_DBFillMovies():
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


# Tests for DBFillRatings
def test_DBFillRatings():
    result = session.query(Rating).filter_by(user_id=1, movie_id=13).first()
    assert result.rating == 5.0







