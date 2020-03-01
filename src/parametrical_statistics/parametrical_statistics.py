from scipy import stats
import numpy as np
from math import sqrt
from scipy import stats

# from src.utils.interpretation_of_tests import interpretation_of_test
from src.utils.interpretation_of_tests import interpretation_of_test


class ParametricStatistics:

    def __init__(self, first_sample, second_sample, alpha, is_independent):
        self.first_sample = first_sample
        self.second_sample = second_sample
        self.alpha = alpha
        self.is_independent = is_independent

    def welch_test(self):
        # mean1, mean2 = np.mean(self.first_sample), np.mean(self.second_sample)
        # std1, std2 = np.std(self.first_sample, ddof=1), np.std(self.second_sample, ddof=1)
        # print(std1, std2)
        # n1, n2 = len(self.first_sample), len(self.second_sample)
        # se1, se2 = std1 / sqrt(n1), std2 / sqrt(n2)
        # sed = sqrt(se1 ** 2.0 + se2 ** 2.0)
        # t_stat = (mean1 - mean2) / sed
        # df = n1 + n2 - 2
        # cv = stats.t.ppf(1.0 - self.alpha, df)
        # p = (1 - stats.t.cdf(abs(t_stat), df)) * 2
        # print(t_stat, cv, p)
        return stats.ttest_ind(self.first_sample, self.second_sample, equal_var=False)

    def student_ind(self):
        stats.ttest_ind(self.first_sample, self.second_sample)

    def student_rel(self):
        stats.ttest_rel(self.first_sample, self.second_sample)

    def test(self):
        res=''
        if np.std(self.first_sample, ddof=1) != np.std(self.second_sample, ddof=1):
            stat, p_value = self.welch_test()
            if interpretation_of_test(p_value, self.alpha):
                res = f'На уровне значимости {self.alpha},' \
                      f' нет оснований отвергать гипотезу о том, что средние значения отличаются'
            else:
                res = f'На уровне значимости {self.alpha}, гипотеза о равенстве средних отвергается'

                #         how to validate if samples are independent

        print(res)





