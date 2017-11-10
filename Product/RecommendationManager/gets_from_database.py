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

from Product.Database.DBConn import session, Rating, TrendingScore, Movie

### old TODOS, ok to delete?
# Filling the lists with data from the database
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix.
# TODO Should only collect ratings over 3, otherwise even a one is treated as a positive rating. We should load
# TODO the combination of every movie and user into the lists. If there is no rating by the user,
# TODO this should be represented as a zero.
# TODO should the creation of the testing matrix be here too?


def get_trending_scores():
    """
    fills a dictionary with trending scores. Movie id is the key and normalized score is the value.

    :return: trending_scores in the form a of a dictionary
    """
    trending_scores = {}

    for row in session.query(TrendingScore).all():
        trending_scores[row.movie_id] = row.normalized_score

    return trending_scores


def get_train_matrix():
    """
    returns the train matrix. The matrix is 80% (4/5) of the user ratings at the moment

    :return: training matrix in the form of a numpy matrix
    """
    user_list = []
    movie_list = []
    rating_list = []

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
    returns the new users matrix. The matrix is 10 % of the user ratings. Is used for showing that model is evolving

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
    returns the movie title from a movie id input

    :param movie_id:
    :return: movie name as string
    """
    return session.query(Movie.title).filter(Movie.id == movie_id).one()[0]

