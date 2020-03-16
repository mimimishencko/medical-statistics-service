import pandas as pd
import numpy as np
from scipy import stats
from src.utils.interpretation_of_test import interpretation_of_test


class NormalDistTests:
    def __init__(self, data, alpha):
        self.data = data
        self.alpha = alpha

    def ks_test(self):
        # if p-value larger than 0.05 we assume normal dist
        return stats.kstest(self.data, 'norm')
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
       return stats. shapiro(self.data)


    def summary(self, test = 'shapiro'):
        res = ''
        p_value = 0
        if test == 'shapiro':
            stat, p_value = self.shapiro()
        if test == 'kolmogorov':
            stat, p_value = self.ks_test()
        if interpretation_of_test(p_value, self.alpha):
            res = f'На уровне доверия {self.alpha}, распределение близко к нормальному. В качестве центральной тенденции' \
                  f' стоит использовать среднее выборочное значение, а в качестве меры рассеяния' \
                  f' - стантартное отклонение.'
        else:
            res = f'На уровне доверия {self.alpha}, распределение не является нормальным. Среднее выборочное значение ' \
                  f'и стантартное отклонение' \
                  f'не являются показательными характеристиками. В качестве цетральной тенденции стоит использовать ' \
                  f'медиану, а в качестве меры рассеяния ' \
                  f'интерквантильный размах.'
        print(res)
        return res





