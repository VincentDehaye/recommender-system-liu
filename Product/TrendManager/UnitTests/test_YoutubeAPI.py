from ..YoutubeAPI import youtube_search
from oauth2client.tools import argparser


def test_youtube_search_standard_case(self):
    """
    Author: Martin Lundberg
    Date: 2017-10-03
    Purpose: Assert that we're getting what we want from Youtube
    """

    # Pre-conditions
    argparser.add_argument("--q", help="Search term", default="frozen")
    argparser.add_argument("--type", help="Type", default="video")
    argparser.add_argument("--video-category-id",
                           help="Video Category Id", default=30)
    argparser.add_argument("--max-results", help="Max results", default=10)
    argparser.add_argument("--publishedAfter",
                           help="Date condition", default="")
    arguments = argparser.parse_args()

    # Expected outputs
    # Insert what to check for here

    # Observed outputs
    youtube_search(arguments) # This should return outputs

    # Compare
    self.asssertEqual(True, True)
