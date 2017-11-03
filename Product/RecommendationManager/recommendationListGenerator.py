import numpy as np

from lightfm import LightFM
from lightfm.evaluation import precision_at_k

from Product.Database.DBConn import session, TrendingScore, Movie
from scipy.sparse import coo_matrix
import generateModel as gen_model
import getTrainMatrixFromDb as get_train_matrix




#def get_movie_title_from_db(id):
   # for row in enumerate(session.query(Movie.title)).\
   #         filter(Movie.id==id):
   #     return row
# TODO move to db file also fix for loop
def get_movie_title_from_db(id):
    for movie in session.query(Movie.title).\
             filter(Movie.id == id):
        return movie
#print(trending_scores)

# Evaluate the trained model by comparing it with the original data
# It evaluates the precision for the top k movies from the algorithm
# Could be a good idea to move this to another file since it takes a lot of time to run
# TODO move this to generate model.
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
def sample_recommendation(model, trainmatrix, user_ids, trending_weight):
    n_users, n_items = trainmatrix.shape
    trending_scores = {}

    # gets the normalized scores from the database
    # adds the scores to a dictionary. {id: score}
    # TODO move to db queries file
    for row in enumerate(session.query(TrendingScore.movie_id, TrendingScore.normalized_score)):
        # row[1][0] is movie_id
        # row[1][1] is normalized trending score
        # print(row[1][0])
        trending_scores[row[1][0]] = row[1][1]

    # for each user:
    for user_id in user_ids:

        movie_scores={}
        scores = model.predict(user_id, np.arange(n_items))
        normalized_scores=normalize_user_scores(scores)
        print("This is the recommended movie_ids for user:" + str(user_id))

        #argsort gets the movie ids for the corresponding scores.

        for movie_id in np.argsort(-scores):

            movie_scores[movie_id]=normalized_scores[movie_id]

        trending_and_user_pref_scores={}

        # adds the movie scores to the trending scores to create an aggregated dictionary
        for id in trending_scores:
            trending_and_user_pref_scores[id] = movie_scores[id]+trending_weight*trending_scores[id]

        print(trending_and_user_pref_scores[2])
        #print(sorted(trending_and_user_pref_scores, key=trending_and_user_pref_scores.get, reverse=True)[:5])
        top5items = sorted(trending_and_user_pref_scores, key=trending_and_user_pref_scores.get, reverse=True)[:5]
        #print(top5items)
        top5itemlist=[]
        for id in top5items:
            #TODO get the movie name from the id.
            print('\nmovie id: %s '%id)

            movie_title=get_movie_title_from_db(id)
            print(movie_title[0])
            print('with score')
            print(trending_and_user_pref_scores[id])
            top5itemlist.append([movie_title[0], trending_and_user_pref_scores[id]])
        #print(top5itemlist)
        return top5itemlist
model = gen_model.load_model('new_model.sav')

#print(get_train_matrix.getMovieList())

trainmatrix = get_train_matrix.getTrainMatrix()

# Calls upon the sample_recommendation to create a recommendation list for user 56.
trending_weight=1.5
#sample_recommendation(model, trainmatrix, range(56, 57), trending_weight)

user_id=0
continue_flag='y'
while(continue_flag=='y'):
    user_id=int(input('Which user do you want to check (between 0 and 671): '))
    trending_weight = float(input('What trending weight do you want: '))

    sample_recommendation(model, trainmatrix, range(user_id, user_id+1), trending_weight)
    continue_flag=input('Do you want to check another user? (y/n): ')
