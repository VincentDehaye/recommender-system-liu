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
        result = []
        all_rates = RetrieveSuccessRate().get_simple_success_rate()
        for rate in all_rates:
            print("watched: ", rate.watched)
            print("not_watched: ", rate.not_watched)
            #print("timestamp :", rate.timestamp)
            result.append({'watched': rate.watched, 'not_watched': rate.not_watched})#,
                           #'timestamp': rate.timestamp})

        return result

    @staticmethod
    def get_average_user_success_rate():
        """
        Author: John Andree Lidquist, David Cerny
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Retrieve the average number of recommended movies that have been watched, and the number that
        have not been watched for each user
        """
        return RetrieveSuccessRate().get_average_user_success_rate()

print(GetSuccessRate().get_simple_success_rate())