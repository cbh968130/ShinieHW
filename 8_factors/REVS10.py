#4.REVS10
#revs10=close_t/close_t-10

def run_formula(dv):
    alpha=dv.add_formula("REVS10_J",
                         "close/Delay(close,10)",
                         is_quarterly=False)
    return alpha
