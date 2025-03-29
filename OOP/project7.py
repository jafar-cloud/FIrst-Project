class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def chirp(self):
        print("Bird chirping")
    
    def sleep(self):
        print("Bird sleeping.")
    

class Child(Bird):
    def method1(self):
        print("Method 1")
        super().__init__("ok", "ok2")
    
    def method2(self):
        print("Method 2")


a = Child(name="child", age=10)