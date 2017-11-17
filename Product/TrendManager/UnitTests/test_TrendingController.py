from ..TrendingController import TrendingController

def test_get_trending_content_standard_case():
    """
    Author: Albin Bergvall, Karl Lundvall
    Date: 2017-11-16
    Purpose: Assert that get_trending_content returns a scored movie
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'Frozen'

    # Expected output
    # scoredmovie != null
    # scoredmovie.score >= 0

    # Observed output
    observed = trendingcontroller.get_trending_content(keyword)

    assert observed[0] >= 0
    assert observed[1] >= 0
    assert observed[2] >= 0


def test_get_trending_content_bad_input():
    """
    Author: Albin Bergvall, Karl Lundvall
    Date: 2017-11-16
    Purpose: Assert that get_trending_content returns a scored movie with zero score when given bad input
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'garga 11 jnargao'

    # Observed output
    observed = trendingcontroller.get_trending_content(keyword)

    assert observed[0] is 0

