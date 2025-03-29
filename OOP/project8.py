class MyClass:
    def __init__(self):
        self.__privateVar = 2
    
    def __privMethod(self):
        print("Hi there.")

    def hello(self):
        print(self.__privateVar)


a = MyClass()

a.hello()
a.__privMethod()
