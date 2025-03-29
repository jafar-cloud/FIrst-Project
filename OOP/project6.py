class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(f"Name: {self.name}, Id Number: {self.id_number}")


class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post


employee = Employee(name="Whatever", id_number=43243423, salary=20_000, post="Education")

print(employee.name, employee.id_number)

print(employee.display())