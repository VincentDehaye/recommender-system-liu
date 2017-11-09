import numpy as np

from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from lightfm.evaluation import auc_score

import generate_model as gen_model
import gets_from_database as get_train_matrix


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
#print(get_train_matrix.getMovieList())

trainmatrix = get_train_matrix.get_train_matrix()
testmatrix = get_train_matrix.get_test_matrix()
new_user_matrix = get_train_matrix.get_new_users_matrix()
#trainmatrix, testmatrix, new_user_matrix = get_train_matrix.get_matricies()

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





trending_weight=1
#sample_recommendation(model, trainmatrix, range(56, 57), trending_weight)

user_id=0
continue_flag='y'
while(continue_flag=='y'):
    user_id=int(input('Which user do you want to check (between 0 and 99): '))
    trending_weight = float(input('What trending weight do you want: '))

    sample_recommendation(model, trainmatrix, range(user_id, user_id+1), trending_weight)
    continue_flag=input('Do you want to check another user? (y/n): ')

