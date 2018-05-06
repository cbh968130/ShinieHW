# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈熙元" # 这里填下你的名字
default_params = {"t1":10, "t2":6} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"t1日价格平均线", "t2":"t2日线性回归"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    10日价格平均线N日线性回归系数。
    取近N个交易日的对应MA值，
    对N个周期的序数进行普通最小二乘线性回归，
    取股价关于周期序数的系数。
    MA(close, N)=a+bt+e
    b即为MA10RegressCoeff。
    N取6日。
    """
    t1=params["t1"]
    t2=params["t2"]
    
    value = dv.add_formula("MA10RegressCoeff6_J",
                           "Ta('LINEARREG_SLOPE',0,0,0,0,Ta('SMA',0,0,0,0,close,0,%s),0,%s)"%(t1,t2),
                           is_quarterly=False,
                           add_data=True)

    return value
