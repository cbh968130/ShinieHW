#5.CCI10

def run_formula(dv):
    alpha=dv.add_formula("CCI10_J",
                   "Ta('CCI',0,open,high,low,close,volume,10)",
                   is_quarterly=False)
    return alpha
