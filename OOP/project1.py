class Student:
    def __init__(self, grade):
        self.grade = grade

    def method(self):
        print(f"Student Grade Is {self.grade}")


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


my_vehicle = Vehicle(100, 1000)

print(f"Max speed is {my_vehicle.max_speed}, And Mileage Is {my_vehicle.mileage}")


class Parrot:
    species = "Something Here"

    def __init__(self, name, age):
        self.name = name
        self.age = age


my_parrot = Parrot(name="I don't know", age=120)

print(my_parrot.name)
print(my_parrot.age)
