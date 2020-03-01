import pandas as pd
import numpy as np
from scipy import stats


class NormalDistTests:
    def __init__(self, data, p_value):
        self.data = data
        self.p_value = p_value

    def ks_test(self):
        # if p-value larger than 0.05 we assume normal dist
        print('kstest: ', stats.kstest(self.data, 'norm'))
        # sort_data = np.sort(self.data)
        # N = np.size(self.data)
        # i = np.arange(1, N+1, 1)
        # D_plus = max(i / N - sort_data)
        # print('D_plus ', D_plus)
        # D_minus = max(sort_data - (i - 1) / N)
        # print('D_minus', D_minus)
        # D = max(D_plus, D_minus)
        # print(D)

    def shapiro(self):
        # if p-value lager than 0.05 assume normal
        print('shapiro-uilk: ', stats. shapiro(self.data))




