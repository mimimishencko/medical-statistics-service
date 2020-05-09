from dotenv import load_dotenv
from src.data_methods.data_methods import *
from src.descriptive_statistics.descriptive_statistics import DescriptiveStatistics, GraphicStatistics
from src.data_methods.generate_pdf import ReportGen
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
# unique_filename2 = str(uuid.uuid4())
#
# print(data1[0:100])
# # stat2 = DescriptiveStatistics(data=data2)
#
# # graphic2 = GraphicStatistics(data2, unique_filename2)
#
# # normal_test2 = NormalDistTests(data=data2, alpha=0.05)
#
# pd.set_option('display.float_format', lambda x: '%.3f' % x)
#
# # normal_test2.summary()
# # normal_test2.shapiro()
#
# # parametric_tests = ParametricMethods(data1[0:100], data2, 0.01, is_independent=True)
# # parametric_tests.test()
#
#

# #
# # graphic2.histogram()
# # graphic2.qq_plot()
# # graphic2.box_plot()
# generate_pdf(stat1.descriptive_statistics(), stat1.summary(), unique_filename1, distr_summary)
# generate_pdf(stat2.descriptive_statistics(), stat2.summary(), unique_filename2)

# data1 = np.array([93.2, 98.2, 105.6, 86.8, 95.5])
# data2 = np.array([88.9, 94.5, 106.1, 84.3, 92.5])

# d1 = np.array([193, 206, 188, 375, 204, 287, 221, 216, 195, 231])
# d2 = np.array([217, 214, 197, 412, 199, 310, 215, 223, 208, 224])
# d3 = np.array([191, 293, 181, 400, 211, 304, 213, 207, 186, 227])
# d4 = np.array([149, 169, 145, 306, 170, 243, 158, 155, 144, 172])
# d5 = np.array([202, 189, 192, 387, 196, 312, 232, 209, 200, 218])
# d6 = np.array([127, 130, 128, 230, 132, 198, 135, 124, 129, 125])
# stat1 = DescriptiveStatistics(data=d1)

d1=np.array([22.2, 17., 14.1, 17])
d2=np.array([5.4, 6.3, 8.5, 10.7])
d3=np.array([10.6, 6.2, 9.3, 12.3])
non_parametric = NonParametricMethods()
non_parametric.friedman(d1, d2, d3, 0.05)
# W_obs, df, n, critical, alpha = non_parametric.wilcoxon()


# normal_test1 = NormalDistTests(data=d1, alpha=0.05)
# distr_summary = normal_test1.summary()
# graphic1 = GraphicStatistics(d1, unique_filename1)
# graphic1.histogram()
# graphic1.qq_plot()
# graphic1.box_plot()
#
# report_generator.for_descriptive(stat1.descriptive_statistics(), stat1.summary(), unique_filename1, distr_summary)
