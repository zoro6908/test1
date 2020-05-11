import pandas

sr1=pandas.Series([40,50,60], index=['math','chem','phys'])
sr2=pandas.Series([70,80,90], index=['math','chem','phys'])

table=pandas.DataFrame({'jim':sr1, 'sara':sr2})

table.to_csv("C:/Users/Administrator/PycharmProjects/tutorial/pandas_to_csv.csv")