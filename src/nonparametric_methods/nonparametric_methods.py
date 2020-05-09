from scipy import stats
from src.utils.conjugation_table import conjugation_table
from src.data_methods.generate_pdf import ReportGen
from src.critical_tables import *
import pandas as pd
import numpy as np


class NonParametricMethods:
    def __init__(self, first_sample=None, second_sample=None):
        if second_sample is None:
            second_sample = []
        if first_sample is None:
            first_sample = []
        self.first_sample = first_sample
        self.second_sample = second_sample
        self.conj_table = conjugation_table(first_sample, second_sample)
        self.chi2_critical = chi_square_table.ChiCriticalTable()
        self.report_generator = ReportGen()


    def wilcoxon(self):
        df = pd.DataFrame({'before': self.first_sample, 'after': self.second_sample,
                           'difference': self.first_sample - self.second_sample,
                           'abs_diff': abs(self.first_sample - self.second_sample)})
        sorted_differences = np.sort(df['abs_diff'])
        ranges = np.empty(np.shape(sorted_differences))
        i = 0
        for value in df['abs_diff']:
            ranges[i] = (int(np.where(sorted_differences == value)[0] + 1))
            i += 1
        df['ranges'] = ranges

        for key, item in df['difference'].iteritems():
            if item < 0:
                df['ranges'][key] *= -1

        W_obs = df['ranges'].sum()

        n = np.size(self.first_sample)
        critical, alpha = wilcoxon_table.get_value(n)
        return W_obs, df, n, critical, alpha

    def mann_whitney(self):
        return stats.mannwhitneyu(self.first_sample, self.second_sample)

    def chi2(self):
        return stats.chi2_contingency(self.conj_table.to_numpy())

    def friedman(self, *args):
        alpha = args[-1]
        args = args[0:-1]
        k = len(args)
        n = np.size(args[0])
        df = pd.DataFrame(index=range(1, n+1), columns=range(1, len(args)+1))
        index = 1
        for arg in args:
            df[index] = arg
            index += 1

        index = 0
        ranges = np.zeros((n, k))

        sorted_array = np.zeros((n, k))
        for row in df.iterrows():
            sorted_array[index] = np.sort(df.loc[index+1])
            index += 1

        for i in range(n):
            for j in range(k):
                row, col = np.where(sorted_array == df.loc[i+1][j+1])
                ranges[i][j] = col[0] + 1
        df_ranges = pd.DataFrame(ranges, index=range(1, n+1), columns=range(1, len(args)+1))
        print(df_ranges)
        sum_col = np.zeros(k, dtype=int)
        i = 0
        for col in df_ranges:
            sum_col[i] = df_ranges[col].sum()
            i += 1

        chi = 12 / (n * k * (k + 1)) * np.sum((sum_col - n * (k + 1) / 2) ** 2)
        if (k == 3 and n <= 15) or (k == 4 and n <= 8):
            critical1, p1 = fridman_table.get_value(n, k)
            p_value = p1

        else:
            p1 = alpha
            degree_of_freedom = k - 1
            critical1 = self.chi2_critical.get_value(p1, degree_of_freedom)
            stat, p_value = stats.friedmanchisquare(*(args[i] for i in range(len(args))))
        self.report_generator.for_friedman(chi, critical1, p1,  df, df_ranges, n, k, format(p_value, '.4f'), alpha)

