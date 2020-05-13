from scipy.stats import f_oneway
import numpy as np

class Anova:
    def __init__(self):

     # add all statistics for report and critical value
    def anova_f_oneway(self, df, alpha):
        data=[]
        size_array = []
        for i in range(0, len(df.columns)-1):
            data.append(df[i].no_numpy().transpose())
            size_array.append(np.size(data[i]))
        stat, p_value = f_oneway( *data )
        print(stat, p_value, size_array)