import numpy as np

from lightfm import LightFM
#from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

from Product.Database.DBConn import session, User, Movie, Rating
from scipy.sparse import coo_matrix


#This file in contrast to lightfm_example will try to use our own database to create a recommendation list.



# Load the MovieLens 100k dataset.
#data = fetch_movielens()

#As we can see when printing, data['train'] is a "sparse matrix"
#print('this is the train data in the dataset. (userid, movieid) rating')
#print(data['train'])
#As we can see when printing, data['test'] is a "sparse matrix"
#print('this is the test data in the dataset')
#print(data['test'])
#As we can see when printing, data['item_labels'] is an array?,
#print('this is the movies in the dataset')
#print(data['item_labels'])

print('-------------------------------')
#print(data['item_features'])

#TODO Save this information in the same format as data['train'] and data['test'], e.g. sparse matrix
Ratings = session.query(Rating).all()
UserList = []
MovieList = []
RatingList = []
TestUserList = []
TestMovieList = []
TestRatingList = []

for counter,row in enumerate(session.query(Rating.user_id,Rating.movie_id,Rating.rating)):

    if counter % 5 == 0:
        TestUserList.append(row[0])
        TestMovieList.append(row[1])
        TestRatingList.append(row[2])
    else:
        UserList.append(row[0])
        MovieList.append(row[1])
        RatingList.append(row[2])

TrainMatrix = coo_matrix((RatingList,(UserList,MovieList)))
TestMatrix = coo_matrix((TestRatingList,(TestUserList,TestMovieList)))
print('                 this is OUR train data')
print(TrainMatrix)
print('                 this is OUR test data')
print(TestMatrix)


# Saves the data in the same format as the data[labels] list in lightfm example
movieList=[]
Movies = session.query(Movie).all()
for row in session.query(Movie.title):
    movieList.append(row[0])
newMovieList=np.transpose(movieList)

print('                 this is OUR labels')
print(newMovieList)

# Instantiate and train the model, change epochs to improve precision.
model = LightFM(loss='warp')
model.fit(TrainMatrix, epochs=20, num_threads=2)

# Evaluate the trained model by comparing it with the original data
# It evaluates the precision for the top k=10 movies from the algorithm
test_precision = precision_at_k(model, TrainMatrix, k=10).mean()
# this prints the test precision
# the precision is in percentage.
print('precision at train: %s' % test_precision)


# Sends in our testmatrix and the user_ids for the users to present recommendations
def sample_recommendation(model, trainmatrix, newMovieList, user_ids):
    n_users, n_items = trainmatrix.shape
    print("Our testmatrix shape: ")
    print(trainmatrix.shape)
    print("Our newMovieList shape: ")
    print(newMovieList.shape)
    for user_id in user_ids:
        # known_positives = newMovieList[testmatrix.tocsr()[user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        # print("This is the ng.arg")
        # print(np.argsort(-scores))
        top_items = np.argsort(-scores)
        print("This is the recommended movie_ids for user:" + str(user_id))
        for movie_id in top_items[:100]:
            print(movie_id)

        # top_items = newMovieList[np.argsort(-scores)]

        # print("User %s" % user_id)
        # print("     Known positives:")

        # for x in known_positives[:3]:
            # print("        %s" % x)

        # print("     Recommended:")

        # for x in top_items[:10]:
        #    print("        %s" % x)


# this method prints the recommended and known positives for the first three users
# known positives are movies that users have watched and rated highly
# recommended are the movies that lightfm recommends.
# observe that the user id is +1 and movie_id +1 in the dataset compared to the method output
# That is because arrays start at 0 in python and.
# TODO The output from this function should be a list of length 10 with ID:s that corresponds to the predicted movies.
sample_recommendation(model, TrainMatrix, newMovieList, range(56, 57))