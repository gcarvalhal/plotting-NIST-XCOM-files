
# encoding: utf-8


import matplotlib.pyplot as plt
import pandas as pd

filename = "XCOM Cu.txt"

df = pd.read_csv(filename, delimiter=" ", comment="#")

x = df.iloc[:, 0]
y = df.iloc[:, 7]

plt.plot(x, y, 'o', label=filename)
plt.title(filename)
plt.show()
