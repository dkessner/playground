#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Perceptron:

    def __init__(self, n, eta=.01, iteration_count=5):
        self.eta = eta
        self.iteration_count = iteration_count

        print("dimension:", n)
        seed = 1
        generator = np.random.RandomState(seed)
        self.w_ = generator.normal(loc=0, scale=.01, size=n)
        self.b_ = np.float_(0)
        

    def fit(self, X, y):

        self.error_counts_ = []
        #print("y:", y)

        for _ in range(self.iteration_count):
            error_count = 0
            for xi, target in zip(X, y):
                dw = self.eta * (target - self.predict(xi))
                self.w_ += dw * xi
                self.b_ += dw
                error_count += int(dw != 0.0)
            self.error_counts_.append(error_count)
            #print("y_predicted:", self.predict(X))
            print("error_count:", error_count)

    def output(self, X):
        return np.dot(X, self.w_) + self.b_

    def predict(self, X):
        return np.where(self.output(X) >= 0, 1, 0)


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

    # draw decision boundary line
    b = -p.b_ / p.w_[1]
    m = -p.w_[0] / p.w_[1]
    print("m:", m)
    print("b:", b)
    plt.axline((0,b), (7, m*7+b))

    plt.savefig('scatter.png')




def main():
    X, y = read_data()
    #print("X:", X)
    #print("y:", y)

    p = Perceptron(X.shape[1])
    p.fit(X, y)

    plot_data(X, y, p)

if __name__ == '__main__':
    main()

