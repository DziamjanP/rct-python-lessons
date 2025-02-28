import matplotlib.pyplot as plt
import numpy as np

x = [30, 25, 20, 15, 10]
labels = ["Banans", "Apples", "Pears", "Oranges", "Avocado"] 

def to_pct(p):
    return "{:.1f}%".format(p)

plt.pie(x, autopct=lambda pct: to_pct(pct), textprops={'color':'white'})
plt.legend(labels)
plt.title("User favors in fruits")

plt.savefig("plots/pie.png", bbox_inches='tight')
plt.savefig("plots/pie.pdf", bbox_inches='tight')
