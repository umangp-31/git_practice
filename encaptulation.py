from html.entities import name2codepoint


class Demo:
    def __init__(self,name):
        self.name = name
        self.__amount=100

    def getAmount(self):
        return self.__amount



obj1= Demo("Abc")
print(obj1.name)
# print(obj1._Demo__amount)
print(obj1.getAmount())