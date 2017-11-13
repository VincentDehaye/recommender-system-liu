from Product.DataManager.TopTrending.RetrieveTopTrendingYoutube import RetrieveTopTrendingYoutube


def test_get_top_trending():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-13
    Purpose: Assert that movies (titles + youtube_scores) are returned and that it is the correct amount
    """

    # Pre-conditions
    trender = RetrieveTopTrendingYoutube()

    # Expected output
    num_of_movies = 5

    # Observed output
    observed = len(trender.get_top_trending(num_of_movies).dict())

    assert observed == num_of_movies
