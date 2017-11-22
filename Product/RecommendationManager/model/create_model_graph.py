"""
creates a plot graph over adadelta and adagrad. Can be used to find out which model parameters
are  best.
"""
import numpy as np
import matplotlib.pyplot as plt
from Product.RecommendationManager.model import generate_model as generate_model
from Product.RecommendationManager import gets_from_database as get_matrices


def evolve_model_graph(train_matrix):
    """
    Author: Gustaf Norberg
    Date: 2017-11-15
    Last update: 2017-11-20
    Purpose: should generate a graph to show improvement over time.
    """
    alpha = 1e-3
    # TODO change the constant epochs to be the same as the in generate model
    epochs = 50
    k = 10

    adagrad_model = generate_model.LightFM(no_components=30,
                                           loss='warp',
                                           learning_schedule='adagrad',
                                           user_alpha=alpha,
                                           item_alpha=alpha)

    adadelta_model = generate_model.LightFM(no_components=30,
                                            loss='warp',
                                            learning_schedule='adadelta',
                                            user_alpha=alpha,
                                            item_alpha=alpha)

    adagrad_precision_at_k = []

    for epoch in range(epochs):
        adagrad_model.fit_partial(train_matrix, epochs=1)
        adagrad_precision_at_k.append(generate_model.test_precision(adagrad_model, train_matrix, k))

    adadelta_precision_at_k = []

    for epoch in range(epochs):
        adadelta_model.fit_partial(train_matrix, epochs=1)
        adadelta_precision_at_k.append(generate_model.test_precision(adadelta_model,
                                                                     train_matrix,
                                                                     k))

    x_value = np.arange(len(adagrad_precision_at_k))
    plt.plot(x_value, np.array(adagrad_precision_at_k))
    plt.plot(x_value, np.array(adadelta_precision_at_k))
    plt.legend(['adagrad', 'adadelta'], loc='lower right')
    plt.show()


    print("adadelta")
    for value in adadelta_precision_at_k:
        print(value)

    for value in adagrad_precision_at_k:
        print(value)

# evolve_model_graph(get_matrices.get_train_matrix())
