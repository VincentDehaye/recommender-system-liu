import numpy as np

from lightfm import LightFM
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

# Filling the lists with data from the database
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix.
# TODO Should only collect ratings over 3, otherwise even a one is treated as a positive rating. We should load
# TODO the combination of every movie and user into the lists. If there is no rating by the user,
# TODO this should be represented as a zero.
for counter,row in enumerate(session.query(Rating.user_id,Rating.movie_id,Rating.rating)):

    if counter % 5 == 0:
        TestUserList.append(row[0])
        TestMovieList.append(row[1])
        TestRatingList.append(row[2])
    else:
        UserList.append(row[0])
        MovieList.append(row[1])
        RatingList.append(row[2])

# Creates two sparse matrixes, to make the data compatable with LightFM
TrainMatrix = coo_matrix((RatingList,(UserList,MovieList)))
TestMatrix = coo_matrix((TestRatingList,(TestUserList,TestMovieList)))

# Instantiate and train the model, epochs is number of iterations of training done on the trainmatrix.
model = LightFM(loss='warp')
model.fit(TrainMatrix, epochs=20, num_threads=2)

# Evaluate the trained model by comparing it with the original data
# It evaluates the precision for the top k movies from the algorithm
# Could be a good idea to move this to another file since it takes a lot of time to run
test_precision = precision_at_k(model, TrainMatrix, k=5).mean()

# this prints the test precision
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

# Calls upon the samle_recommendation to create a recommendation list for user 56.
sample_recommendation(model, TrainMatrix, range(56, 57))