from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal

def test_RetrieveTopTrendingTotal():

    # Pre-conditions
    trender = RetrieveTopTrendingTotal()
    num_of_movies = 5

    # Expected output
    result = trender.get_top_trending(num_of_movies)

    # Observed output
    observed = result.size

    assert observed == num_of_movies
