# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":20} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"t日ChandeSU"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    计算CMO因子的中间变量。
    SU是今日收盘价与昨日收盘价（上涨日）差值加总。
    若当日下跌，则增加值为0。
    SU=sum(max(close_i-close_i-1, 0), i=t-N+1, t)
    N取20
    """
    t=params["t"]
    
    value = dv.add_formula("ChandeSU_J",
                           "Ts_Sum(Max(close-Delay(close,1),0),%s)"%t,
                           is_quarterly=False,
                           add_data=True)

    return value
