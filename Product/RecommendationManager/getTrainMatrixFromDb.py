
from scipy.sparse import coo_matrix

from Product.Database.DBConn import session, User, Movie, Rating, TrendingScore

Ratings = session.query(Rating).all()
UserList = []
MovieList = []
RatingList = []
TestUserList = []
TestMovieList = []
TestRatingList = []
# This file in contrast to lightfm_example will try to use our own database to create a recommendation list.

# Filling the lists with data from the database
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix.
# TODO Should only collect ratings over 3, otherwise even a one is treated as a positive rating. We should load
# TODO the combination of every movie and user into the lists. If there is no rating by the user,
# TODO this should be represented as a zero.
# TODO should the creation of the testing matrix be here too?
for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):

    if counter % 5 == 0:
        TestUserList.append(row[0])
        TestMovieList.append(row[1])
        TestRatingList.append(row[2])
    else:
        UserList.append(row[0])
        MovieList.append(row[1])
        RatingList.append(row[2])

# trending_scores={}
# for row in enumerate(session.query(TrendingScore.movie_id, TrendingScore.normalized_score)):
#     # row[1][0] is movie_id
#     # row[1][1] is normalized trending score
#     print(row[1][0])
#     trending_scores[row[1][0]]=row[1][1]

# print(trending_scores)
# Creates two sparse matrixes, to make the data compatable with LightFM
TrainMatrix = coo_matrix((RatingList, (UserList, MovieList)))
TestMatrix = coo_matrix((TestRatingList,(TestUserList,TestMovieList)))



def getTrainMatrix():

    return TrainMatrix


def getMovieList():

    return MovieList

# TODO also create a function to get the test matrix
