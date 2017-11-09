from Product.Database.DBConn import session, User, Movie
from Product.Database import DBConn


def get_restricted_ids(table, feature, min, max):
    """
    :param table: table name in database
    :param feature: column name in database
    :param min: minimum value
    :param max: maximum value
    :return: list of the ids of records of the desired table between the min and max boundaries
    """
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