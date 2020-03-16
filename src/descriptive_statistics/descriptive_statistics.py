from collections import Counter
from itertools import takewhile
import numpy as np
from scipy import stats
import pandas as pd
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt
from src.assets.summary_dict import *
import pylab


class DescriptiveStatistics:

    def __init__(self, data, fields=None):
        if fields is None:
            fields = ['Выборочное среднее', 'Выборочная дисперсия', 'Стандартное отклонение', 'Мода', 'Медиана',
                      'Эксцесс', 'Асимметрия', 'Размах', 'Минимальное значение', 'Максимальное значение', 'Сумма',
                      'Объем выборки', 'Процентиль', 'Дециль', 'Квартиль 25', 'Квартиль 75', 'Интерквартильный размах']
        self.fields = fields
        self.data = data

        self.target_statistics = {
            "Выборочное среднее": self.sample_average(),
            "Выборочная дисперсия": self.dispersion(),
            "Стандартное отклонение": self.std(),
            "Мода": self.mode(),
            "Медиана": self.median(),
            "Эксцесс": self.excess(),
            "Асимметрия": self.assymmetry(),
            "Размах": self.sample_range(),
            "Минимальное значение": self.sample_min(),
            "Максимальное значение": self.sample_max(),
            "Сумма": self.sample_sum(),
            "Объем выборки": self.count(),
            "Процентиль": self.percentile(percent=99),
            "Дециль": self.percentile(percent=10),
            "Квартиль 25": self.percentile(percent=25),
            "Квартиль 75": self.percentile(percent=75),
            "Интерквартильный размах": self.IQS(),
        }

    def sample_average(self):
        return np.mean(self.data)

    def dispersion(self):
        n = np.size(self.data)
        average = self.sample_average()
        f = lambda x: (x - average) ** 2
        return np.sum(f(self.data)) / (n - 1)

    def std(self):
        return sqrt(self.dispersion())

    def sample_min(self):
        return np.min(self.data)

    def sample_max(self):
        return np.max(self.data)

    def sample_range(self):
        return max(self.data) - min(self.data)

    def sample_sum(self):
        return np.sum(self.data)

    def count(self):
        return np.size(self.data)

    def median(self):
        return np.median(self.data)

    def mode(self):
        counter = Counter(self.data)
        if len(counter) <= 1:
            modes = []
        else:
            mostCommon = counter.most_common()
            maxCount = mostCommon[0][1]
            modes = [t[0] for t in takewhile(lambda x: x[1] == maxCount, mostCommon)]
        return modes

    def excess(self):
        return stats.kurtosis(self.data)

    def assymmetry(self):
        return stats.skew(self.data)

    def percentile(self, percent):
        return stats.scoreatpercentile(self.data, percent)

    def IQS(self):
        return self.percentile(75)-self.percentile(25);

    def descriptive_statistics(self):
        statistics = []
        for key in self.fields:
            statistics.append(self.target_statistics[key])
        self.statistics_df = pd.DataFrame(statistics, self.fields, columns=[' '])
        return self.statistics_df

    def summary(self):
        result = []
        for index, row in self.statistics_df.iterrows():
            if index == 'Мода':
                if len(row.values[0]) == 1:
                    result.append(summary_dict['mode_uni'])
                if len(row.values[0]) > 1:
                    result.append(summary_dict['mode_muli'])
                if len(row.values[0]) == 0:
                    result.append(summary_dict['mode_none'])

            if index == 'Процентиль':
                result.append(summary_dict['percentile'] + str(row.values[0]) + '. ')

            if index == 'Дециль':
                result.append(summary_dict['decile'] + str(row.values[0]) + '. ')

            if index == 'Квартиль':
                result.append(summary_dict['quartile'] + str(row.values[0]) + '. ')

            if index == 'Асимметрия':
                str_to_append = summary_dict['assymetry'] + str(row.values[0]) + summary_dict['assymetry_conclusion']
                if row.values[0] > 0:
                    str_to_append += summary_dict['left_assymmetry']
                elif row.values[0] < 0:
                    str_to_append += summary_dict['right_assymmetry']
                else:
                    str_to_append += summary_dict['symmetric']
                result.append(str_to_append)

            if index == 'Эксцесс':
                str_to_append = ''
                if row.values[0] > 0:
                    str_to_append += summary_dict['excess_positive']
                elif 0 > row.values[0] > -3:
                    str_to_append += summary_dict['excess_negative']
                else:
                    str_to_append += summary_dict['excess_null']
                result.append(str_to_append)
        return result


class GraphicStatistics:

    def __init__(self, data, unique_filename):
        self.data = data
        self.unique_filename = unique_filename

    def histogram(self):
        sns_plot = sns.distplot(self.data, norm_hist=True)
        sns_plot.figure.savefig(f"assets/histogram-{self.unique_filename}.jpg", format='jpg')
        plt.show()

    def qq_plot(self):
        stats.probplot(self.data, dist="norm", plot=pylab)
        plt.savefig(f"assets/qq-plot-{self.unique_filename}.jpg", format='jpg')
        plt.show()

    def box_plot(self):
        plt.boxplot(self.data)
        plt.savefig(f"assets/box-plot-{self.unique_filename}.jpg", format='jpg')
        plt.show()
