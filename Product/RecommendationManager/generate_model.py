"""
This module has the following functions:
Training and saving a lightFM model
Loading a lightFM model
Testing the precision@k for a lightFM model
"""
import pickle
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from Product.RecommendationManager import getTrainMatrixFromDb as get_train_matrix


def train_model(filename):
    """

    :param filename:
    :type filename: string
    """
    # gets the training matrix from the database
    train_matrix = get_train_matrix.get_train_matrix()

    # Instantiate and train the model
    # epochs is number of iterations of training done on the training matrix.
    model = LightFM(loss='warp')
    model.fit(train_matrix, epochs=20, num_threads=2)
    pickle.dump(model, open(filename, 'wb'))


# loads trained model
def load_model(filename):
    """

    :param filename:
    :return: lightFM model
    """
    return pickle.load(open(filename, 'rb'))


# returns a test precision for the model at k value.
def test_precision(model, train_matrix, k):
    """

    :param model: lightFM model
    :param train_matrix: Matrix from database
    :param k: precision@k
    :return:
    """
    return precision_at_k(model, train_matrix, k).mean()
