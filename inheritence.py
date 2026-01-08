class Demo:
    def print1(self):
        print("print1")
    def print2(self):
        print("print2")

class child1(Demo):
    def print2(self):
        print("print2 from child1")

class child2(Demo):
    pass

class child3(Demo):
    def print2(self):
        print("print2 from child3")

obj1=child1()
obj2=child2()
obj3=child3()
for i in(obj1,obj2,obj3):
    i.print2()