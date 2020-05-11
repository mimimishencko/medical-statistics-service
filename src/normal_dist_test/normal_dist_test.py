import pandas as pd
import numpy as np
from scipy import stats
from src.utils.interpretation_of_test import interpretation_of_test


class NormalDistTests:

    def ks_test(self, data):
        # if p-value larger than 0.05 we assume normal dist
        return stats.kstest(data, 'norm')
        # sort_data = np.sort(self.data)
        # N = np.size(self.data)
        # i = np.arange(1, N+1, 1)
        # D_plus = max(i / N - sort_data)
        # print('D_plus ', D_plus)
        # D_minus = max(sort_data - (i - 1) / N)
        # print('D_minus', D_minus)
        # D = max(D_plus, D_minus)
        # print(D)

    def shapiro(self, data):
        # if p-value lager than 0.05 assume normal
        return stats.shapiro(data)

    def summary(self, data, alpha, test='shapiro'):
        res = [0, 0, 0]
        p_value = 0
        if test == 'shapiro':
            stat, p_value = self.shapiro(data)
            res[1] = format(stat, '.4f')
            res[2] = format(p_value, '.4f')
        if test == 'kolmogorov':
            stat, p_value = self.ks_test(data)
            res[1] = format(stat, '.4f')
            res[2] = format(p_value, '.4f')
        if interpretation_of_test(p_value, alpha):
            res[
                0] = f'На уровне значимости {alpha}, распределение близко к нормальному. В качестве меры центральной ' \
                     f'тенденции' \
                     f' стоит использовать среднее выборочное значение, а в качестве меры рассеяния' \
                     f' - стантартное отклонение.'
        else:
            res[0] = f'На уровне значимости {alpha}, распределение не является нормальным. Среднее выборочное значение ' \
                     f'и стантартное отклонение' \
                     f'не являются показательными характеристиками. В качестве цетральной тенденции стоит использовать ' \
                     f'медиану, а в качестве меры рассеяния ' \
                     f'интерквантильный размах.'
        print(res)
        return res
