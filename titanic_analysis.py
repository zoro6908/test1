import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

original_df=pd.read_csv("titanic3.csv")

# print('# of passengers in original data:' + str(len(original_df.index))+'\n')
# print(original_df.head())
# print(original_df.isnull().sum())
#
# age_wrangled_df=original_df[pd.notna(original_df['age'])]
# print('No of passenger in age wragled data: '+str(len(age_wrangled_df.index))+'\n')
#
# embark_wrangled_df=original_df[pd.notna(original_df['embarked'])]
# print('No of passenger in embark wragled data: '+str(len(embark_wrangled_df.index))+'\n')

embark_wrangled_df=original_df[pd.notnull(original_df['embarked'])]
gender_data=embark_wrangled_df.groupby('sex', as_index=False)
gender_mean_data=gender_data.mean()
print('Total Survival Rate: '+str(embark_wrangled_df['survived'].mean()),'%')
print('\nMean Data by Gender')
print(gender_mean_data[['sex','survived','age','pclass', 'sibsp', 'parch','fare']])

# 전체 인원계산
total_df=gender_data['name'].count()
print('\n',total_df)
# print('\n',gender_data)

# 컬럼 이름을 변경 (sex, name) -> (sex, total)
total_df.columns=['sex','total']
print('\n',total_df)

gender_list=total_df['sex']
# print('\n',gender_list)
del total_df['sex']
print(gender_data)
#
gender_survived_df=gender_data['survived'].sum()
del gender_survived_df['sex']

combinded_df=total_df.add(gender_survived_df,fill_value=0)
print(combinded_df)

combinded_df.plot.bar(color=['limegreen','dodgerblue'])
plt.title('Effect of Gender on survival')
plt.xlabel('Gender')
plt.ylabel('No of people')
plt.xticks(range(len(gender_list)),gender_list)

# survival_gender_list=[combinded_df.loc[0]['survived']],[combinded_df.loc[1]['survived']]
# total_gender_list=[combinded_df.loc[0]['survived']],[combinded_df.loc[1]['survived']]
#
# def create_value_labels(list_data,decimals,x_adjust,y_adjust):
#     for x, y in enumerate(list_data):
#         plt.text(x + x_adjust, y + y_adjust,round(list_data[x],decimals),color='w',fontweight='bold')

# create_value_labels(survival_gender_list, 1, -0.2, -50)
# create_value_labels(total_gender_list, 1, 0.05,-50)
plt.show()