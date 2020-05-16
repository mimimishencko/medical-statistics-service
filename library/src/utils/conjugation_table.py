import numpy as np
import pandas as pd


def conjugation_table(first_sample, second_sample):
    df = pd.DataFrame({'first': first_sample, 'second': second_sample})
    conj_table = pd.crosstab(df['first'], df['second'])
    return conj_table



first = np.array([1, 0, 0, 0, 1, 0, 1, 0])
second = np.array(['m', 'f', 'm', 'f', 'f', 'm', 'm', 'f'])
conjugation_table(first, second)