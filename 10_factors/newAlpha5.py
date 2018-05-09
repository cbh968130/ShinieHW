# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":90} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"90日收益率的标准差"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    ROE/90日收益率的标准差
    """
    Ret_adj=dv.add_formula("Ret_adj","close_adj/Delay(close_adj,1)-1",
                       is_quarterly=False,
                       add_data=True)
    
    value = dv.add_formula('newAlpha5','TTM(net_profit)/Ts_Mean(tot_assets,4)/StdDev(Ret_adj,90)',
                           is_quarterly=True,
                           add_data=True)

    return value
