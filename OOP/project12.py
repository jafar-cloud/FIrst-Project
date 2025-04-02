from abc import ABC, abstractmethod


class A(ABC):
    def display(self):
        print("displaying value")

    @abstractmethod
    def abs_method(self):
        pass


class B(A):
    def abs_method(self):
        print("Abstract method")



try:
    a = A()
except TypeError as e:
    print(e)
finally:
    b = B()
    b.abs_method()
