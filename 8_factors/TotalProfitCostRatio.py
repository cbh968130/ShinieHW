#2.TotalProfitCostRatio
#成本费用利润率=利润总额/(营业成本+财务费用+销售费用+管理费用)

def run_formula(dv):
    alpha=dv.add_formula("TotalProfitCostRatio_J","tot_profit/(less_oper_cost+less_fin_exp+less_selling_dist_exp+less_gerl_admin_exp)",
               is_quarterly=True,add_data=True)
    return alpha
