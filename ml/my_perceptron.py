#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
        b = -p.b_ / p.w_[1]
        m = -p.w_[0] / p.w_[1]
        print("m:", m)
        print("b:", b)
        plt.axline((0,b), (7, m*7+b))

    plt.savefig('blah.png')


def main():
    X, y = read_data()
    plot_data(X, y, None)


if __name__ == '__main__':
    main()


