class base1:
    def fun(self):
        print("In Class Base1")


class sub(base1):
    pass

ob=sub()
ob.fun()
