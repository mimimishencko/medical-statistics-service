import pandas as pd

chi_table = None
class ChiCriticalTable:
    def __init__(self):
        self.chi2_table = pd.read_csv('../resources/chi2_table.csv', index_col=0)
    def get_value(self, p, df):
        return float(self.chi2_table.loc[str(df)][str(p)])
