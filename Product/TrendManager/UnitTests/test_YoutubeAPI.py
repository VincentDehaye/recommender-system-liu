import datetime
import pytz
from tweepy.streaming import json

from ..YoutubeAPI import YoutubeAPI


def test_get_youtube_data():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that the get_youtube_data returns a search response
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    # Observed output
    observed = youtube.get_youtube_data("IT")

    assert observed is not None


def test_get_date():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that the get_date method in YoutubeAPI returns the correct format.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    # Expected output
    expected = ('%Y-%m-%dT%H:%M:%S.%f%z')
    # Observed output
    output = youtube.get_date(30)

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











