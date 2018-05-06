# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":0} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"无参数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
   成本费用利润率=利润总额/(营业成本+财务费用+销售费用+管理费用)
    """
    value = dv.add_formula("TotalProfitCostRatio_J",
                           "tot_profit/(less_oper_cost+less_fin_exp+less_selling_dist_exp+less_gerl_admin_exp)",
                           is_quarterly=True,
                           add_data=True)

    return value
