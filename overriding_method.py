
#
# class Parent:
#     def myMthod(self):
#         print("Calling parent method")
#
# class Child(Parent):
#     def myMthod(self):
#         print("Calling child method")
#
# c=Child()
# c.myMthod()


class Rectnagle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def getArea(self):
        print(self.length*self.breadth,"is area of retangle")

class Square(Rectnagle):
    def __init__(self,side):
        self.side = side
        Rectnagle.__init__(self,side,side)
    def getArea(self):
        print(self.side*self.side," is area of square")

s=Square(4)
r=Rectnagle(2,4)
s.getArea()
r.getArea()