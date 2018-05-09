# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t1":1, "t2":5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"t1日收益率", "t2":"过去t2日成交量标准差"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
   1日收益率与过去5日成交量标准差之积
    """
    t1=params["t1"]
    t2=params["t2"]
    
    value = dv.add_formula('newAlpha8',
                           '(close_adj/Delay(close_adj,%s)-1)*StdDev(volume,%s)'%(t1,t2),
                           is_quarterly=False,
                           add_data=True)

    return value
