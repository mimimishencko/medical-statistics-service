import pandas as pd
from scipy.stats import chi2

# chi_table = None
# class ChiCriticalTable:
#     def __init__(self):
#         self.chi2_table = pd.read_csv('../resources/chi2_table.csv', index_col=0)

def get_value( p, df):
    return chi2.ppf(p, df)
