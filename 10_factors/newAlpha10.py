# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t1":1, "t2":5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"t1日收盘价变化率与成交量变化率之积", "t2":"t2日简单移动平均"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    1日收盘价变化率与成交量变化率之积的5日简单移动平均
    """
    t1=params["t1"]
    t2=params["t2"]
    
    value = dv.add_formula('newAlpha10',
                           "Ta('SMA',0,0,0,0,-(close/Delay(close,%s)-1)*(volume/Delay(volume,%s)-1),0,%s)"%(t1,t1,t2),
                           is_quarterly=False,
                           add_data=True)
    return value
