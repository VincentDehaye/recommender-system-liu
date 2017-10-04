import numpy as np

from lightfm import LightFM
#from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

from Product.Database.DBConn import session, User, Movie, Rating
from scipy.sparse import coo_matrix


# This file in contrast to lightfm_example will try to use our own database to create a recommendation list.
# Sets up all the lists that will be needed.
Ratings = session.query(Rating).all()
UserList = []
MovieList = []
RatingList = []
TestUserList = []
TestMovieList = []
TestRatingList = []

# TODO Should only collect ratings over 3 or 5?
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix. We should load
# the combination of every movie and user. If there is no rating by the user, this should be represented as a zero.
for counter,row in enumerate(session.query(Rating.user_id,Rating.movie_id,Rating.rating)):

    if counter % 5 == 0:
        TestUserList.append(row[0])
        TestMovieList.append(row[1])
        TestRatingList.append(row[2])
    else:
        UserList.append(row[0])
        MovieList.append(row[1])
        RatingList.append(row[2])

# Creates two sparse matrixes to make the data compatable with LightFM
TrainMatrix = coo_matrix((RatingList,(UserList,MovieList)))
TestMatrix = coo_matrix((TestRatingList,(TestUserList,TestMovieList)))

# Instantiate and train the model, change epochs to improve precision.
model = LightFM(loss='warp')
model.fit(TrainMatrix, epochs=20, num_threads=2)

# Evaluate the trained model by comparing it with the original data
# It evaluates the precision for the top k=10 movies from the algorithm
# Could be a good idea to move this to another file since it takes some time to run
test_precision = precision_at_k(model, TrainMatrix, k=5).mean()

# this prints the test precision
# the precision is in percentage.
print('precision at train: %s' % test_precision)


# Sends in our testmatrix and the user_ids for the users to present recommendations
def sample_recommendation(model, trainmatrix, user_ids):
    n_users, n_items = trainmatrix.shape
    for user_id in user_ids:

        scores = model.predict(user_id, np.arange(n_items))
        top_items = np.argsort(-scores)
        print("This is the recommended movie_ids for user:" + str(user_id))
        for movie_id in top_items[:10]:
            print(movie_id)


# this method prints the recommended and known positives for the users in the defined range
# known positives are movies that users have watched and rated highly
# recommended are the movies that lightfm recommends.
# observe that the user id is +1 and movie_id +1 in the dataset compared to the method output
# That is because arrays start at 0 in python and.
# TODO The output from this function should be a list of length 10 with ID:s that corresponds to the predicted movies.
sample_recommendation(model, TrainMatrix, newMovieList, range(56, 57))