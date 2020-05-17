import pandas as pd
from statistics import variance
import numpy as np
from scipy import stats
from src.utils.interpretation_of_test import interpretation_of_test


class NormalDistTests:

    def ks_test(self, data):
        return stats.kstest(data, 'norm')

    def shapiro(self, data):
        # if p-value lager than 0.05 assume normal
        # n = np.size(data)
        # m = n // 2
        # print(m)
        # B = 0
        # a0 = 0.899 / ((n - 2.4) ** 0.4162) - 0.02
        # for j in range(1, m):
        #     z = (n - 2 * j + 1) / (n - 0.5)
        #     a = a0 * (z + 1483 / ((3 - z) ** 10.845) + (71.6 * 10 ** (-10)) / ((1.1 - z) ** 8.26))
        #     B += a * (data[n - j] - data[j])
        # W = (1 - 0.6695 / (n ** 0.6518)) * np.var(data) / (B ** 2)
        # print(W)

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
                     f' - стандартное отклонение.'
        else:
            res[0] = f'На уровне значимости {alpha}, распределение не является нормальным. Среднее выборочное значение ' \
                     f'и стандартное отклонение' \
                     f' не являются показательными характеристиками. В качестве цетральной тенденции стоит использовать ' \
                     f'медиану, а в качестве меры рассеяния ' \
                     f'интерквантильный размах.'
        print(res)
        return res

    def normality_check(self, data):
        stat, p_value = self.shapiro(data)
        return interpretation_of_test(p_value, 0.05)
