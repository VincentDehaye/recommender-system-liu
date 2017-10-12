from ..YoutubeAPI import YoutubeAPI


def test_get_youtube_data_standard_case():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that get_youtube_data returns search results.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = 'Frozen'

    # Expected output
    # > 0

    # Observed output
    observed = youtube.get_youtube_data(keyword)

    assert observed['pageInfo']['totalResults'] > 0


def test_get_youtube_data_bad_input():
    """
    Author: Martin Lundberg
    Date: 2017-10-11
    Purpose: Assert that get_youtube_data doesn't return any results when given gibberish input.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = '!!akjfa asdjk a nganans k a'

    # Expected output
    expected = 0

    # Observed output
    observed = youtube.get_youtube_data(keyword)

    assert observed['pageInfo']['totalResults'] == expected


def test_get_date():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that the get_date method in YoutubeAPI returns the correct format.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    days = 30

    # Expected output
    expected = '%Y-%m-%dT%H:%M:%S.%f%z'

    # Observed output
    output = youtube.get_date(days)

    assert output is output.format(expected)


def test_get_video_id():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that get_video_id method in YoutubeAPI returns id´s.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    # Observed output
    output1 = youtube.get_video_id("IT")
    # Observed output
    output2 = youtube.get_video_id("laskdaslkjdaslkjdaslkdjaslkjdaslkjasdkljadslkdj alkdjaslkjddslak alksdjj")

    assert output1 is not None

    assert output2 is ""

def test_get_youtube_count():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that get_youtube_count returns a integer with a value.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    # Observed output
    output1 = youtube.get_youtube_count("IT")

    assert output1 is int(output1) and output1 > 0

def test_get_youtube_count_standard_case():
    """
    Author: Linn Pettersson
    Date: 2017-10-12
    Purpose: Assert that get_youtube_count returns an integer with a total trending score
    given a valid keyword
    """
    # Pre-conditions
    youtube = YoutubeAPI()

    # Expected output
    # >= 0

    # Observed output
    observed = youtube.get_youtube_count("It")

    print(observed)
    assert observed >= 0

def test_get_youtube_count_unexisting_keyword():
    """
    Author: Linn Pettersson
    Date: 2017-10-12
    Purpose: Assert that get_youtube_count returns 0 as total trending score
    for movie title that does not exist
    """
    # Pre-conditions
    youtube = YoutubeAPI()

    # Expected output
    expected = 0

    # Observed output
    observed = youtube.get_youtube_count("hdjsksjfkald")

    print(observed)
    assert observed == 0






