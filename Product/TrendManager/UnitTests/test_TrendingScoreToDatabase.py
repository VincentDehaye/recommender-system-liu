import time

from Product.Database.DbFillMovieLens.DBConn import TrendingScore
from Product.Database.DbFillMovieLens.DBConn import session
from Product.TrendManager.TrendScoreToDatabase import TrendingToDB


def test_TrendingToDB():
    '''
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-30
    Purpose: Assert that the database gets filled/updated with trending scores.
    '''

    # The test will first start to run the class TrendingToDB and then wait (sleep) for 3 seconds before moving on
    # to make sure that there has been a value stored for the trending score "total_score".

    # Pre-conditions
    trend_to_db = TrendingToDB(continuous=False, background=True)
    time.sleep(3)

    # Expected output 1
    expected_high = 99999
    expected_low = 0

    # Observed output 1
    result = session.query(TrendingScore).filter_by(movie_id=1).first()
    observed = result.total_score

    assert expected_low <= observed <= expected_high
