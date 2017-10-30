from Product.TrendManager.TrendScoreToDatabase import TrendingToDB

def test_TrendingToDB():
    '''
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-30
    Purpose: Assert that the database gets filled/updated with trending scores
    '''

    # Just the first structure of the test

    # Pre-conditions
    trend_to_db = TrendingToDB()

    # Expected output
    expected = 0

    # Observed output
    observed = 0

    assert observed == expected
