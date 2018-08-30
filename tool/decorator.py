import sklearn.utils
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def shuffle(data):
    return sklearn.utils.shuffle(data, random_state=1031)


def series_plot(series_, grid=False):
    series_.plot(grid=grid)
    plt.show()


def series_distribution(series_, grid=False):
    series_.hist(grid=grid)
    plt.show()


def print_to_file(file_name, list_):
    np.set_printoptions(threshold=np.inf)
    f = open(file_name, 'w')
    print(list_, file=f)


if __name__ == '__main__':
    series_distribution(pd.Series([10, 21, 31, np.nan, 12, 22, 32, 13, 23, 33]))
