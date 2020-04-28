import pandas as pd

n_k3 = [3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
chi_k3 = [6, 6.5, 8, 5.2, 6.4, 8.4, 5.33, 6.33, 9., 6,
          8.86, 6.25, 9., 6.22, 6.2, 8.6, 6.54, 8.91, 6.17, 8.67, 6., 8.67, 6.14, 9., 6.4, 8.93]
p_k3 = [0.028, 0.042, 0.005, 0.093, 0.039, 0.008, 0.072,
        0.052, 0.008, 0.051, 0.008, 0.047, 0.010, 0.048, 0.046, 0.012, 0.043, 0.011, 0.050, 0.011, 0.050, 0.012, 0.049,
        0.010, 0.047, 0.010]
n_k4 = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8]

chi_k4 = [6., 7., 8.2, 7.5, 9.3, 7.8, 9.96, 7.6, 10.2, 7.63, 10.37, 7.65, 10.35, 8.67]
p_k4 = [0.042, 0.054, 0.017, 0.054, 0.011, 0.049, 0.009, 0.043, 0.010, 0.051, 0.009, 0.049, 0.010, 0.010]

friedman_k_3 = pd.DataFrame({'n': n_k3, 'chi': chi_k3, 'p': p_k3}, index=None)
friedman_k_4 = pd.DataFrame({'n': n_k4, 'chi': chi_k4, 'p': p_k4}, index=None)


def get_value(n, k):
    values = pd.DataFrame()
    print(n, k)
    if k == 3:
        values = friedman_k_3.loc[friedman_k_3['n'] == n]
        print(values)
    if k == 4:
        values = friedman_k_4.loc[friedman_k_4['n'] == n]

    return values.loc[values['p'] == values['p'].max(), 'chi'].item(), \
           values.loc[values['p'] == values['p'].max(), 'p'].item()
