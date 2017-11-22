from Product.Database.DatabaseManager.Retrieve.RetrieveRecommendation import RetrieveRecommendation


class GetRecommendation:
    """
    Author: John Andree Lidquist / Alexander Dahl
    Date: 2017-11-20
    Last update: 2017-11-20
    Purpose: Retrieve the number of recommended movies that have been watched, and the number that
    have not been watched
    """

    @staticmethod
    def retrieve_watched_and_not_watched():
        """
        Author: John Andree Lidquist / Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve the number of recommended movies that have been watched, and the number that
        have not been watched
        """
        return RetrieveRecommendation().retrieve_watched_ratio()

    @staticmethod
    def retrieve_average_user_experience():
        """
        Author: John Andree Lidquist / Alexander Dahl
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve the average number of recommended movies that have been watched, and the number that
        have not been watched for each user
        """
        return RetrieveRecommendation().retrieve_average_user_experience()
