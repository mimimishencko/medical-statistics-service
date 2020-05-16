from scipy.stats import t


def get_value(p, df):
    value = t.ppf(p, df)
    return value

