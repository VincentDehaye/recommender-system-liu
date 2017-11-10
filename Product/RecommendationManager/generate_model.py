"""
This module has the following functions:
Training and saving a lightFM model
Loading a lightFM model
Testing the precision@k for a lightFM model
"""
import pickle
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from Product.RecommendationManager import gets_from_database as get_train_matrix


def train_model(filename):
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-10-08
    Purpose: Trains and saves a lightFM model
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



def load_model(filename):
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-10-08
    Purpose: loads trained model
    :param filename:
    :return: lightFM model
    """
    return pickle.load(open(filename, 'rb'))


def test_precision(model, train_matrix, k):
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-10-08
    Purpose: returns a test precision for the model at k value.

    :param model: lightFM model
    :param train_matrix: Matrix from database
    :param k: precision@k
    :return: float
    """
    return precision_at_k(model, train_matrix, k).mean()
