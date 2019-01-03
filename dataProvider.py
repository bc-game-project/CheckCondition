#coding=utf-8

import os
import pandas as pd


def load_csv_data(path, file):
    '''
    :param path: path of data to be checked
    :param file: file name
    :return: array
    '''
    file_path = os.path.join(path, file)
    data = pd.read_csv(file_path, header = None)
    return data.values[:,1]


