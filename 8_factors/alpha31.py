#6.alpha31
#(CLOSE-MEAN(CLOSE,12))/MEAN(CLOSE,12)*100

def run_formula(dv):
    alpha=dv.add_formula("alpha31",
                         "(close-Ts_Mean(close,12))/Ts_Mean(close,12)*100",
                         is_quarterly=False)
    return alpha
