class IOString:
    def __init__(self):
        self.str = ''

    def set_str(self, new_value):
        self.str = new_value
    
    def print_str(self):
        print(f"String is: {self.str.upper()}")


my_str = IOString()

my_str.set_str("Hi")

my_str.print_str()