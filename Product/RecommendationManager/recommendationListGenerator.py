import numpy as np

from lightfm import LightFM
from lightfm.evaluation import precision_at_k

from Product.Database.DBConn import session, TrendingScore, Movie
from scipy.sparse import coo_matrix
import generateModel as gen_model
import getTrainMatrixFromDb as get_train_matrix


trending_scores={}

# gets the normalized scores from the database
# adds the scores to a dictionary. {id: score}
for row in enumerate(session.query(TrendingScore.movie_id, TrendingScore.normalized_score)):
    # row[1][0] is movie_id
    # row[1][1] is normalized trending score
    #print(row[1][0])
    trending_scores[row[1][0]]=row[1][1]


#def get_movie_title_from_db(id):
   # for row in enumerate(session.query(Movie.title)).\
   #         filter(Movie.id==id):
   #     return row
#
def get_movie_title_from_db(id):
    for movie in session.query(Movie.title).\
             filter(Movie.id == id):
        return movie
#print(trending_scores)

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
        normalized_scores=normalize_user_scores(scores)
        print("This is the recommended movie_ids for user:" + str(user_id))

        #argsort gets the movie ids for the corresponding scores.

        for movie_id in np.argsort(-scores):

            movie_scores[movie_id]=normalized_scores[movie_id]

        #trending score weight.
        w = 1.5

        trending_and_user_pref_scores={}

        # adds the movie scores to the trending scores to create an aggregated dictionary
        for id in trending_scores:
            trending_and_user_pref_scores[id] = movie_scores[id]+w*trending_scores[id]

        print(trending_and_user_pref_scores[2])
        #print(sorted(trending_and_user_pref_scores, key=trending_and_user_pref_scores.get, reverse=True)[:5])
        top5items = sorted(trending_and_user_pref_scores, key=trending_and_user_pref_scores.get, reverse=True)[:5]
        #print(top5items)
        top5itemlist=[]
        for id in top5items:
            #TODO get the movie name from the id.
            print('\nid: %s '%id)

            movie_title=get_movie_title_from_db(id)
            print(movie_title[0])
            print('with score')
            print(trending_and_user_pref_scores[id])
            top5itemlist.append([movie_title[0], trending_and_user_pref_scores[id]])
        print(top5itemlist)
        return top5itemlist
model = gen_model.load_model('new_model.sav')

#print(get_train_matrix.getMovieList())

trainmatrix = get_train_matrix.getTrainMatrix()

# Calls upon the sample_recommendation to create a recommendation list for user 56.
sample_recommendation(model, trainmatrix, range(56, 57))

