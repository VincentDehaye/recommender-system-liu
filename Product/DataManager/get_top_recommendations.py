from Product.Database.DBConn import create_session, Recommendation
from Product.DataManager.restrict import get_user_group_ids
from Product.RecommendationManager import gets_from_database as gets_from_database

"""
Author: Eric Petersson, Vincent Dehaye
Date: 2017-11-21
Last update:
Purpose: Return the movies which has been the most recommended for the users considered
"""

def get_top_recommendations(age_range, gender_list):
    # Example call for all users : get_top_recommandations([], [])
    # Example call for only Male and Unknown users : get_top_recommandations([],["Male", "Unknown"])
    # Example call for users only between 15 and 35 : get_top_recommandations([15,35], [])
    # Example call for Female users between 35 and 50 : get_top_recommandations([35,50], ["Female"])

    # Generates the list of users matching the query
    list_of_matching_users = get_user_group_ids(age_range, gender_list)

    # Will be the list of recommended movies, and the number of time the were recommended.
    toplist = {}
    session = create_session()

    # Populates toplist.
    for user in list_of_matching_users:
        recommended_to_user = session.query(Recommendation).filter(Recommendation.user_id == user).all()
        for recommendation in recommended_to_user:
            if recommendation.movie_id not in toplist:
                toplist[recommendation.movie_id] = 1
            else:
                toplist[recommendation.movie_id] += 1

    output_list = []

    keys = sorted(toplist.items(), key=lambda x: x[1], reverse=True)

    # Prints toplist
    for k, v in keys:
        tmp_dict = {}
        tmp_dict["id"] = k
        tmp_dict["title"] = gets_from_database.get_movie_title(k)
        tmp_dict["count"] = v
        output_list.append(tmp_dict)

    return output_list


print(get_top_recommendations([],[]))
