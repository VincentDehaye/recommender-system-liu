from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal


def test_get_top_trending():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-13
    Purpose: Assert that movies (titles + total_scores) are returned and that it is the correct amount
    """

    # Pre-conditions
    trender = RetrieveTopTrendingTotal()

    # Expected output
    num_of_movies = 5

    # Observed output
    observed = len(trender.get_top_trending(num_of_movies).dict())

    assert observed == num_of_movies