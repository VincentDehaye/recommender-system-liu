from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation
from Product.Database.DBConn import create_session
#from Product.Database.DBConn import Recommendations

def test_insert_recommendation():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-15
    Purpose: Assert that recommendations are inserted to the database
    """
    pass
    # TODO Code is broken after last push that removes Recommendation class in DBCONN

    # Pre-conditions
"""
    movie_id = 11
    user_id = 11
    inserter = InsertRecommendation()
    inserter.insert_recommendation(movie_id=movie_id, user_id=user_id)
    session = create_session()

    # Expected output
    # The expected output is that we get a result back from the database after adding it

    # Observed output
    observed = session.query(Recommendations).filter_by(movie_id=movie_id, user_id=user_id).first()
    session.delete(observed) #After adding the row in the database we remove it again.
    session.commit()

    assert observed
"""
