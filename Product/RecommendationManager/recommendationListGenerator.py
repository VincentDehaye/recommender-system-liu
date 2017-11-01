import numpy as np

from lightfm import LightFM
from lightfm.evaluation import precision_at_k

from Product.Database.DBConn import session, User, Movie, Rating, TrendingScore
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

trending_scores={}
for row in enumerate(session.query(TrendingScore.movie_id, TrendingScore.normalized_score)):
    # row[1][0] is movie_id
    # row[1][1] is normalized trending score
    print(row[1][0])
    trending_scores[row[1][0]]=row[1][1]

print(trending_scores)
# Creates two sparse matrixes, to make the data compatable with LightFM
TrainMatrix = coo_matrix((RatingList,(UserList,MovieList)))
TestMatrix = coo_matrix((TestRatingList,(TestUserList,TestMovieList)))

# Instantiate and train the model, epochs is number of iterations of training done on the trainmatrix.
# TODO save model to file after having been generated.
model = LightFM(loss='warp')
model.fit(TrainMatrix, epochs=20, num_threads=2)

# Evaluate the trained model by comparing it with the original data
# It evaluates the precision for the top k movies from the algorithm
# Could be a good idea to move this to another file since it takes a lot of time to run
# TODO move this to another file.
#test_precision = precision_at_k(model, TrainMatrix, k=5).mean()

# this prints the test precision
#print('precision at train: %s' % test_precision)
def normalize_user_scores(scores):
    min_score = np.amin(scores)
    max_score = np.amax(scores)

    for i in range(0, len(scores)):
        scores[i] = (scores[i] - min_score)/(max_score-min_score)

    return scores

# Sends in our testmatrix and the user_ids for the users to present recommendations
def sample_recommendation(model, trainmatrix, user_ids):
    n_users, n_items = trainmatrix.shape
    for user_id in user_ids:
        movie_scores={}
        scores = model.predict(user_id, np.arange(n_items))
        top_items = np.argsort(-scores)
        #movie_scores ={np.argsort(-scores) : scores}
        #print(enumerate(np.argsort(-scores)))
        #movie_scores ={enumerate(np.argsort(-scores)) : scores}
#        movie_scores=[np.argsort(-scores)[:10].tolist(), np.sort(-scores[:10]).tolist()]
      #  movie_scores={np.argsort(-scores).tolist() : scores.tolist()}
        #movie_scores[np.argsort(-scores).tolist()] = scores.tolist()
        #print('argsort')
        #print(np.argsort(-scores).tolist())
        #print('scores \n')
        #print(scores.tolist())
 #       for score in scores:
#            print(score)
        normalized_scores=normalize_user_scores(scores)
        #print(movie_scores)
        print("This is the recommended movie_ids for user:" + str(user_id))
        #print(np.argsort(scores))

        for movie_id in np.argsort(-scores):
           # print(movie_id)
            movie_scores[movie_id]=scores[movie_id]

       # print(movie_scores)
        #print(movie_scores[0])
        trending_test={1: 0.5}
        w = 1.5

        print(movie_scores[1]+w*trending_test[1])
        print(movie_scores[1]+w*trending_scores[1])
        print(np.argsort(-scores)==np.argsort(-normalized_scores))
        print(np.argsort(-scores))
        print(np.argsort(-normalized_scores))

        trending_and_user_pref_scores={}
        for id in trending_scores:
            print(id)
            print(trending_scores[id])
            print(movie_scores[id])
            trending_and_user_pref_scores[id] = movie_scores[id]+w*trending_scores[id]
            print(trending_and_user_pref_scores[id])

            #print(scores[0])
        #print(np.arange(n_items))


# Calls upon the samle_recommendation to create a recommendation list for user 56.
sample_recommendation(model, TrainMatrix, range(56, 57))
