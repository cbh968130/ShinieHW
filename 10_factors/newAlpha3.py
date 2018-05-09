# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t":1} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t":"毛利率t期变化率"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    毛利率1期变化率
    """
    t=params["t"]

    gross_profit_ttm=dv.add_formula('gross_profit_ttm','TTM(oper_rev-less_oper_cost)',
                                    is_quarterly=True,
                                    add_data=True)
    
    value = dv.add_formula('newAlpha3','gross_profit_ttm/Delay(gross_profit_ttm,1)-1',
                           is_quarterly=True,
                           add_data=True)

    return value
