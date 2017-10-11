from lightfm import LightFM
from lightfm.datasets import fetch_movielens

import pickle


# this function trains the model with the data from movielens
def train_model(filename):
    # TODO Instead of getting the dataset from movielens, we should get it from our own DB.
    data = fetch_movielens()

    model = LightFM(loss='warp')
    model.fit(data['train'], epochs=30, num_threads=2)

    # saves the trained model to filename
    pickle.dump(model, open(filename, 'wb'))


# loads trained model
def load_model(filename):
    return pickle.load(open(filename, 'rb'))


