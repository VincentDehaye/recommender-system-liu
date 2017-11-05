
from scipy.sparse import coo_matrix

from Product.Database.DBConn import session, Rating


# This file in contrast to lightfm_example will try to use our own database to create a recommendation list.

# Filling the lists with data from the database
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix.
# TODO Should only collect ratings over 3, otherwise even a one is treated as a positive rating. We should load
# TODO the combination of every movie and user into the lists. If there is no rating by the user,
# TODO this should be represented as a zero.
# TODO should the creation of the testing matrix be here too?


# trending_scores={}
# for row in enumerate(session.query(TrendingScore.movie_id, TrendingScore.normalized_score)):
#     # row[1][0] is movie_id
#     # row[1][1] is normalized trending score
#     print(row[1][0])
#     trending_scores[row[1][0]]=row[1][1]

# print(trending_scores)
# Creates two sparse matrixes, to make the data compatable with LightFM



# returns the train matrix. The matrix is 80% (4/5) of the user ratings at the moment

def get_train_matrix():
    user_list = []
    movie_list = []
    rating_list = []
    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 5 != 0:
            user_list.append(row[0])
            movie_list.append(row[1])
            rating_list.append(row[2])

    train_matrix = coo_matrix((rating_list, (user_list, movie_list)))

    return train_matrix

# returns the test matrix. The matrix is 20% (1/5) of the user ratings at the moment


def get_test_matrix():
    test_user_list = []
    test_movie_list = []
    test_rating_list = []

    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 5 == 0:
            test_user_list.append(row[0])
            test_movie_list.append(row[1])
            test_rating_list.append(row[2])

    test_matrix = coo_matrix((test_rating_list, (test_user_list, test_movie_list)))

    return test_matrix
