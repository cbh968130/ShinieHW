# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"过去t天的价格动量"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    过去10天的价格动量。
    REVS10=close_t/close_t-10
    注1：若公司在过去10天有停牌，停牌日也计算在统计天数中。
    注2：若公司在今天停牌，不计算该因子的值。
    """
    t=params["t"]
    
    value = dv.add_formula("REVS10_J",
                           "close/Delay(close,%s)"%t,
                           is_quarterly=False,
                           add_data=True)

    return value
