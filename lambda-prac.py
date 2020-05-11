
import numpy as np
class Perceptron:

    def __init__(self, L_rate=0.001, n_iter=10):
        self.L_rate = L_rate
        self.n_iter = n_iter

    def fit(self, X, Y):
        self._weights = np.zeros( 1 +X.shape[1])
        self._errors = []
        for iter_i in range(self.n_iter):
            errors = 0
            for xi, target in zip(X ,Y):
                predicted = self.predict(xi)
                update = self.L_rate *(target -predicted)
                self._weights[1:] += update *xi
                self._weights[0] += update
                errors += int(update != 0.0)
                self._errors.append(errors)
        return self._weights

    def netInput(self, X):
        return np.dot(X, self._weights[1:]) + self._weights[0]

    def predict(self, X):
        return np.where(self.netInput(X) >= 0.0, 1, -1)

import pandas as pd
info = pd.Series([[12,3], [1,2] ,[1,2] , 4], index=['a','b','c','d'])
print(info['b'][1])

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
print(df.tail())
import matplotlib.pyplot as plt
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values
ppn = Perceptron()
weights = ppn.fit(X, y)
print(X)
print(y)
print(weights)