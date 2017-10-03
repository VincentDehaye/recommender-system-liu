import numpy as np

from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

from Product.Database.DBConn import session, User, Movie, Rating
from scipy.sparse import coo_matrix


#This file in contrast to lightfm_example will try to use our own database to create a recommendation list.



# Load the MovieLens 100k dataset.
data = fetch_movielens()

#As we can see when printing, data['train'] is a "sparse matrix" (coo_matrix).
print('this is the data in the dataset. (userid, movieid) rating')
print(data['train'])
#As we can see when printing, data['item_labels'] is an array?,
print('this is the movies in the dataset')
print(data['item_labels'])

#TODO Save this information in the same format as data['train'], e.g. sparse matrix
Ratings = session.query(Rating).all()
#print(Ratings)

#count=Ratings.__len__()
#while count != 0:
    #count=count-1
    #print(Ratings[count])

#TODO Save this information in the same format as data['item_labels'], e.g. array?
movieList=[]
Movies = session.query(Movie).all()
print(Movies)
for row in session.query(Movie.title):
    movieList.append(row)
print(movieList)


#Trying to understand how "sparse matrix" works.
m = coo_matrix([[1,2,3],[4,5,6]])
m1 = m.tocsr()
print(m)
print(m1)
print(m1[1,2])


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
# TODO The output from this function should be a list of length 10 with ID:s that corresponds to the predicted movies.
sample_recommendation(model, data, range(0, 3))