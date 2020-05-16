import pandas as pd

n = [5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19,
     20, 20, 20]
W = [15, 21, 19, 28, 24, 32, 28, 39, 33, 45, 39, 52, 44, 58, 50, 65, 57, 73, 63, 80, 70, 88, 76, 97, 83, 105, 91, 114,
     98, 124, 106]
alpha = [0.062, 0.032, 0.062, 0.016, 0.046, 0.024, 0.054, 0.020, 0.054, 0.020, 0.048, 0.018, 0.054, 0.020, 0.052, 0.022,
         0.048, 0.020,
         0.050, 0.022, 0.048, 0.022, 0.050, 0.020, 0.050, 0.020, 0.048, 0.020, 0.050, 0.020, 0.048]
wilcoxon_critical_values = pd.DataFrame({'n': n, 'W': W, 'alpha': alpha}, index=None)


def get_value(num):
    values = wilcoxon_critical_values.loc[wilcoxon_critical_values['n'] == num]
    return values.loc[values['alpha'] == values['alpha'].min(), 'W'].item(),\
           values.loc[values['alpha'] == values['alpha'].min(), 'alpha'].item()
