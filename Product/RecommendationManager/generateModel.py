from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from Product.RecommendationManager import getTrainMatrixFromDb as get_train_matrix
from scipy.sparse import coo_matrix

import pickle


# this function trains the model with the data from movielens
# def train_model(filename):
#     # TODO Instead of getting the dataset from movielens, we should get it from our own DB.
#     data = fetch_movielens()
#
#     model = LightFM(loss='warp')
#     model.fit(data['train'], epochs=30, num_threads=2)
#
#     # saves the trained model to filename
#     pickle.dump(model, open(filename, 'wb'))




# This file in contrast to lightfm_example will try to use our own database to create a recommendation list.
def train_model(filename):
# Sets up all the lists that will be needed.
    #TestMatrix = coo_matrix((TestRatingList,(TestUserList,TestMovieList)))
    trainmatrix=get_train_matrix.get_train_matrix()
    # Instantiate and train the model, epochs is number of iterations of training done on the trainmatrix.
    # TODO save model to file after having been generated.
    model = LightFM(loss='warp')
    model.fit(trainmatrix, epochs=20, num_threads=2)
    pickle.dump(model, open(filename, 'wb'))


# loads trained model
def load_model(filename):
    return pickle.load(open(filename, 'rb'))


# returns a test precision for the model at k value.
def test_precision(model, trainmatrix, k):
    return precision_at_k(model, trainmatrix, k).mean()
