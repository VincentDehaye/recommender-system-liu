import pytest
from Product.RecommendationManager import generate_model as generate_model
from Product.RecommendationManager import gets_from_database as get_matrices


def test_test_precision():
    """
    Author: Alexander Dahl
    Date: 2017-11-12
    Last update: 2017-11-12
    Purpose: Asserts that the lightfm precision@k puts out a positive number
    """
    # Pre-Conditions
    generate_model.train_model('test_new_model.sav')
    model = generate_model.load_model('test_new_model.sav')
    train_matrix = get_matrices.get_train_matrix()
    # Expected output
    # >0
    assert(generate_model.test_precision(model,train_matrix, 10) > 0)


def test_evolve_model():
    """
    Author: Gustaf Norberg
    Date: 2017-11-13
    Last update: 2017-11-13
    Purpose: Tests that model evolves after running evolve_model
    """
    # Pre-Conditions
    generate_model.train_model('test_new_model.sav')
    model = generate_model.load_model('test_new_model.sav')
    train_matrix = get_matrices.get_train_matrix()
    new_users_matrix = get_matrices.get_new_users_matrix()
    test_matrix = get_matrices.get_test_matrix()
    k = 10

    value_before = generate_model.test_precision(model, train_matrix, k)
    generate_model.evolve_model('test_new_model.sav', model, new_users_matrix)
    value_after = generate_model.test_precision(model, train_matrix + new_users_matrix, k)

    print("Value before")
    print(value_before)
    print("Value after")
    print(value_after)
    # Expected output > 0
    # since value_after > value_before
    assert(value_after - value_before >= 0)


def test_test_precision():
    """
    Author: Alexander Dahl
    Date: 2017-11-12
    Last update: 2017-11-12
    Purpose: Asserts that the lightfm precision@k puts out a positive number
    """
    # Pre-Conditions
    generate_model.train_model('test_new_model.sav')
    model = generate_model.load_model('test_new_model.sav')
    train_matrix = get_matrices.get_train_matrix()
    # Expected output
    # >0
    assert(generate_model.test_precision(model,train_matrix, 10) > 0)

test_evolve_model()