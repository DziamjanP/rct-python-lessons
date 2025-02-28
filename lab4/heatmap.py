import matplotlib.pyplot as plt
import numpy as np

m = np.random.rand(10, 10)

plt.title("Heatmap")
plt.imshow(m, cmap="hot")
plt.colorbar()

plt.savefig("plots/heatmap.png", bbox_inches='tight')
plt.savefig("plots/heatmap.pdf", bbox_inches='tight')
