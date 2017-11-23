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
    Last update: 2017-11-23
    Purpose: Generates a graph to show how quick the model is trained as well as to what precision we can train the
    model. Stops evolving when the change is still bigger than 1 %
    """
    alpha = 1e-3
    # TODO change the constant epochs to be the same as the in generate model
    epochs = 30
    k = 10
    stop = 1/100

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

    for i in range(epochs):
        adagrad_model.fit_partial(train_matrix, epochs=1)
        adagrad_precision_at_k.append(generate_model.test_precision(adagrad_model, train_matrix, k))
        if (i > 1 and adagrad_precision_at_k[i] - adagrad_precision_at_k[i-1] < stop):
            epochs = i+1
            break

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