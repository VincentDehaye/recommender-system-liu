import numpy as np
import matplotlib.pyplot as plt
from Product.RecommendationManager.model import generate_model as generate_model

# TODO - Fix this script to show improvement graph
def evolve_model_graph(train_matrix):
    """
    Author: Gustaf Norberg
    Date: 2017-11-15
    Last update: 2017-11-20
    Purpose: should generate a graph to show improvement over time, not finished.
    """
    alpha = 1e-3
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
        adadelta_precision_at_k.append(generate_model.test_precision(adadelta_model, train_matrix, k))

    x = np.arange(len(adagrad_precision_at_k))
    plt.plot(x, np.array(adagrad_precision_at_k))
    plt.plot(x, np.array(adadelta_precision_at_k))
    plt.legend(['adagrad', 'adadelta'], loc='lower right')
    plt.show()


    print("adadelta")
    for value in adadelta_precision_at_k:
        print(value)

    for value in adagrad_precision_at_k:
        print(value)


