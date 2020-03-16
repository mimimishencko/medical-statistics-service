from scipy.stats import norm


def z_criterium(x):
    return norm.cdf(x)


print(z_criterium(1.40))
