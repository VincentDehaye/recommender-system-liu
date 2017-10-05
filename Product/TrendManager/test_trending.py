from .YoutubeAPI import *


def test_R11():
    """
    Author: Martin Lundberg
    Date: 2017-10-04
    Purpose: Functional test for requirement R11 for the trending team.
    R11: The module shall retrieve trending content from online sources.

    Tests that we can get data from youtube.
    """

    # Pre-conditions
    # argparser.add_argument("--q", help="Search term", default="")
    # argparser.add_argument("--type", help="Type", default="video")
    # argparser.add_argument("--video-category-id",
    #                        help="Video Category Id", default=category_id)
    # argparser.add_argument("--max-results", help="Max results", default=max_results)
    # argparser.add_argument("--publishedAfter",
    #                        help="Date condition", default="")
    # arguments = argparser.parse_args()

    # This doesn't work for some reason. Problem with parse_args() and pytest...
    arguments = get_arguments(30, 10)

    # Expected outputs
    expected = not None

    # Observed outputs
    output = youtube_search(arguments)  # Call the function that gets data from youtube

    # Compare. Make sure there is data.
    assert output is expected
