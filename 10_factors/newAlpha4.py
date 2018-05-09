# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":0} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"无参数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
   净利润（TTM）/负债合计（Mean）
    """
    value = dv.add_formula('newAlpha4','TTM(net_profit)/Ts_Mean(total_liab,4)',
                           is_quarterly=True,
                           add_data=True)

    return value
