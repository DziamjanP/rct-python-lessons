import matplotlib.pyplot as plt
import numpy as np

def get_plot(positiona=(1,1), positionb=(5,2), positionc = (3,4), cluster_size = 50, cluster_sigma = 0.4):
    fig, ax = plt.subplots()

    x = np.random.normal(positiona[0], cluster_sigma, cluster_size)
    y = np.random.normal(positiona[1], cluster_sigma, cluster_size)

    ax.scatter(x, y, color="red", label = "кластэр 1", marker="o")

    x = np.random.normal(positionb[0], cluster_sigma, cluster_size)
    y = np.random.normal(positionb[1], cluster_sigma, cluster_size)

    ax.scatter(x, y, color="green", label = "кластэр 2", marker="D")

    x = np.random.normal(positionc[0], cluster_sigma, cluster_size)
    y = np.random.normal(positionc[1], cluster_sigma, cluster_size)

    ax.scatter(x, y, color="blue", label = "кластэр 3", marker="v")
    fig.legend()
    fig.suptitle("Кропкавая дыяграма з каляровымі кластэрамі")

    return fig