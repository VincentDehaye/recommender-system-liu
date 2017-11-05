import numpy as np

from lightfm import LightFM

import generate_model as gen_model
import getTrainMatrixFromDb as get_train_matrix


def normalize_user_scores(scores):
    min_score = np.amin(scores)
    max_score = np.amax(scores)

    for i in range(0, len(scores)):
        scores[i] = (scores[i] - min_score)/(max_score-min_score)

    return scores

# Sends in our testmatrix and the user_ids for the users to present recommendations
def sample_recommendation(model, train_matrix, user_ids, trending_weight):
    n_users, n_items = train_matrix.shape

    # gets the normalized scores from the database
    # adds the scores to a dictionary. {id: score}
    trending_scores=get_train_matrix.get_trending_scores()
    # for each user:
    for user_id in user_ids:

        movie_scores={}
        scores = model.predict(user_id, np.arange(n_items))
        normalized_scores=normalize_user_scores(scores)
        print("This is the recommended movie_ids for user:" + str(user_id))

        # argsort gets the movie ids for the corresponding scores.

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
            print('\nmovie id: %s '%id)

            movie_title=get_train_matrix.get_movie_title(id)
            print(movie_title)
            print('with score')
            print(trending_and_user_pref_scores[id])
            top5itemlist.append([movie_title, trending_and_user_pref_scores[id]])
        #print(top5itemlist)
        return top5itemlist

model = gen_model.load_model('new_model.sav')
print("2")
#print(get_train_matrix.getMovieList())

trainmatrix = get_train_matrix.get_train_matrix()
print("3")
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

