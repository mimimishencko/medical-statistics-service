from scipy import stats
import numpy as np
from math import sqrt
from scipy import stats
import pandas as pd
from src.utils.interpretation_of_test import interpretation_of_test
from src.report_generator.generate_pdf import ReportGen
from src.critical_tables import student_table


class ParametricMethods:

    def __init__(self):
        self.report_generator = ReportGen()

    def welch_test(self, first_sample, second_sample):
        statistic, p_value = stats.ttest_ind(first_sample, second_sample, equal_var=False)
        return statistic, p_value

    def student_ind(self, first_sample, second_sample):
        return stats.ttest_ind(first_sample, second_sample)

    def student_rel(self, first_sample, second_sample):

        return stats.ttest_rel(first_sample, second_sample)

    def test(self, df, is_independent, alpha, expected):
        test = ['', '']
        critical = 0
        p_value = 0
        stat = 0

        first_sample = df[0].to_numpy().transpose()
        second_sample = df[1].to_numpy().transpose()

        n = np.size(first_sample)
        k = 2

        if np.std(first_sample, ddof=1) != np.std(second_sample, ddof=1):
            if is_independent:
                test[0] = 'критерия Уэлча'
                test[1] = 'Сравнение проведено с помощью критерия Уэлча, так как выборки независимы и дисперсии не ' \
                          'равны. '
                stat, p_value = self.welch_test(first_sample, second_sample)

        else:
            if is_independent:
                test[0] = 'двухвыборочного критерия Стьюдента'
                test[1] = 'Сравнение проведено с помощью двухвыборочного критерия Стьюдента, так как выборки ' \
                          'независимы. '
                stat, p_value = self.student_ind(first_sample, second_sample)
            else:
                test[0] = 'парного критерия Стьюдента'
                test[1] = 'Сравнение проведено с помощью парного критерия Стьюдента, так как выборки зависимы.'
                stat, p_value = self.student_rel(first_sample, second_sample)
        if expected == -1:
            critical = student_table.get_value(1 - alpha, np.size(first_sample) + np.size(second_sample) - 2)
        elif expected == 1:
            critical = student_table.get_value(alpha, np.size(first_sample) + np.size(second_sample) - 2)
        elif expected == 0:
            critical = student_table.get_value(1 - alpha / 2, np.size(first_sample) + np.size(second_sample) - 2)
        if expected != 0:
            p_value = p_value / 2
        df = pd.DataFrame({1:df[0], 2:df[1]}, index=range(1, len(df[0].tolist())))
        self.report_generator.for_student(format(stat, '.4f'), format(critical, '.4f'), df.head(20), n, k,
                                          format(p_value, '.4f'), alpha, test, is_independent, expected)
