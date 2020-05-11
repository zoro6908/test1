# class First(object):
#    def __init__(self):
#        super(First, self).__init__()
#        print ("Firtst")
#
#
# class Second(object):
#    def __init__(self):
#        super(Second, self).__init__()
#        print("Second")
#
#
# class Third(Second, First):
#    def __init__(self):
#        super(Third, self).__init__()
#        print("Third")

#First()
#Third()

class Animal:
    def eat(self):
        print('Eating...')

class Dog(Animal):
    def bark(self):
        print('Barking...')

class BabyDog(Dog):
    def weep(self):
        print('Weeping...')

d=BabyDog()
d.eat()
d.bark()
d.weep()






