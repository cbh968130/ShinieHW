#7.ChandeSU
#20日内max(close_i-close_i-1,0)加总

def run_formula(dv):
    alpha=dv.add_formula("ChandeSU_J","Ts_Sum(Max(close-Delay(close,1),0),20)",is_quarterly=False)
    return alpha
