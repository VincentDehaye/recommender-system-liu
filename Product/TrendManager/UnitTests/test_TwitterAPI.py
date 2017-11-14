from ..TwitterAPI import TwitterAPI
from ..TwitterAPI import TwitterAPI


def test_get_word_score():
    """
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that it is possible to retrieve a score from the dictionary and that the score is an integer.
    """
    # Pre-conditions
    twitter_api = TwitterAPI()
    dictionary = {'Batman': 0}
    word = 'Batman'

    # Expected output
    expected1 = 0
    expected2 = int(expected1)

    # Observed output
    observed = twitter_api.get_word_score(word, 0, dictionary)
    observed1 = twitter_api.get_word_score(word, 0, dictionary)

    assert observed is expected1
    assert observed1 is expected2

def test_format_word():
    """
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that words are in lowercase and that all non alphabetic or numeric characters gets removed.
    """
    # Pre-conditions
    twitter_api = TwitterAPI()

    # Expected output
    expected = "hej"

    # Observed output
    observed = twitter_api.format_word("H*E'?J")

    assert observed == expected

def test_chi_square():
    """
    Author: Karl Lundvall
    Date: 2017-11-14
    Purpose: Assert that the chi-square method returns a ratio of improvement or the opposite.
    :return:
    """
    # Pre-conditions
    twitter_api = TwitterAPI()
    new_val = 10
    old_val = 20

    # Expected output
    expected = 5.0

    # Observed output
    observed = twitter_api.chi_square(new_val, old_val)

    assert observed == expected

# NO BINARY FILES YET TO BE FOUND, will fail in test without them.
    """"
def test_load_dict():
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that print_dict retrieves a dictionary from the twitter_dataYYYYMMDD.bin.
    # Pre-conditions
    twitterApi = TwitterAPI()

    # Observed output
    observed1 = twitterApi.load_old_dict()

    assert observed1 is not None
    """

    """
def test_get_twitter_score():
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that get_twitter_score retrieves a score.
    # Pre-conditions
    twitter_api = TwitterAPI()

    # Observed output
    observed = twitter_api.get_twitter_score("Batman")

    assert observed is not None
    """

