class A:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other: 'A'):
        return self.val < other.val
    
    def __eq__(self, other: 'A'):
        return self.val == other.val
    

obj1 = A(3)
obj2 = A(4)

print(obj1 < obj2)
print(obj1 == obj2)