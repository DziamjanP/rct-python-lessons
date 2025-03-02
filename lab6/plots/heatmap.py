import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

def get_plot(size_x, size_y):
    m = np.random.rand(size_x, size_y)

    fig, ax = plt.subplots()
    
    fig.suptitle("Heatmap")
    im = ax.imshow(m, cmap="hot")
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')

    return fig
