from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.Database.DBConn import create_session
from Product.Database.DBConn import User


def test_check_if_user_in_rating():
    assert True


def test_retrieve_all_users():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Lates Update:
    Purpose: Assert that users are retrieved from the database correctly
    """

    # PRE-CONDITIONS
    user_id = -1
    user_age = 10
    user_gender = "Male"
    user_occupation = "Student"

    # We create a session and add a dummy movie to add a score to
    session = create_session()
    dummy_user = User(id=user_id, age=user_age, gender=user_gender, occupation=user_occupation)
    session.add(dummy_user)
    session.commit()

    # EXPECTED OUTPUT
    expected_user_id = user_id

    # OBSERVED OUTPUT
    # We query the the score to get a observed output
    observed_all_users = RetrieveUser().retrieve_all_users()

    observed_rating = 0
    for user in observed_all_users:
        if user.id == user_id:
            observed_user = user.id
            observed_age = user.id
            observed_gender = user.id
            observed_occupation = user.id
            break

    # After adding the dummy movie and the dummy trending score for it, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(dummy_user)
    session.commit()

    assert observed_all_users

