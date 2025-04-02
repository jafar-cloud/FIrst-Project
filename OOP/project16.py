class BankAccount:
    def __init__(self, acc_holder, acc_num, bal=0):
        self.acc_holder = acc_holder
        self.acc_num = acc_num
        self.__bal = bal

    def get_balance(self):
        print(f"Balance is: ${self.__bal:.4f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.__bal:
            print("Amount too big.")
        else:
            print(f"Deducting {amount} from balance...")
            self.__bal -= amount

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        else:
            print(f"Adding {amount} to balance...")
            self.__bal += amount
    

class ATM:
    def __init__(self, acc: BankAccount):
        self.acc = acc

    def start(self):
        while True:
            print("1. Get balance.")
            print("2. Deposit (add)")
            print("3. Withdraw")
            print("4. Exit")
            choice = int(input("Enter 1, 2 or 3: "))

            if choice == 1:
                self.acc.get_balance()

            elif choice == 2:
                amount = float(input("Enter amount to deposit: "))
                self.acc.deposit(amount)

            elif choice == 3:
                amount = float(input("Enter amount to be withdrawn: "))
                self.acc.withdraw(amount)

            elif choice == 4:
                print("Have a good day!")
                break

            else:
                print("wrong choice.")
    

my_acc = BankAccount("idk", "3584589034890534")

atm = ATM(my_acc)

atm.start()