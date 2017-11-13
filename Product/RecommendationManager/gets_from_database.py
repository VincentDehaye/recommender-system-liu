"""
Handles the connections to the database
get_trending_scores puts the trending_scores from the
database in a dictionary

get_train_matrix fetches data from the database and puts
it into a training matrix for the lightFM model

get_test_matrix fetches data from the database and puts
it into a test matrix from the lightFM model

get_movie_title returns the movie title for one movie id

"""
from scipy.sparse import coo_matrix
import numpy as np #TODO, remove this. Not needed but used to test shape atm
import random


from Product.Database.DBConn import session, Rating, TrendingScore, Movie
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie

### old TODOS, ok to delete?
# Filling the lists with data from the database
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix.
# TODO Should only collect ratings over 3, otherwise even a one is treated as a positive rating. We should load
# TODO the combination of every movie and user into the lists. If there is no rating by the user,
# TODO this should be represented as a zero.
# TODO should the creation of the testing matrix be here too?


def get_trending_scores():
    """
    Author: Alexander Dahl
    Date: 2017-11-01
    Last update: 2017-11-01
    Purpose:
    fills a dictionary with trending scores. Movie id is the key and normalized score is the value.
    :return: trending_scores in the form a of a dictionary
    
    ### method only used by files in archive!
    """
    trending_scores = {}

    for row in session.query(TrendingScore).all():
        trending_scores[row.movie_id] = row.normalized_score

    return trending_scores


def get_matrices():
    """
    Author: Gustaf Norberg
    Date: 2017-11-09
    Last update: 2017-11-09
    Purpose:
    Returns train matrix, test matrix and new users matrix where all are randomly split into parts of 80 %, 10 % and
    10 % respectively

    :return: training matrix, testing matrix and new users matrix in the form of numpy matrices
    """

    train_user_list = []
    train_movie_list = []
    train_rating_list = []

    test_user_list = []
    test_movie_list = []
    test_rating_list = []

    new_users_user_list = []
    new_users_movie_list = []
    new_users_rating_list = []
    random_division = 0.0
    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        random_division = random.uniform(0, 1)
        if random_division < 0.1:
            new_users_user_list.append(row[0])
            new_users_movie_list.append(row[1])
            new_users_rating_list.append(row[2])
        elif random_division > 0.9:
            test_user_list.append(row[0])
            test_movie_list.append(row[1])
            test_rating_list.append(row[2])
        else:
            train_user_list.append(row[0])
            train_movie_list.append(row[1])
            train_rating_list.append(row[2])

    train_matrix = coo_matrix((train_rating_list, (train_user_list, train_movie_list)))
    test_matrix = coo_matrix((test_rating_list, (test_user_list, test_movie_list)))
    new_users_matrix = coo_matrix((new_users_rating_list, (new_users_user_list, new_users_movie_list)))
    return (train_matrix, test_matrix, new_users_matrix)


def get_train_matrix():
    """
    Author: Marten Bolin / John Lidquist
    Date: 2017-10-02
    Last update: 2017-11-06 by Gustaf Norberg
    Purpose:
    returns the train matrix. The matrix is 80% (4/5) of the user ratings at the moment
    OBS! coo_matrix is a sparse matrix and will (most likely) have the same dimensions for train_matrix, test_matrix and
    new_user_matrix

    :return: training matrix in the form of a numpy matrix
    """

    user_list = []
    movie_list = []
    rating_list = []
    np.shape(Rating)
    # Puts everything but every 5th row (1, 2, 3, 4, 6, 7, 8, 9, 11...) in train_matrix
    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 5 != 0:
            user_list.append(row[0])
            movie_list.append(row[1])
            rating_list.append(row[2])

    train_matrix = coo_matrix((rating_list, (user_list, movie_list)))
    return train_matrix


def get_test_matrix():
    """
    Author: Gustaf Norberg / Alexander Dahl
    Date: 2017-11-06
    Last update: 2017-11-06
    Purpose:
    returns the test matrix. The matrix is 10% of the user ratings at the moment

    :return: test matrix in the form of a numpy matrix
    """
    test_user_list = []
    test_movie_list = []
    test_rating_list = []

    # Puts every 10th row (5, 15, 25...) in test_matrix
    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 5 == 0 and counter % 2 == 1:
            test_user_list.append(row[0])
            test_movie_list.append(row[1])
            test_rating_list.append(row[2])

    test_matrix = coo_matrix((test_rating_list, (test_user_list, test_movie_list)))
    return test_matrix


def get_new_users_matrix():
    """
    Author: Gustaf Norberg
    Date: 2017-11-06
    Last update: 2017-11-06
    Purpose: returns the new users matrix. The matrix is 10 % of the user ratings.
    Is used for showing that model is evolving

    :return: new users matrix in the form of a numpy matrix
    """
    user_list = []
    movie_list = []
    rating_list = []
    #Puts every 10th row (10, 20, 30...) in new_users_matrix
    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 10 == 0:
            user_list.append(row[0])
            movie_list.append(row[1])
            rating_list.append(row[2])

    new_users_matrix = coo_matrix((rating_list, (user_list, movie_list)))

    return new_users_matrix


def get_movie_title(movie_id):
    """
    Author: Alexander Dahl
    Date: 2017-11-01
    Last update: 2017-11-13
    Purpose: returns the movie title from a movie id input

    :param movie_id:
    :return: movie name as string
    """
    return RetrieveMovie().retrieve_movie(movie_id).title

#get_matrices()
