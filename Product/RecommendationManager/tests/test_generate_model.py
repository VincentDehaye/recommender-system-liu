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
    model=generate_model.load_model('test_new_model.sav')
    train_matrix = get_matrices.get_train_matrix()
    # Expected output
    # >0
    assert(generate_model.test_precision(model,train_matrix, 10) > 0)
