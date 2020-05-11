# 출력 명령어
# print('*' * 10) # ********** 10 아스트리크

# 변수
# price  = 10 # print(type(price)) --> <class 'int'>
# rating = 4.9 # <class 'float'>
# name = 'Jung' # <class 'str'>
# is_published = True #<class 'bool'>
#
# print(type(price),type(rating),type(name), type(is_published))

# 입력 명령어
# name = input('What is your name? ')
# print('Hi ' + name) # concatenate two string
# color = input('What is your favorite color? ')
# print(name + 'Like ' + color)

# Type 변경 1
# from datetime import datetime
#
# birth_year = input('Birth yeae: ')
# print(type(birth_year)) # <class 'str'>
# age = datetime.today().year - int(birth_year)
# print(type(age)) # <class 'int'>
# print(age)

# Type 변경 2
# weight_lbs = input('Weight (lbs): ')
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)

# String
# course = '''
# Hi
# I am Good
# See you
# ''' # multiline string
# print(course)
# course = 'Python for Beginners'
# another = course[:]
#
# print(course[0]) # P
# print(course[-1]) # s
# print(course[-2]) # r
# print(course[0:3]) #end index는 제외 : Pyt
# print(course[0:]) # Python for Beginners
# print(course[0:5]) # Pytho
# print(course[1:]) # ython for Beginners
# print(another)

# print(name[1:-1])
# name = 'Jennifer'
#
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# String Method
# course = 'Python for Beginners'
# print(len(course))
# print(course.__len__())
# print(course.upper())
# print(course.lower())
# print(course) # Not modifyed
# print(course.find('P')) # Index Return : 0
# print(course.find('f')) # Index Return : 7
# print(course.find('O')) # Index Return : -1, Not find
# print(course.find('Beginners')) # Start Index Return : 11
# print(course.replace('Beginners','Absolute Beginners')) # String Change
# print(course) # Not modifyed
# print('Python' in course) # True
# print('python' in course) # False

# Arithmetic operation
# print(10 + 3) # retun : 3
# print(10 / 3) # return float : 3.3333333333333335
# print(10 // 3) # return inter : 3
# print(10 % 3) # return divistion : 1
# print(10 ** 3) # return : 1000
#
# x = 10
# x = x + 3 # return 13
# x = += 3 # return 13
# x = -= 3 # return 7

# operator precedence
# x = 10 + 3 * 2 # return 16
# x = 10 + 3 * 2 ** 2 # return 22
# x = (10 + 3) * 2 ** 2 # return 52
# x = (2 + 3) * 10 - 3 # return 47

# 연산 순서
# parenthesis 괄호
# exponentiation 2 ** 3
# multiplication or division
# addtion or subtraction

# Math Function
# import math
#
# x = 2.9
# print(round(x)) # return 3
# print(abs(-2.9)) # return 2.9
# print(math.ceil(x)) # return 3

# If statement
# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("It's Hot Day")
#     print("Drink A lot Water")
# elif is_cold:
#     print("It's coldDay")
#     print("Wear warm clothes")
# else:
#     print("It's Lovely day")
# print("Enjoy your day~~~")

# If statement 2
# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down Payment: ${down_payment}')

# If statement 3
# has_high_income = True
# has_high_credit = True
#
# and : both, or : at least one , not#
# if has_high_income and has_high_credit:
#     print("Greate~~~~~")
#
# if has_high_income or has_high_credit:
#     print("Greate~~~~~")
#
# if has_high_income and not has_high_credit:
#     print("Greate~~~~~")

# temperature = 30
#
# if temperature > 30: # ==, >=, !=
#     print("It's hot day")
# else:
#     print("It's not host day")

# If statement 4
# name = input("What's your Name? : ")
#
# if len(name) < 3:
#     print("Name must be at 3 charactor? ")
#     name = input("Rename Please : ")
# elif len(name) > 7:
#     print("Name must be at 7 charactor? ")
#     name = input("Rename Please : ")
# else:
#     print(f'Your Name is {name}')

### unit convert
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
#
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f'You are {converted} Kilograms')
# elif unit.upper() == 'K':
#     converted = weight / 0.45
#     print(f'You are {converted} pounds')
# else:
#     print("reinput unit")

### while Loop
# i = 1
# while i <= 5:
#     # print(i)
#     print('*' * i)
#     # i = i + 1
#     i += 1


# secret_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
# # guess_count = guess_count + 1
#     if guess == secret_number:
#         print("Yoy Win~~~")
#         break
# else:
#     print("\nYou losse~~~")

# 반복문 While
# command = ""
# started = False
#
# while command.lower() != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped...")
#     elif command == "help":
#         print("""
# start - to start car
# stop - to stop car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I dont kwon")

# 반복문 for
# for item in 'Python':
#     print(item)
# result P... y... t... 한 문자씩 출력
# for item in ['Kim','jo','Choi']:
#     print(item)
# for item in range(10): #result : 0에서 9까지 출력
#     print(item)
# for item in range(5,10,2): #(start,stop,step), result : 5,7,9
#     print(item)
# prices = [10, 20, 30]
# total = 0
#
# for price in prices:
#     # total = total + price
#     total += price
# print(f"Total; {total}")
# Nested loop
# for x in range(4): # outter loop
#     for y in range(3): # inner loop
#         print(f'({x},{y})')
# x 찍기
# number = [5,2,5,2,2]
# for i in number:
#     print('X' * i)
# x 찍기 2
# number = [5,2,5,2,2]
# for i in number:
#     output = ''
#     for j in range(i):
#         output += 'X'
#     print(output)
# List
# names = ['Kim','Jo','Choi','Han', 'Park']
# print(type(names),names) # <class 'list'> ['Kim', 'Jo', 'Choi', 'Han', 'Park']
# print(names[1]) # jo
# print(names[-1]) # Park
# print(names[2:]) # ['Choi', 'Han', 'Park']
# print(names[2:4]) # ['Choi', 'Han']
#
# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
#
# for i in numbers:
#     if i > max:
#         max = i
#         print(max)
# print(f'\n At Last max num : {max}')

### 2D List
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# # matrix[0][1] = 20
# # print(matrix[0][1])
#
# for i in matrix:
#     for j in i:
#         print(j)

### List Method
# numbers = [5,2,1,7,4]
# numbers.append(13) # List 추가 : [5, 2, 1, 7, 4, 13]
# numbers.insert(0, 10) # 해당 index에 추가 : [10, 5, 2, 1, 7, 4]
# numbers.remove(5) # List 삭제 : [2, 1, 7, 4]
# numbers.clear() # List 전체 삭제 : []
# numbers.pop() # 마지막 삭제 : [5, 2, 1, 7]
# numbers.append(5) # [5, 2, 1, 7, 4, 5]
# print(numbers.count(5)) # 5를 찾음 : 2
# print(numbers.sort()) # : None
# numbers.sort() # result : [1, 2, 4, 5, 7]
# numbers.reverse() # result : [7, 5, 4, 2, 1]
# numbers2 = numbers.copy()
# numbers.append(10)
#
# print(numbers)
# print(numbers2)

### 동일 값 삭제하기
# numbers = [2,3,4,6,3,4,6,1]
# uniques = []
#
# for i in numbers:
#     if i not in uniques:
#         uniques.append(i)
# print(uniques)

### Tuples :아이템 변경이 안되
# numbers = (1,2,3)
# numbers[0] = 10 # TypeError: 'tuple' object does not support item assignment
# print(numbers[0]) # result : 1

### Unpacking
# coordinates = (1,2,3)
# x, y, z = coordinates # 아래와 동일한 정의
# x = coordinates[0]
# y = coordinates[0]
# z = coordinates[0]

### dctionanies
# customer = {
#     "name":"john Smith",
#     "age":30,
#     "is_verfied":True
# }
# print(customer[name])    # NameError: name 'name' is not defined
# print(customer["Name"])  # KeyError: 'Name'
# print(customer["name"])
# print(customer.get("name")) # Result : john Smith
# print(customer.get("birthdate","jan 1 1980")) # result : jan 1 1980
# customer["name"] = "Jack Smith"
# print(customer["name"]) # result : Jack Smith
# 2:23:32
# phone = input("Phone: ")
# output = ""
# digits_mapping = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# for ch in phone:
#     output += digits_mapping.get(ch,"!") + " "
# print(output)
#
# message = input(">")
# word = message.split(' ') # space로 구분하여 리스트 형식으로 저장
# output = ""
# emojis = {
#     ":)":"😀",
#     ":(":"😞"
# }
# for i in word:
#     output += emojis.get(i, i) + " "
# print(output)

### Funtion
# def greet_user():
#     print('Hi')
#     print('Welcome')
#
# greet_user()
#
# def greet_user(name):
#     print(f'Hi {name} !')
#     print('Welcome')

# greet_user("john")
# greet_user(john) # NameError: name 'john' is not defined
# greet_user() # TypeError: greet_user() missing 1 required positional argument: 'name'

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name} !')
#     print('Welcome')
# greet_user("Jo","Smith")
# greet_user(last_name="Jo",first_name="Smith") # Keyword argument

# def square(number):
#     return number * number
#
# num = int(input("Input number : "))
# result = square(num)
# print(result)

### Exception
# age = int(input('Age; '))
# print(age) # ValueError: invalid literal for int() with base 10: 'abcd'
# try:
#     age = int(input('Age; '))
#     income = 20000
#     risk = income / age # ZeroDivisionError: division by zero
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid Value')

### Classes
# class Point:
#     # def __init__(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# pt = Point()
# pt.draw()
#
# pt.x = 10
# pt.y = 20
# print(pt.x)
#
# pt1 = Point()
# print(pt1.x) # AttributeError: 'Point' object has no attribute 'x'

### 예제 Calss : Person
###      attribute : name
###      method : talk()
# class Person:
#     def talk(self):
#         print("talk")
#
# john = Person()
# john.talk()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print("talk")
#
# # john = Person() # TypeError: __init__() missing 1 required positional argument: 'name'
# john = Person("John Smith")
# print(john.name)
# john.talk()
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'I am {self.name}')
#
# # john = Person() # TypeError: __init__() missing 1 required positional argument: 'name'
# john = Person("John Smith")
# john.talk() # I am John Smith
#
# bob = Person('Bob Smith')
# bob.talk()

### Inheritnace
### 동일한 메소드를 사용할 경우
# class Dog:
#     def walk(self):
#         print('walk')
#
# class Cat:
#     def walk(self):
#         print('walk')
#
# class Mammal:
#     def walk(self):
#         print('walk')
#
# class Dog(Mammal):
#     pass
#
# class Cat(Mammal):
#     pass
#
# dog1 = Dog()
# dog1.walk()

# class Mammal:
#     def walk(self):
#         print('walk')
#
# class Dog(Mammal):
#     def bark(self):
#         print('bark')
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print('annoying')
#
# dog1 = Dog()
# dog1.bark()
# dog1.walk()

### Modules
# import converters
#
# print(converters.kg_to_lbs(70))

# import converters
# from converters import kg_to_lbs
#
# print(kg_to_lbs(100))
# print(converters.kg_to_lbs(70)) #NameError: name 'converters' is not defined (import coneters 가 없는 경우)
#
# import utils
#
# numbers = [10,3,6,2]
# print(utils.find_max(numbers))
# print(max(numbers)) # Bulit in fucton

### Package
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
### package : ecommerce
### module : shipping
### function : calc_shipping

# from ecommerce.shipping import calc_shipping
#
# calc_shipping()

### Random values
import random

# for i in range(3):
#     # print(random.random())
#     print(random.randint(10,20))

# members = ['John','Mary','Bob','Mosh']
# leader = random.choice(members)
# print(leader)
#
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return(first,second)
#
#
# dice = Dice()
# print(dice.roll())

### Files & Directory
from pathlib import Path
# Absolute path : c:\adfa
# Relative path

# path = Path('ecommerce')
# print(path.exists()) # True
#
# path = Path()
# for file in path.glob('*.py'):
#     print(file)

### Pypi and Pip

### Exel control and Chart
# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#     # cell = sheet['a1']
#     # cell = sheet.cell(1,1)
#     # print(cell.value) # transaction_id
#
#     for row in range(2,sheet.max_row + 1):
#         # print(row)
#         cell = sheet.cell(row, 3)
#         # print(cell.value)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#                        min_row=2,
#                        max_row=sheet.max_row,
#                        min_col=4,
#                        max_col=4)
#
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#
#     wb.save(filename)

### Machine Learning
### Machine Learning Action
### Step1. Import Data
### Step2. Clean Data
### Step3. Split the Data into Training/Test Sets
### Step4. Create a Model
### Step5. Train the Model
### Step6. Make Predictions
### Step7. Evaludate and improve

### Libraries : Numpy, Pandas, MatPlotLib, Scikit-Learn
### https;//jupyter.org
### https://anaconda.com/download/anaconda
### 아나콘다란 Continuum Analytics(현 Anaconda Inc.)에서 제작한 배포판 파이썬입니다.
### 쉽게 말하면 파이썬 편집 프로그램, 즉 파이썬 전용 비주얼 스튜디오라고 할 수 있습니다.
### 현재 약 600만 명 가량이 아나콘다를 사용중이며, 400개 이상의 패키지를 지원한다고 합니다.

### 파이썬은 pip 라는 훌륭한 패키지 관리자가 있지만 머신 러닝이나 R 사용을 위한 개별 패키지를 설치하는 건 매우 귀찮은 일입니다.
### 아나콘다는 이런 문제 해결을 위해 사전에 패키징한 python 배포판입니다.

### Anaconda란 세계에서 가장유명한 오픈소스 파이썬 데이터 사이언스 플랫폼입니다. 데이터 사이언스 관련 패키지를 손쉽게
### 설치/관리 할 수 있으며 다양한 파이썬 버전별로 가상환경을 제공함에 따라서 파이썬의 효율성을 극대화 시킬 수 있습니다.

### https://www.kaggle.com #zoro6908 계정생성
### http://bit.ly/music-csv


