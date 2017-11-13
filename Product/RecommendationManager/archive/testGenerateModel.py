import sys
sys.path.append('../')
from lightfm.datasets import fetch_movielens
import numpy as np
import generateModel as gen_model

filename='test_trained_model.sav'

# TODO make a real test that follows testing conventions

# quick dirty test
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


gen_model.train_model(filename)

loaded_model = gen_model.load_model(filename)

data=fetch_movielens()
sample_recommendation(loaded_model, data, range(0, 3))

# load it again for visual inspection

loaded_model = gen_model.load_model(filename)

data=fetch_movielens()
sample_recommendation(loaded_model, data, range(0, 3))