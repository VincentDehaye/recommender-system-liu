from Product.Database.DBConn import create_session, User
from Product.Database import DBConn

'''
Author: Eric Petersson, Vincent Dehaye
Date: 13/11/2017
Last update: 20/11/2017
Purpose: Filter users on metadata values
'''

def get_user_group_ids(age, gender):
    age_list = get_restricted_ids("User", "age", age[0], age[1])
    gender_list = get_restricted_match("User",["gender"],[gender])
    output = set(age_list) & set(gender_list)
    return output


def get_restricted_ids(table, feature, min, max):
    """
    :param table: table name in database
    :param feature: column name in database
    :param min: minimum value
    :param max: maximum value
    :return: list of the ids of records of the desired table between the min and max boundaries
    """
    session = create_session()
    sqltable = getattr(DBConn, table)
    objects_list = session.query(sqltable).\
        filter((getattr(sqltable, feature) >= min) & (getattr(sqltable, feature) <= max)).all()
    output_list = []
    for object in objects_list:
        output_list.append(object.id)
    return output_list

# Example : output only the ids of Movies which year feature is comprised
# between 2015 and 2016
# list = get_restricted_ids('Movie','year',2015,2016)
# print(list)

def get_restricted_match(table, feature_list, list_of_matching_strings_list):
    """
    :param table: table name in database
    :param feature_list: list of strings, features one want to restrict on
    :param list_of_matching_strings_list: list of lists of values to match for each feature
    :return: list of the ids of records of the desired table matching the given string
    """
    session = create_session()
    if len(feature_list) != len(list_of_matching_strings_list):
        return "Length of features list different of length of list of matching strings list"

    if not all(isinstance(n, str) for n in feature_list):
        return "Feature list must only contain strings"

    if not all(isinstance(n, list) for n in list_of_matching_strings_list):
        return "List of matching strings list must only contain lists"

    for sublist in list_of_matching_strings_list:
        if not all(isinstance(n, str) for n in sublist):
            return "List of matching strings must only contain strings"

    # for feature in feature_list:

    output_list = []


    feature_list_current_position = 0
    query = "session.query(" + str(table) + ").filter("
    filters = "("
    for feature in feature_list:
        filters += "("
        for string in list_of_matching_strings_list[feature_list_current_position]:
            filters += str(table) + "." + str(feature) + " == '" + string + "') | ("

        filters = filters[:-4]
        feature_list_current_position += 1
        filters += ") & ("

    filters = filters[:-4]
    query += filters + ").all()"

    result = eval(query)

    for object in result:
        output_list.append(object.id)
    return output_list
