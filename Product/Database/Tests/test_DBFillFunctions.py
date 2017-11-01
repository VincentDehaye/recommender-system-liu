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

    result = session.query(User).filter_by(id=700).first()
    assert result.id == 700

# Tests for DBFillMovies
def test_DBFillMovies():
    result = session.query(Genre).filter_by(name='Action').first()
    assert result.name == 'Action'

    result = session.query(Movie).filter_by(id=1).first()
    assert result.title == "Toy Story"
    assert result.year == 1995

    result = session.query(Movie).filter_by(id=164979).first()
    print(result.title)
    assert result.title == "Women of '69, Unboxed"

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


    result = session.query(MovieInGenre).filter_by(movie_id=164979).first()
    assert result.genre == "Documentary"

# Tests for DBFillRatings
def test_DBFillRatings():
    result = session.query(Rating).filter_by(user_id=1, movie_id=31).first()
    assert result.rating == 2.5

    result = session.query(Rating).filter_by(user_id=671, movie_id=6565).first()
    assert result.rating == 3.5

# Tests for DBFillLinks
def test_DBFillLinks():
    result = session.query(MovieLinks).filter_by(movie_id=1).first()
    assert result.imdb_id == 114709
    assert result.tmdb_id == 862

    result = session.query(MovieLinks).filter_by(movie_id=164979).first()
    assert result.imdb_id == 3447228
    assert result.tmdb_id == 410803






