from dotenv import load_dotenv
from src.nonparametric_methods.nonparametric_methods import NonParametricMethods
import os
import numpy as np

np.set_printoptions(suppress=True)
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.normpath(os.path.join(BASE_DIR, '../'))


# data1 = read_data()
# data = read_data('../test_data/body_mass.xlsx')
nonparam = NonParametricMethods()
# descriptive = DescriptiveStatistics(data[0].to_numpy().transpose())
# nonparam.mann_whitney(data, 0.05, -1)
# descriptive.summary(0.05)
data1 = np.array([93.2, 98.2, 105.6, 86.8, 95.5])
data2 = np.array([88.9, 94.5, 106.1, 84.3, 92.5])
nonparam.wilcoxon(data1, data2)