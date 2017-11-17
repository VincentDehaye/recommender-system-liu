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


# TODO - Fix this script to show improvement graph
def evolve_model_graph(train_matrix, test_matrix):
    """
    Author: Gustaf Norberg
    Date: 2017-11-15
    Last update: 2017-11-15
    Purpose: should generate a graph to show improvement over time, not finished.
    """
    alpha = 1e-3
    epochs = 70

    adagrad_model = LightFM(no_components=30,
                            loss='warp',
                            learning_schedule='adagrad',
                            user_alpha=alpha,
                            item_alpha=alpha)
    adadelta_model = LightFM(no_components=30,
                             loss='warp',
                             learning_schedule='adadelta',
                             user_alpha=alpha,
                             item_alpha=alpha)

    adagrad_auc = []

    for epoch in range(epochs):
        adagrad_model.fit_partial(train_matrix, epochs=1)
        adagrad_auc.append(auc_score(adagrad_model, test_matrix).mean())

    adadelta_auc = []

    for epoch in range(epochs):
        adadelta_model.fit_partial(train_matrix, epochs=1)
        adadelta_auc.append(auc_score(adadelta_model, test_matrix).mean())


def evolve_model(filename, model, new_users_matrix):
    """
    Author: Gustaf Norberg
    Date: 2017-11-09
    Last update: 2017-11-13
    Purpose: evolves the model using fit_partial - an add-on for the already fitted model

    :param model: lightFM model
    :param new_users_matrix: Matrix from database
    :param filename:
    :type filename: string
    """
    model.fit_partial(new_users_matrix, epochs=10)
    pickle.dump(model, open(filename, 'wb'))

    # TODO what is the purpose of this commented code?
    # print("Before")
    #
    # model = LightFM(learning_rate=0.05, loss='warp')
    # model.fit(trainmatrix, epochs=10)
    #
    # train_precision = precision_at_k(model, trainmatrix, k=10).mean()
    # test_precision = precision_at_k(model, testmatrix, k=10).mean()
    #
    # train_auc = auc_score(model, trainmatrix).mean()
    # test_auc = auc_score(model, testmatrix).mean()
    #
    # print('Precision: train %.2f, test %.2f.' % (train_precision, test_precision))
    # print('AUC: train %.2f, test %.2f.' % (train_auc, test_auc))
    #
    # model.fit_partial(new_user_matrix, epochs=10)
    #
    # ninetypercent_matrix = trainmatrix + new_user_matrix
    #
    # train_precision = precision_at_k(model, ninetypercent_matrix, k=10).mean()
    # test_precision = precision_at_k(model, testmatrix, k=10).mean()
    #
    # train_auc = auc_score(model, ninetypercent_matrix).mean()
    # test_auc = auc_score(model, testmatrix).mean()
    #
    # print("After fitpartial")
    # print('Precision: train %.2f, test %.2f.' % (train_precision, test_precision))
    # print('AUC: train %.2f, test %.2f.' % (train_auc, test_auc))
    #
    # print("Train")
    # print(np.shape(trainmatrix))
    # print(np.shape(testmatrix))
    # print(np.shape(new_user_matrix))
    #


def show_evolvement():
    """
    Author: Gustaf Norberg
    Date: 2017-11-09
    Last update: 2017-11-13
    Purpose: Shows, in print, that model evolves after running evolve_model
    """
    print("Generate new model")
    train_model('test_new_model.sav')
    print("Load the new model")
    model = load_model('test_new_model.sav')
    print("Import train matrix (80 % of total user data)")
    print("Import new user data matrix - emulated new user data (10 % of total user data)")
    print(" ")
    train_matrix = get_matrices.get_train_matrix()
    new_users_matrix = get_matrices.get_new_users_matrix()
    k = 10

    print("Check precision @ k for the model based on the train matrix (80 %)")
    precision_before = test_precision(model, train_matrix, k)
    print("Precision before re-training of model")
    print(precision_before)
    print(" ")
    print("Re-train model with the extra users (80 + 10 %)")
    evolve_model('test_new_model.sav', model, new_users_matrix)
    print("Check precision @ k for the model based on the train matrix & new users (90 %)")
    precision_after = test_precision(model, train_matrix + new_users_matrix, k)
    print("Precision after re-training of model")
    print(precision_after)

# show_evolvement()
