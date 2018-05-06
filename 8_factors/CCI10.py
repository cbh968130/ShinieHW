# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"t日顺势指标，默认10"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    10日顺势指标（10-day Commodity Channel Index），
    专门测量股价是否已超出常态分布范围。
    CCI指标波动于正无穷大到负无穷大之间，
    不会出现指标钝化现象，
    有利于投资者更好地研判行情，
    特别是那些短期内暴涨暴跌的非常态行情。
    TYP=(close+highest+lowest)/3
    MATYP=MA(TYP, N)
    DEV=sum( |TYP_i-TYPMA|, i=t-N+1, t)
    CCI=(TYP-TYPMA)/0.015/DEV
    N取10
    """
    t=params["t"]
    
    value = dv.add_formula("CCI10_J",
                           "Ta('CCI',0,open,high,low,close,volume,%s)"%t,
                           is_quarterly=False,
                           add_data=True)

    return value
