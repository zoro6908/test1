import pandas as pd
import numpy as np

# d={'odd':np.arange(1,100,2), 'even':np.arange(0,100,2)}
# print(d['odd'])
# print(d['even'])
# df=pd.DataFrame(d)
# print(df.groupby('odd').groups)

# world_cup={'Team':['West Indies', 'India', 'Australia', 'Pakistan', 'Sri Lanka'],
#            'Rank':[7,5,2,1,6],
#            'Year':[1975,1979,1983,1987,1992]}
#
# chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
#          'Rank':[3,4,9],
#          'Year':[1995,1992,1993]}
# df1=pd.DataFrame(world_cup)
# df2=pd.DataFrame(chokers)
# print(pd.concat([df1,df2]))

a=pd.DataFrame({'Key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
b=pd.DataFrame({'Key':['K1','K2','K3','K4'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
# print(left.append(right))
# print(right.append(left))
print(pd.concat([a,b],axis=0))
print(pd.concat([a,b],axis=1))
print(pd.merge(a,b,on='Key'))
print(pd.merge(a,b,on='Key',how='left'))
print(pd.merge(a,b,on='Key',how='right'))
print(pd.merge(a,b,on='Key',how='outer'))
print(pd.merge(a,b,on='Key',how='inner'))