import matplotlib.pyplot as plt
import numpy as np

def get_plot(start_x, end_x, start_y, end_y):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    X = np.linspace(start_x, end_x, 100)
    Y = np.linspace(start_y, end_y, 100)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, antialiased=False)

    return fig