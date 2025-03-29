class Computer:
    def __init__(self):
        self.__max_price = 1000

    def sell(self):
        print(f"Max price is {self.__max_price}")

    def set_max_price(self, new_max_price):
        self.__max_price = new_max_price


comp = Computer()
comp.__max_price = 67
comp.sell()
comp.set_max_price(100)
    