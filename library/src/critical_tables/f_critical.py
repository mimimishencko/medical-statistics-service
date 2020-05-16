from scipy.stats import f

def get_value(p, dfn, dfm):
    print(f.cdf(p, dfn, dfm))

get_value(0.95, 15, 2)
