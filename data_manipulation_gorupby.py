import pandas as pd

world_cup={'Team':['West Indies', 'West indies', 'India', 'Australia', 'Pakistan', 'Sri Lanka', 'Ausralia', 'Australia', 'Australia', 'Insia', 'Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,1,],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df=pd.DataFrame(world_cup)

# print(df)
# print(df.groupby('Team').groups)
# print(df.groupby(['Team','Rank']).groups)

# grouped=df.groupby('Team')
# print(grouped)
# for name,group in grouped:
#     print(name)

# for name,group in df.groupby('Team'):
#     print('Group Name:',name)
#     # print(group)
#     print(group['Year'])
#     print('================================')

grouped=df.groupby('Team')
print(grouped.get_group('India'))


