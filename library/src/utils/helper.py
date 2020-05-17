from src.nonparametric_methods.nonparametric_methods import NonParametricMethods
from src.descriptive_statistics.descriptive_statistics import DescriptiveStatistics, GraphicStatistics
from src.report_generator.generate_pdf import ReportGen
from src.normal_dist_test.normal_dist_test import NormalDistTests
from src.parametrical_statistics.parametrical_statistics import ParametricMethods


class Helper:

    def __init__(self):
        # self.data = data
        self.parametric = ParametricMethods()
        self.non_parametric = NonParametricMethods()
        self.norm_dist_tests = NormalDistTests()
        # self.descriptive = DescriptiveStatistics(data)

    def helper(self, data, helper_data):
        data_array = []
        normality_array = []
        for column in data:
            data_array.append(data[column].to_numpy().transpose())
            normality_array.append(self.norm_dist_tests.normality_check(data))
        print(data_array, normality_array)
        expected, is_independent, sample_count, sample_size_equal, alpha, continues = self.parse_answers(helper_data)
        all_normal = all(normality_array)
        print('helper_parse', expected, is_independent, sample_count, sample_size_equal, alpha, continues)
        if all(normality_array):
            self.parametric.test(data, is_independent=is_independent, alpha=alpha, expected=expected)
        return data_array, normality_array

    def parse_answers(self, helper_data):
        expected = 0
        is_independent = True
        alpha = 0.05
        sample_count = 0
        sample_size_equal = True
        continues = True

        for answer in helper_data:
            if answer["question_code_name"] == "sample_count":
                if answer["answer_id"] == 1:
                    sample_count = 1
                    # вызвать описательную статистику для выборки
                    print('descriptive')
                    return
                elif answer["answer_id"] == 2:
                    sample_count = 2
                else:
                    sample_count = 3
            if answer["question_code_name"] == "sample_size_equal":
                if answer["answer_id"] == 1:
                    sample_size_equal = True
                else:
                    sample_size_equal = False
            if answer["question_code_name"] == "analysis_goal":
                if answer["answer_id"] == 1:
                    # вызвать описательную статистику для каждой выборки
                    print('descriptive')
                    return
            if answer["question_code_name"] == "independent_two_samples":
                if answer["answer_id"] == 1:
                    is_independent = False
                else:
                    is_independent = True
            if answer["question_code_name"] == "independent_more_samples":
                if answer["answer_id"] == 1:
                    is_independent = False
                else:
                    is_independent = True
            if answer["question_code_name"] == "data_type":
                if answer['answer_id'] == 1:
                    continues = True
                else:
                    continues = False
            if answer["question_code_name"] == "experiment_result":
                if answer['answer_id'] == 1:
                    expected = 0
                elif answer['answer_id'] == 2:
                    expected = 1
                else:
                    expected = -1
            if answer["question_code_name"] == "need_descriptive":
                if answer['answer_id'] == 1:
                    # вызвать описательную статистику для каждой выборки
                    print('descriptive')
            if answer["question_code_name"] == "significance_level":
                if answer["answer_id"] == 1:
                    alpha = 0.1
                elif answer["answer_id"] == 2:
                    alpha = 0.05
                else:
                    alpha = 0.01

        return expected, is_independent, sample_count, sample_size_equal, alpha, continues
