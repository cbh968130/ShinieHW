#1.alpha16
#(-1 * TSMAX(RANK(CORR(RANK(VOLUME), RANK(VWAP), 5)), 5))

def run_formula(dv):
    alpha=dv.add_formula("alpha16",
                         "-1*Ts_Max(Correlation(volume,vwap,5),5)",
                         is_quarterly=False)
    return alpha
