import numpy as np
import csv

#TODO : fetch list length from database instead of csv

def generate_random_trending_scores():
    # Find path of this file in the system, only keep from the root to Product
    a,b = __file__.split('Product')

    # Add to the path generated above the end of the path to get to the csv file
    path_to_movie_set = a + 'Product/Database/DbFillMovieLensGitLab/movies.csv'

    # Count the number of items
    with open(path_to_movie_set, 'rt') as movies:
        spamreader = csv.reader(movies)
        movies_number = 0
        for row in spamreader:
            movies_number += 1

    # Generate movies_number random floats between 0 and 1
    trending_scores = np.random.ranf(movies_number)
    return trending_scores


