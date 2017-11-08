from Product.Database.DatabaseManager import DatabaseManager


class DataManager():
    def __init__(self):
        print("Do Something")

    def getTrending(self, numOfTitles):
        return DatabaseManager.getTrending(numOfTitles)

    def getTrendingYoutube(self, numOfTitles):
        return DatabaseManager.getTrendingYoutube(numOfTitles)

    def getTrendingTwitter(self, numOfTitles):
        return DatabaseManager.getTrendingTwitter()

