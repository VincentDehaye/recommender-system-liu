from ..TrendingController import TrendingController

def test_get_trending_content_standard_case():
    """
    Author: Albin Bergvall
    Date: 2017-10-12
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

    assert observed is not None
    assert observed >= 0


def test_get_trending_content_bad_input():
    """
    Author: Albin Bergvall
    Date: 2017-10-12
    Purpose: Assert that get_trending_content returns a scored movie with zero score when given bad input
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'garga 11 jnargao'

    # Expected output
    # scoredmovie != null
    # scoredmovie.score = 0

    # Observed output
    observed = trendingcontroller.get_trending_content(keyword)

    assert observed is not None
    assert observed == 0


def test_total_score_calc_standard_case():
    """
    Author: Albin Bergvall
    Date: 2017-10-12
    Purpose: Assert that total_score_calc returns a score >= 0
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'frozen'

    # Expected output
    # >= 0

    # Observed output
    observed = trendingcontroller.total_score_calc(keyword)

    assert observed >= 0

def test_total_score_calc_bad_input():
    """
    Author: Albin Bergvall
    Date: 2017-10-12
    Purpose: Assert that total_score_calc returns a zero score with bad input
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'garga 11 jnargao'

    # Expected output
    # = 0

    # Observed output
    observed = trendingcontroller.total_score_calc(keyword)

    assert observed == 0
