from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.Database.DBConn import create_session
from Product.Database.DBConn import User


def test_retrieve_all_users():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Lates Update: 2017-11-20
    Purpose: Assert that users are retrieved from the database correctly
    """

    # PRE-CONDITIONS
    user_id = -1
    user_age = 10
    user_gender = "Male"
    user_occupation = "Student"

    # We create a session and add a dummy user
    session = create_session()
    dummy_user = User(id=user_id, age=user_age, gender=user_gender, occupation=user_occupation)
    session.add(dummy_user)
    session.commit()

    # EXPECTED OUTPUT
    expected_user_id = user_id
    expected_user_age = user_age
    expected_user_gender = user_gender
    expected_user_occupation = user_occupation

    # OBSERVED OUTPUT
    # We call the method to be tested that retrieves all the users
    observed_all_users = RetrieveUser().retrieve_all_users()

    # We look for the user we added, and observe the attributes
    observed_user_id = None
    observed_user_age = None
    observed_user_gender = None
    observed_user_occupation = None

    for user in observed_all_users:
        if user.id == user_id:
            observed_user_id = user.id
            observed_user_age = user.age
            observed_user_gender = user.gender
            observed_user_occupation = user.occupation
            break

    # After adding the dummy user we remove them again.
    session.delete(dummy_user)
    session.commit()

    assert observed_all_users
    assert observed_user_id == expected_user_id
    assert observed_user_age == expected_user_age
    assert observed_user_gender == expected_user_gender
    assert observed_user_occupation == expected_user_occupation


def test_check_if_user_in_rating():
    # TODO finish this unit test
    assert True


def test_retrieve_largest_user_id():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-20
    Lates Update: 2017-11-20
    Purpose: Assert that the highest user id is retrieved
    """

    # PRE-CONDITIONS
    user_id = 9999999999999999

    # We create a session and add a dummy user
    session = create_session()
    dummy_user = User(id=user_id, age=20, gender='Male', occupation='Student')
    session.add(dummy_user)
    session.commit()

    # EXPECTED OUTPUT
    expected_user_id = user_id

    # OBSERVED OUTPUT
    # We call the method to be tested that retrieves all the users
    observed_user_user_id = RetrieveUser().retrieve_largest_user_id()

    # After adding the dummy user we remove them again.
    session.delete(dummy_user)
    session.commit()

    assert observed_user_user_id == expected_user_id
