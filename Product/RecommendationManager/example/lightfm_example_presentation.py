import numpy as np
from lightfm import LightFM
# TODO Instead of getting the dataset from movielens, we should get it from our own DB.
from lightfm.datasets import fetch_movielens


# this example will get you started on how lightfm works.

# Load the MovieLens 100k dataset.
data = fetch_movielens()

# Instantiate and train the model
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)


def output_specific_user_recommendations_terminal_prompt(model, data):
    n_users, n_items = data['train'].shape
    continue_flag = 'yes'
    while (continue_flag == 'yes'):
        n_users_display = n_users - 1
        user_checked = input('Which user user do you want to check (between 0 and %s): ' % n_users_display)
        scores = model.predict(user_checked, np.arange(n_items))
        print('prints the top 10 scores user %s' % user_checked)
        print(np.sort(-scores[:10]).tolist())
        # np.argsort(-scores) outputs the indexes for the movie ids (sorted by score)
        # When we change the dataset we will instead output movie id.
        # there will be a database call to get the right movie_id
        print('prints the top 10 scores corresponding movie id for user %s' % user_checked)
        print(np.argsort(-scores)[:10].tolist())
        continue_flag = input('Do you want to check another user ? Type yes if you do, whatever otherwise : ')

output_specific_user_recommendations_terminal_prompt(model, data)

