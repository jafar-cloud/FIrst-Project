class A:
    def __init__(self):
        self.__x = 1


a = A()

a._A__x = 8
print(a._A__x)