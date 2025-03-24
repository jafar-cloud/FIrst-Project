class BankAccount:
    def __init__(self, acc_num, acc_bal=0):
        self.acc_num = acc_num
        self.acc_bal = acc_bal

    def deposit(self, amount):
        self.acc_bal += amount
        print(f"{amount} added to account.")
    
    def withdraw(self, amount):
        if amount > self.acc_bal:
            print("Insufficent balance.")
        else:
            self.acc_bal -= amount
            print(f"{amount} withdrawed from account.")

    def display_details(self):
        print(f"Account Name: {self.acc_num}, Account Balance: {self.acc_bal}")


class Employee:
    tax = 13 / 100
    def __init__(self, name, id, basic_salary):
        self.name = name; self.id = id; self.basic_salary = basic_salary

    def gross_salary(self, hra, da):
        return self.basic_salary + hra + da
    
    def net_salary(self):
        return self.gross_salary(100, 100) * (1 - self.tax)
    

class Manager(Employee):
    pass


class Developer(Employee):
    pass

