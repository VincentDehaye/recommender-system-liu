"""
Copy pasted from recommendationListGenerator but without clutter
just to create a working integration to visualization.

"""
from Product.RecommendationManager import generate_model as gen_model
from Product.RecommendationManager import gets_from_database as get_train_matrix
import numpy as np

def normalize_user_scores(scores):
    min_score = np.amin(scores)
    max_score = np.amax(scores)

    for i in range(0, len(scores)):
        scores[i] = (scores[i] - min_score) / (max_score - min_score)

    return scores


# Sends in our testmatrix and the user_ids for the users to present recommendations
def sample_recommendation(model, train_matrix, user_id, trending_weight):
    n_users, n_items = train_matrix.shape

    # gets the normalized scores from the database
    # adds the scores to a dictionary. {id: score}
    trending_scores = get_train_matrix.get_trending_scores()

    movie_scores = {}
    scores = model.predict(user_id, np.arange(n_items))
    normalized_scores = normalize_user_scores(scores)

    # argsort gets the movie ids for the corresponding scores.

    for movie_id in np.argsort(-scores):
        movie_scores[movie_id] = normalized_scores[movie_id]

    trending_and_user_pref_scores = {}

    # adds the movie scores to the trending scores to create an aggregated dictionary
    for id in trending_scores:
        trending_and_user_pref_scores[id] = movie_scores[id] + trending_weight * trending_scores[id]

    top10items = sorted(trending_and_user_pref_scores, key=trending_and_user_pref_scores.get, reverse=True)[:10]
    #print(top10items)
    top10itemlist = []
    innerdict={}
    for id in top10items:
        movie_title = get_train_matrix.get_movie_title(id)
        innerdict['id', 'title', 'score'] = id, movie_title, trending_and_user_pref_scores[id]
        #top10itemlist.append(innerdict)
        #print(id)
        #print(innerdict)
        # has to do a copy otherwise it references the original dictionary
        # we only want the last generated dict and not all of it.
        top10itemlist.append(innerdict.copy())
        #print(top10itemlist)
    #print(innerdict)

    recommendation_dict={}
    recommendation_dict['user_id', 'recommendation_list']=user_id, top10itemlist
    #print(recommendation_dict)
    return recommendation_dict


def get_aggregated_recommendation_for_a_user(user_id):

    model = gen_model.load_model('../new_model.sav')

    train_matrix = get_train_matrix.get_train_matrix()

    trending_weight = 1

    return sample_recommendation(model, train_matrix, user_id, trending_weight)

# rec_dict =(get_aggregated_recommendation_for_a_user(55))

# prints just the user_id
# print(rec_dict['user_id', 'recommendation_list'][0])
# prints the recommendation_list
# print(rec_dict['user_id', 'recommendation_list'][1])
# prints entire dict
# print(rec_dict)
