import matplotlib.pyplot as plt
import numpy as np
import random

def get_plot():

    x = [30, 25, 20, 15, 10]
    labels = ["Banans", "Apples", "Pears", "Oranges", "Avocado"] 

    def to_pct(p):
        return "{:.1f}%".format(p)

    fig, ax = plt.subplots()

    ax.pie(x, autopct=lambda pct: to_pct(pct), textprops={'color':'white'}, startangle=random.uniform(-180, 180))
    fig.legend(labels)
    fig.suptitle("User favors in fruits")

    return fig