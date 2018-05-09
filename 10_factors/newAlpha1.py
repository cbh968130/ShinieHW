# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":1} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"收盘价t日变化率与成交量t日变化率乘积的相反数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
   收盘价1日变化率与成交量1日变化率乘积的相反数
    """
    t=params["t"]
    
    value = dv.add_formula('newAlpha1', '-(close/Delay(close,%s)-1)*(volume/Delay(volume,%s)-1)'%(t,t),
                           is_quarterly=False,
                           add_data=True)

    return value
