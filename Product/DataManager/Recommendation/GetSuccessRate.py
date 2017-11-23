from Product.Database.DatabaseManager.Retrieve.RetrieveSuccessRate import RetrieveSuccessRate


class GetSuccessRate:
    """
    Author: John Andree Lidquist / Alexander Dahl
    Date: 2017-11-20
    Last update: 2017-11-20
    Purpose: Retrieve the number of recommended movies that have been watched, and the number that
    have not been watched
    """

    @staticmethod
    def get_simple_success_rate():
        """
        Author: John Andree Lidquist, David Cerny
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve the number of recommended movies that have been watched, and the number that
        have not been watched
        """
        # TODO docstring needs updating.
        success_rate_dict = []
        all_rates = RetrieveSuccessRate().get_simple_success_rate()
        for rate in all_rates:
            success_rate_dict.append({'watched': rate.watched, 'not_watched': rate.not_watched,
                                      'timestamp': rate.timestamp})
        return success_rate_dict

    @staticmethod
    def get_average_user_success_rate():
        """
        Author: John Andree Lidquist, David Cerny
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve the average number of recommended movies that have been watched, and the number that
        have not been watched for each user
        """
        # TODO update docstring
        result = []
        all_rates = RetrieveSuccessRate().get_average_user_success_rate()
        for rate in all_rates:
            result.append({'average_user_success_rate': rate.average_user_success_rate,
                           'timestamp': rate.timestamp})
        return result

