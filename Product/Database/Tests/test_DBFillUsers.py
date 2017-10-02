from Product.Database.DBConn import User, Movie, Genre, MovieInGenre
from Product.Database.DBConn import session


def test_DBFillUsers():
    result = session.query(User).filter_by(id=1).first()
    assert result.id == 1

    result = session.query(User).filter_by(id=700).first()
    assert result.id == 700


def test_DBFillMovies():
    result = session.query(Genre).filter_by(name='Action').first()
    assert result.name == 'Action'

    result = session.query(Movie).filter_by(id=1).first()
    assert result.title == "Toy Story (1995)"

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







