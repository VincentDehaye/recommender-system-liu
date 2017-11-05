
from scipy.sparse import coo_matrix

from Product.Database.DBConn import session, Rating, TrendingScore, Movie

### old TODOS, ok to delete?
# Filling the lists with data from the database
# This way of doing a testmatrix is wrong it will result in a different size matrix then the Trainmatrix.
# TODO Should only collect ratings over 3, otherwise even a one is treated as a positive rating. We should load
# TODO the combination of every movie and user into the lists. If there is no rating by the user,
# TODO this should be represented as a zero.
# TODO should the creation of the testing matrix be here too?


# fills a dictionary with trending scores. Movie id is the key and normalized score is the value.
def get_trending_scores():
    trending_scores = {}

    for row in (session.query(TrendingScore).all()):
        trending_scores[row.movie_id] = row.normalized_score

    return trending_scores


# returns the train matrix. The matrix is 80% (4/5) of the user ratings at the moment
def get_train_matrix():
    user_list = []
    movie_list = []
    rating_list = []
    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 5 != 0:
            user_list.append(row[0])
            movie_list.append(row[1])
            rating_list.append(row[2])

    train_matrix = coo_matrix((rating_list, (user_list, movie_list)))

    return train_matrix


# returns the test matrix. The matrix is 20% (1/5) of the user ratings at the moment
def get_test_matrix():
    test_user_list = []
    test_movie_list = []
    test_rating_list = []

    for counter, row in enumerate(session.query(Rating.user_id, Rating.movie_id, Rating.rating)):
        if counter % 5 == 0:
            test_user_list.append(row[0])
            test_movie_list.append(row[1])
            test_rating_list.append(row[2])

    test_matrix = coo_matrix((test_rating_list, (test_user_list, test_movie_list)))

    return test_matrix


# returns the movie title from a movie id input
def get_movie_title(movie_id):
    return session.query(Movie.title).filter(Movie.id == movie_id).one()[0]

