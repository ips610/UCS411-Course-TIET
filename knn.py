import numpy as np
import pandas as pd
df = pd.read_csv('/content/Untitled spreadsheet - Sheet1.csv')
x = df.iloc[:,:-1].values

y = df.iloc[:,-1:].values
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
class knn:
    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_values = [self.y_train[i] for i in k_indices]
        prediction=np.mean(k_values)
        return prediction
knn = knn(5)
knn.fit(x, y)
candidate_1 = [5,8,10]
candidate_2 = [8,7,6]
predictions = knn.predict([candidate_1,candidate_2])
print(predictions)