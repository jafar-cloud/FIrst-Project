print('Basic Calculator')
print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')

choice = int(input('What Do You Want To Do? '))
num1 = float(input('Enter Number 1: '))
num2 = float(input("Enter Number 2: "))
if choice == 1:
    print(f'Sum Of {num1} and {num2} is: {num1 + num2}')
elif choice == 2:
    print(f'Difference Of {num1} and {num2} is: {num1 - num2}')
elif choice == 3:
    print(f'Product Of {num1} and {num2} is: {num1 * num2}')
elif choice == 4:
    print(f'Division Of {num1} and {num2} is: {num1 / num2}')
else:
    print('Invalid Choice')