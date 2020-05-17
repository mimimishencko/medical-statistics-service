import csv
import os
import pandas as pd
import numpy as np
from random import randint


def read_data_excel(result_path='DATA_PATH'):
    if result_path == 'DATA_PATH':
        path = os.getenv('DATA_PATH')
    else:
        path = result_path
    df = pd.read_excel(path, header=None)

    return df

def read_data_csv(result_path='DATA_PATH'):
    if result_path == 'DATA_PATH':
        path = os.getenv('DATA_PATH')
    else:
        path = result_path
    df = pd.read_excel(path, header=None)

    return df


def write_data(df, result_path='RESULT_PATH'):
    if result_path == 'RESULT_PATH':
        path = os.getenv('RESULT_PATH')
    else:
        path = result_path
    df.to_csv(path)


def generate_data(N):
    data_second = [i for i in range(N)]
    with open('../test_data/test_data_2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for row in data_second:
            writer.writerow([randint(-1000, 1000)])
