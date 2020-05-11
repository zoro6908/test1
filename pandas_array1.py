import pandas
import numpy

# arr=numpy.array([3,9,19,27,56,109,200])
# data_d={'a':1,'b':2,'c':3}
#
# ser=pandas.Series(arr)
# ser=pandas.Series(data_d)
#
# print(ser)
# print(data_d)

# listx=[10,20,30,40]
# table=pandas.DataFrame(listx)
#
# listy=[{'a':1, 'b':2}, {'a':23, 'b':41}, {'a':45, 'b':47}]
# table=pandas.DataFrame(listy)
#
# listz=[{'a':1, 'b':2}, {'a':23, 'b':41}, {'a':45, 'b':47,'c':48}]
# tablez=pandas.DataFrame(listz, index=['r1','r2','r3'])
#
# print(listx)
# print(table)
# print(tablez)
# print(type(listx))
# print(type(table))

sr1=pandas.Series([40,50,60], index=['math','chem','phys'])
sr2=pandas.Series([70,80,90], index=['math','chem','phys'])

table=pandas.DataFrame({'jim':sr1, 'sara':sr2})

print(table)
