class Outer:
    def __init__(self,name):
        self.name=name
    class Inner:
        def __init__(self,name,age):
            self.name=name
            self.age=age

        def print1(self):
            print(f"Name :{self.name} , Age : {self.age}")

    def print1(self):
        print(self.name)

obj1=Outer("AAA")
obj1.print1()

obj2=obj1.Inner("BBB",18)
obj2.print1()
