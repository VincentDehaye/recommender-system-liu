from Product.RecommendationManager import generate_model as generate_model
def test_create_new_model():
    """
    Author: Alexander Dahl
    Date: 2017-11-05
    Purpose: Assert that create_new_model creates a model and saves it to disk
    """

    generate_model.train_model('test_new_model.sav')

    assert()

