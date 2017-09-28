import numpy as np

from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

# this example will get you started on how

# Load the MovieLens 100k dataset.
data = fetch_movielens()

# Instantiate and train the model
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)
print('this is the data in the dataset. (userid, movieid) rating')
print(data['train'])

# Evaluate the trained model by comparing it with the original data
# It evaluates the top 5 movies (k=5)

test_precision = precision_at_k(model, data['test'], k=5).mean()

# this prints the test precision

print(test_precision)


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

        for x in top_items[:3]:
            print("        %s" % x)


sample_recommendation(model, data, range(0,3))