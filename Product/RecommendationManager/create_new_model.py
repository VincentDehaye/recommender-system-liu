"""
This file creates a new model by calling the train model method
in generate model. The param is the file name.
"""
from Product.RecommendationManager import generate_model as generate_model

generate_model.train_model('new_model.sav')
