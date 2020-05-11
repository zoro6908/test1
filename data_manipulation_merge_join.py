import pandas as pd
import numpy as np

world_cup={'Team':['West Indies', 'India', 'Australia', 'Pakistan', 'Sri Lanka'],
           'Rank':[7,5,2,1,6],
           'Year':[1975,1979,1983,1987,1992]}

chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
         'Rank':[3,4,9],
         'Year':[1995,1992,1993]}

df1=pd.DataFrame(world_cup)
df2=pd.DataFrame(chokers)

# print(df1)
# print(df2)
print(pd.merge(df1,df2,on='Team'))