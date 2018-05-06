# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t1":5, "t2":5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"t1日成交量和成交均价的相关系数", "t2":"过去t2天的最大值"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    (-1 * TSMAX(RANK(CORR(RANK(VOLUME), RANK(VWAP), 5)), 5))
    """
    t1=params["t1"]
    t2=params["t2"]
    
    value = dv.add_formula("alpha16",
                           "-1*Ts_Max(Correlation(volume,vwap,%s),%s)"%(t1,t2),
                           is_quarterly=False,
                           add_data=True)

    return value
