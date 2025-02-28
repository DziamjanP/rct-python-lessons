import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(1, 0.4, 50)
y = np.random.normal(1, 0.4, 50)

plt.scatter(x, y, color="red", label = "кластэр 1", marker="o")

x = np.random.normal(5, 0.4, 50)
y = np.random.normal(2, 0.4, 50)

plt.scatter(x, y, color="green", label = "кластэр 2", marker="D")

x = np.random.normal(3, 0.4, 50)
y = np.random.normal(4, 0.4, 50)

plt.scatter(x, y, color="blue", label = "кластэр 3", marker="v")
plt.legend()
plt.title("Кропкавая дыяграма з каляровымі кластэрамі")

plt.savefig("plots/scatter.png", bbox_inches='tight')
plt.savefig("plots/scatter.pdf", bbox_inches='tight')
