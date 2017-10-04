import numpy as np
import json as json
from lightfm import LightFM
# TODO Instead of getting the dataset from movielens, we should get it from our own DB.
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

# this example will get you started on how lightfm works.

# Load the MovieLens 100k dataset.
data = fetch_movielens()

# Printing the data in the dataset.
print('this is the data in the dataset. (userid, movieid) rating')
print(data['train'])
print('This is a list of all movies')
print(data['item_labels'])

# Instantiate and train the model
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)

# Evaluate the trained model by comparing it with the original data
# It evaluates the precision for the top k=5 movies from the algorithm
test_precision = precision_at_k(model, data['test'], k=5).mean()

# this prints the test precision
# the precision is in percentage.
print('precision: %s' % test_precision)

def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape

    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]

        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:10]:
            print("        %s" % x)


# this method prints the recommended and known positives for the first three users
# known positives are movies that users have watched and rated highly
# recommended are the movies that lightfm recommends.
# observe that the user id is +1 and movie_id +1 in the dataset compared to the method output
# That is because arrays start at 0 in python and.
# TODO Each movie should be related to an id in our own database so that the integration with trending is done smootlhy.
# TODO The output from this function should be a list of length 10 with ID:s that corresponds to the predicted movies.
#sample_recommendation(model, data, range(0, 3))



# TODO find out what argsort is. read how numpy works.
def sample_output_to_visualisation(model, data):
    n_users, n_items = data['train'].shape
    dictionary = {}

    for user_id in range(0, n_users):

        scores = model.predict(user_id, np.arange(n_items))

        print('prints the top 10 scores user %s' % user_id)
        print(np.sort(-scores[:10]).tolist())
        # np.argsort(-scores) outputs the indexes for the movie ids (sorted by score)
        # When we change the dataset we will instead output movie id.
        # there will be a database call to get the right movie_id

        print('prints the top 10 scores corresponding index for user %s' % user_id)
        print(np.argsort(-scores)[:10].tolist())

        # adds to a dictionary
        # user_id is the dictionary key
        # the index and the scores are in an array

        dictionary[user_id]=[np.argsort(-scores)[:10].tolist(), np.sort(-scores[:10]).tolist()]

    # prints the dictionary
    print(dictionary)
    # see if there is a difference when converted to json
    print(json.dumps(dictionary))
    # looks at the movie ids and scores for user_id=9
    print(dictionary[9])
    # same but in json to spot any differences
    print(json.dumps(dictionary[9]))

sample_output_to_visualisation(model, data)
