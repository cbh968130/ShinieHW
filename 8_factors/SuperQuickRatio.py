#3.SuperQuickRatio
#超速动比率=（货币资金+交易性金融资产+应收票据+应收账款+其他应收款）/流动负债合计

def run_formula(dv):
    alpha=dv.add_formula("SuperQuickRatio_J",
                         "(monetary_cap+tradable_assets+notes_rcv+acct_rcv+other_rcv)/tot_cur_liab",
               is_quarterly=True)
    return alpha
