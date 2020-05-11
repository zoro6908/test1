import pandas as pd
import numpy as np

# 판다 데이터 플레임 정의1
# d={'odd':np.arange(1,100,2), 'even':np.arange(0,100,2)}
# print(d['odd'])
# print(d['even'])
# df=pd.DataFrame(d)

# 판다 데이터 플레임 정의2
# df=pd.DataFrame({'odd':np.arange(1,10,2), 'even':np.arange(0,10,2)})
# print(df)

# 각 데이터의 합계 출력 : odd     25 even    20
# print(df.sum())

# 데이터의 표준편차 출력
# print(df.std())

df=pd.DataFrame(np.random.rand(5,4),columns=['col1','col2','col3','col4'])
# for key, value in df.iteritems():
#     print('KEY:', key)
#     print('VALUE:', value, type(value))

    # print(key,value)

# iterrows
# for key, value in df.iterrows():
#     # print('KEY:', key)
#     print('VALUE DIMENSION:', value.ndim) #, type(value))

for row in df.itertuples():
    print(row)
    print(type(row))

    # print(key,value)


    # print(key,value)