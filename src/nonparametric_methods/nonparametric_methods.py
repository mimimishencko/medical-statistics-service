from scipy import stats
from src.utils.conjugation_table import conjugation_table


class NonParametricMethods:
    def __init__(self, first_sample, second_sample):
        self.first_sample = first_sample
        self.second_sample = second_sample
        self.conj_table = conjugation_table(first_sample, second_sample)

    def wilcoxon(self):
        return stats.wilcoxon(self.first_sample, self.second_sample, )

    def mann_whitneyu(self):
        return stats.mannwhitneyu(self.first_sample, self.second_sample)

    def chi2(self):
        return stats.chi2_contingency(self.conj_table.to_numpy())
