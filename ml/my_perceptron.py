#!/usr/bin/env python
#
# my_perceptron.py
#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MyPerceptron:

    def __init__(self):
        self.eta = .0001
        self.iteration_count = 400
        generator = np.random.RandomState(1)
        self.w = generator.normal(loc=0, scale=.01, size=3)

    def forward(self, X):
        o = np.ones((len(X),1))
        self.X1 = np.hstack((o,X))
        self.y = np.dot(self.X1, self.w)
        #print("X1:", self.X1)
        #print("y:", self.y)

    def update(self, y):
        dy = y - self.y
        dw = (self.X1.T * dy).sum(1)
        dw *= self.eta
        self.w += dw

        #dy2 = np.linalg.norm(dy,2)
        #print("dy2:", dy2)
        #print("dw:", dw)

        # first draft (unvectorized)
        #x0 = self.X1[..., 0]
        #x1 = self.X1[..., 1]
        #x2 = self.X1[..., 2]
        #dy = y - self.y
        #dy2 = np.linalg.norm(dy,2)
        #print("dy2:", dy2)
        #dw0 = (x0*dy).sum() * self.eta
        #dw1 = (x1*dy).sum() * self.eta
        #dw2 = (x2*dy).sum() * self.eta
        #print([dw0, dw1, dw2])
        #self.w += [dw0, dw1, dw2]

    def __str__(self):
        return "MyPerceptron w: " + str(self.w)
 

def read_data():

    filename = 'iris.data'
    df = pd.read_csv(filename, header=None)
    print(df.head())

    # select setosa and versicolor (first 100 rows)
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)

    # extract sepal length and petal length (first, thrid column)
    X = df.iloc[0:100, [0, 2]].values

    return X, y


def plot_data(X, y, p):

    plt.scatter(X[:50, 0], X[:50, 1], \
        color='red', marker='o', label='Setosa')

    plt.scatter(X[50:100, 0], X[50:100, 1], \
        color='blue', marker='s', label='Versicolor')

    plt.xlabel('Sepal length [cm]')
    plt.ylabel('Petal length [cm]')
    plt.legend(loc='upper left')

    if p is not None:
        # draw decision boundary line
        # prediction w dot x =
        #    w0 + w1x1 + w2x2 > threshold
        threshold = .3
        b = (threshold-p.w[0]) / p.w[2]
        m = -p.w[1] / p.w[2]
        print("m:", m)
        print("b:", b)
        plt.axline((0,b), (7, m*7+b))

    plt.savefig('scatter_my_perceptron.png')


def main():
    X, y = read_data()
    print("y:", y)

    p = MyPerceptron()

    print(str(p.iteration_count) + " iterations")
    for i in range(p.iteration_count):
        p.forward(X)
        p.update(y)

    print("p.y (prediction):", p.y)

    plot_data(X, y, p)


if __name__ == '__main__':
    main()


