number = int(input('Enter A Number: '))
square_root = number**0.5
print(f'Square root of {number} is {square_root}')
# doing this for extra credit
print("Now I'm Giving A Rounded Up Answer.")
d = int(input('How Many Rounded Digits: '))
r = round(square_root,d)
print(f'Square Root Of {number} with {d} rounded digits is: {r}')