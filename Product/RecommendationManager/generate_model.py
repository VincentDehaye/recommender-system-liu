"""
This module has the following functions:
Training and saving a lightFM model
Loading a lightFM model
Testing the precision@k for a lightFM model
"""
import pickle
from lightfm import LightFM
from lightfm.evaluation import precision_at_k, auc_score
from Product.RecommendationManager import gets_from_database as get_matrices
import numpy as np


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
    train_matrix = get_matrices.get_train_matrix()

    # Instantiate and train the model
    # epochs is number of iterations of training done on the training matrix.
    model = LightFM(loss='warp')
    model.fit(train_matrix, epochs=20, num_threads=2)
    pickle.dump(model, open(filename, 'wb'))


def load_model(filename):
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-11-03
    Purpose: loads trained model
    :param filename:
    :return: lightFM model
    """
    try:
        return pickle.load(open(filename, 'rb'))
    except FileNotFoundError:
        print('Wrong file or file path')

def test_precision(model, matrix, k):
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
    return precision_at_k(model, matrix, k=k).mean()


# TODO split this method into a method that evolves the model
# TODO and add the testing methods to the tests folder
def evolve_model():
    """
    Author: Gustaf Norberg
    Date: 2017-11-09
    Last update: 2017-11-10
    Purpose: evolves the model and prints test_precisions after evolution

    """
    model = load_model('new_model.sav')
    # print(get_train_matrix.getMovieList())

    trainmatrix = get_matrices.get_train_matrix()
    testmatrix = get_matrices.get_test_matrix()
    new_user_matrix = get_matrices.get_new_users_matrix()
    # trainmatrix, testmatrix, new_user_matrix = get_train_matrix.get_matricies()

    print("Before")

    model = LightFM(learning_rate=0.05, loss='warp')
    model.fit(trainmatrix, epochs=10)

    train_precision = precision_at_k(model, trainmatrix, k=10).mean()
    test_precision = precision_at_k(model, testmatrix, k=10).mean()

    train_auc = auc_score(model, trainmatrix).mean()
    test_auc = auc_score(model, testmatrix).mean()

    print('Precision: train %.2f, test %.2f.' % (train_precision, test_precision))
    print('AUC: train %.2f, test %.2f.' % (train_auc, test_auc))

    model.fit_partial(new_user_matrix, epochs=10)

    ninetypercent_matrix = trainmatrix + new_user_matrix

    train_precision = precision_at_k(model, ninetypercent_matrix, k=10).mean()
    test_precision = precision_at_k(model, testmatrix, k=10).mean()

    train_auc = auc_score(model, ninetypercent_matrix).mean()
    test_auc = auc_score(model, testmatrix).mean()

    print("After fitpartial")
    print('Precision: train %.2f, test %.2f.' % (train_precision, test_precision))
    print('AUC: train %.2f, test %.2f.' % (train_auc, test_auc))

    print("Train")
    print(np.shape(trainmatrix))
    print(np.shape(testmatrix))
    print(np.shape(new_user_matrix))


#   evolve_model()
