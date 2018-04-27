#8.MA10RegressCoeff6

import pandas as pd
import numpy as np

def run_formula(dv):
    df=dv.get_ts('close')
    m=10
    n=6
    t=np.arange(1,n+1) #周期序数
    var=np.cov(t,t)[0][0]
    ma=pd.rolling_mean(df,m) #计算MA
    rd=pd.DataFrame(index=df.index,columns=df.columns) #要输出的df
    l=len(df.index) #日期长度
    for k in df.columns:
        s=ma[k]
        rs=pd.Series(index=df.index)
        for i in np.arange(m+n-2,l):
            rs[rs.index[i]]=np.cov(s[s.index[i-5:i+1]],t)[0][1]/var #得到beta
        rd[k]=rs
    return rd
