#!/usr/bin/env python


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class MyPerceptron:

    def __init__(self):
        self.eta = .01
        self.iteration_count = 3

        generator = np.random.RandomState(1)
        self.w = generator.normal(loc=0, scale=.01, size=3)

    def forward(self, X):
        o = np.ones((len(X),1))
        self.X1 = np.hstack((X,o))
        print("X1:", self.X1)
        self.y = np.dot(self.X1, self.w)
        print("y:", self.y)

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
        b = -p.w[0] / p.w[2]
        m = -p.w[1] / p.w[2]
        print("m:", m)
        print("b:", b)
        plt.axline((0,b), (7, m*7+b))

    plt.savefig('blah.png')


def main():
    X, y = read_data()

    p = MyPerceptron()
    print(p)

    p.forward(X)

    plot_data(X, y, p)


if __name__ == '__main__':
    main()


