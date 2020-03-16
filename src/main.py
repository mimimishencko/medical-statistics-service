from dotenv import load_dotenv
from src.data_methods.data_methods import *
from src.descriptive_statistics.descriptive_statistics import DescriptiveStatistics, GraphicStatistics
from src.data_methods.generate_pdf import generate_pdf
from src.normal_dist_test.normal_dist_test import NormalDistTests
from src.parametrical_statistics.parametrical_statistics import ParametricMethods
from src.nonparametric_methods.nonparametric_methods import NonParametricMethods
import os
import numpy as np
import uuid

np.set_printoptions(suppress=True)
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.normpath(os.path.join(BASE_DIR, '../'))


# data1 = read_data()
# data2 = read_data('../test_data/test_data_2.csv')
#
# unique_filename1 = str(uuid.uuid4())
# # unique_filename2 = str(uuid.uuid4())
#
# stat1 = DescriptiveStatistics(data=data1[0:100])
# print(data1[0:100])
# # stat2 = DescriptiveStatistics(data=data2)
#
# graphic1 = GraphicStatistics(data1, unique_filename1)
# # graphic2 = GraphicStatistics(data2, unique_filename2)
#
# normal_test1 = NormalDistTests(data=data1[0:100], alpha=0.05)
# # normal_test2 = NormalDistTests(data=data2, alpha=0.05)
#
# pd.set_option('display.float_format', lambda x: '%.3f' % x)
# distr_summary = normal_test1.summary()
#
# # normal_test2.summary()
# # normal_test2.shapiro()
#
# # parametric_tests = ParametricMethods(data1[0:100], data2, 0.01, is_independent=True)
# # parametric_tests.test()
#
#
# graphic1.histogram()
# graphic1.qq_plot()
# graphic1.box_plot()
# #
# # graphic2.histogram()
# # graphic2.qq_plot()
# # graphic2.box_plot()
# generate_pdf(stat1.descriptive_statistics(), stat1.summary(), unique_filename1, distr_summary)
# generate_pdf(stat2.descriptive_statistics(), stat2.summary(), unique_filename2)

data1 = np.array([93.2, 98.2, 105.6, 86.8, 95.5])
data2 = np.array([88.9, 94.5, 106.1, 84.3, 92.5])

non_parametric = NonParametricMethods(data1, data2)
print(non_parametric.wilcoxon())

