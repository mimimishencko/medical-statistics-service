from scipy.stats import norm


def get_value(x):
    return norm.cdf(x)

