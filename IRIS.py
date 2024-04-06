# IRIS Dataset

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('IRIS.csv')

plt.subplot(1, 2, 1)
plt.scatter(dataset['sepal_length'], dataset['sepal_width'])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')

plt.subplot(1, 2, 2)
plt.scatter(dataset['petal_length'], dataset['petal_width'])
plt.xlabel('petal_length')
plt.ylabel('petal_width')

plt.legend()
plt.show()