import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',passwd='zoro123') #,database='zoro',auth_plugin='mysql_native_password')
#
# print(mydb)
#
# if (mydb):
#     print("Connection Sucessful")
# else:
#     print("Connection Unsucessful")
#
# mycursor=mydb.cursor()
# db스키마 만들기
# mycursor.execute('create database zorodb')
# db스키마 출력
# mycursor.execute('show databases')
# for db in mycursor:
#     print(db)
# 테이블 만들기
mydb=mysql.connector.connect(host='localhost',user='root',passwd='zoro123',database='zorodb') #,auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
# mycursor.execute('create table emp(id int(4),name varchar(40),sal int(20))')
# 테이블 출력
# mycursor.execute('show tables')
# for table in mycursor:
#     print(table)
# 데이블에 데이터 입력
# sqlform='insert into emp(id,name,sal) values(%s,%s,%s)'
# emps=[(1,'kim',200),(2,'cho',300),(3,'choi',400)]
# mycursor.executemany(sqlform,emps)
# mydb.commit()
# 테이블에 입력된 데이터 출력1
mycursor.execute('select id,name,sal from emp')
for data in mycursor:
    print(data)
# 테이블에 입력된 데이터 출력2
# mycursor.execute('select id,name,sal from emp')
# myresult=mycursor.fetchone()
# for data in myresult:
#     print(data)
# 테이블에 입력된 데이터 출력3
# mycursor.execute('select * from emp')
# myresult=mycursor.fetchall()
# for data in myresult:
#     print(data)
# 데이블 데이터 업데이트
# sqlform="update emp set sal=900 where name='kim'"
# mycursor.execute(sqlform)
# mydb.commit()
# 데이블 데이터 삭제
# sqlform="delete from emp where name='kim'"
# mycursor.execute(sqlform)
# mydb.commit()