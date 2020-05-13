from dotenv import load_dotenv
from src.report_generator.data_methods import *
from src.descriptive_statistics.descriptive_statistics import DescriptiveStatistics, GraphicStatistics
from src.report_generator.generate_pdf import ReportGen
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
data = read_data('../test_data/body_mass.xlsx')
nonparam = NonParametricMethods()
descriptive = DescriptiveStatistics(data[0].to_numpy().transpose())
# nonparam.mann_whitney(data, 0.05, -1)
descriptive.summary(0.05)

