import matplotlib.pyplot as plt
import numpy as np

def get_plot():
    x = [200, 100, 350, 250]
    y = ["Orange", "Banana", "Avocado", "Apple"]

    fig, ax = plt.subplots()

    ax.barh(y, x)
    fig.suptitle("Fruit data")
    ax.set_ylabel("Fruits")
    ax.set_xlabel("Amount")

    return fig
