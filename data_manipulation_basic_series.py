import pandas as pd
import numpy as np

# 1-51사이를 시리즈를 정의
# df=pd.Series(np.arange(1,51))

# print(df)

# 데이터의 디멘전 출력
# print(df.ndim)

# 데이터의 디멘전 = 2
df=pd.DataFrame({'a': pd.Series(np.arange(1,51)),'b':pd.Series(np.arange(51,101))})
# print(df)
print(df.ndim)

# 데이터의 라벨값 출력 [RangeIndex(start=0, stop=50, step=1), Index(['a', 'b'], dtype='object')]
# df=pd.DataFrame({'a': pd.Series(np.arange(1,51)),'b':pd.Series(np.arange(51,101))})

# 데이터의 라벨값 출력 [RangeIndex(start=0, stop=102, step=1), Index(['a', 'b'], dtype='object')]
# df=pd.DataFrame({'a': pd.Series(np.arange(1,103)),'b':pd.Series(np.arange(51,101))})

print(df.axes)

# 데이터의 값을 출력
print(df.values)

# 데이터의 처음값을 출력 (디폴트는 5)
print(df.head(10))

# 데이터의 꼬리값을 출력 (디폴트는 5)
print(df.tail())