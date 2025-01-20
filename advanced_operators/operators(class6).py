a = 3
b = 3
c = a
print(a is b)
print(a is not b)
print(a is c)

list = [1,2,3,'akash',True]
print(1 in list)
print(1 not in list)
print(f'ID of a: {id(a)}')
print(f'ID of b: {id(b)}')

a1 = [1,2,3,4]
b1 = [1,2,3,4]
c1 = a1
print(a1 is b1)
print(a1 is c1)