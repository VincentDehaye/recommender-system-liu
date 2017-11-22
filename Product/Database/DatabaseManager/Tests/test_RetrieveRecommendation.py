from Product.Database.DatabaseManager.Retrieve.RetrieveRecommendation import RetrieveRecommendation
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import Movie
from Product.Database.DBConn import User


def test_retrieve_watched_and_not_watched():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-21
    Last Updated: 2017-11-22
    Purpose: Assert that the number of watched and the number of not watched are returned
    """

    # PRE-CONDITIONS
    user_id = -1
    movie_id = -1

    # We create a session and add a dummy movie, a dummy user and a dummy recommendation for that user and movie
    # We need to commit twice because of foreign key constraints
    session = create_session()
    dummy_movie = Movie(id=movie_id, title="dummy", year=1111)
    dummy_user = User(id=user_id, age=10, gender='Male', occupation='Student')
    session.add(dummy_movie)
    session.add(dummy_user)
    session.commit()
    dummy_recommendation = Recommendation(user_id=user_id, movie_id=movie_id, watched=True)
    session.add(dummy_recommendation)
    session.commit()

    # EXPECTED OUTPUT
    # The expected outcome is a number bigger than 0 (can't give exact number since we don't know how many
    # recommendations is already in the database)

    # OBSERVED OUTPUT
    # We call the method to be tested to get all the ratings
    observed_watched = RetrieveRecommendation().retrieve_watched_and_not_watched()

    # After adding the dummy movie, the dummy user and the dummy recommendation, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(dummy_recommendation)
    session.commit()
    session.delete(dummy_user)
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed_watched
    assert observed_watched >= 0
    assert observed_watched <= 1


def test_retrieve_average_user_experience():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-22
    Last Updated: 2017-11-22
    Purpose: Assert that the average user experience is returned
    """

    # PRE-CONDITIONS
    user_id = -1
    movie_id = -1

    # We create a session and add a dummy movie, a dummy user and a dummy recommendation for that user and movie
    # We need to commit twice because of foreign key constraints
    session = create_session()
    dummy_movie = Movie(id=movie_id, title="dummy", year=1111)
    dummy_user = User(id=user_id, age=10, gender='Male', occupation='Student')
    session.add(dummy_movie)
    session.add(dummy_user)
    session.commit()
    dummy_recommendation = Recommendation(user_id=user_id, movie_id=movie_id, watched=True)
    session.add(dummy_recommendation)
    session.commit()

    # EXPECTED OUTPUT
    # The expected outcome is a number bigger than 0 (can't give exact number since we don't know how many
    # recommendations is already in the database)

    # OBSERVED OUTPUT
    # We call the method to be tested to get all the ratings
    observed_average = RetrieveRecommendation().retrieve_average_user_experience()

    # After adding the dummy movie, the dummy user and the dummy recommendation, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(dummy_recommendation)
    session.commit()
    session.delete(dummy_user)
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed_average
    assert observed_average >= 0
    assert observed_average <= 1
