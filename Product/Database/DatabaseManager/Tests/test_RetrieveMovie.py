from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Movie


def test_retrieve_movie():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Last Updated:
    Purpose: Assert that a movie, or all movies, are retrieved correctly
    """

    # PRE-CONDITIONS
    movie_id = -3
    movie_title = "dummy"
    movie_year = 1111

    # We create a session and add a dummy movie that we can later retrieve
    session = create_session()
    dummy_movie = Movie(id=movie_id, title=movie_title, year=movie_year)
    session.add(dummy_movie)
    session.commit()


    # EXPECTED OUTPUT
    expected_id = movie_id
    expected_title = movie_title
    expected_year = movie_year

    # OBSERVED OUTPUT
    # We query the the movie to get a observed output
    observed = RetrieveMovie().retrieve_movie(movie_id=movie_id)

    # After adding the dummy movie and the dummy trending score for it, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(observed)
    session.commit()

    assert observed
    assert observed.movie_id == expected_id
    assert observed.title == expected_title
    assert observed.year == expected_year

