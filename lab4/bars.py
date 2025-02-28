import matplotlib.pyplot as plt
import numpy as np

x = [200, 100, 350, 250]
y = ["Orange", "Banana", "Avocado", "Apple"]

plt.barh(y, x)
plt.title("Fruit data")
plt.ylabel("Fruits")
plt.xlabel("Amount")

plt.savefig("plots/bars.png", bbox_inches='tight')
plt.savefig("plots/bars.pdf", bbox_inches='tight')
