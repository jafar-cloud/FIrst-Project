# odd even checker
n = int(input('Enter Number: '))
if n % 2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

# is divisible by 17 or not
m = int(input('Enter Number '))
if m % 17 == 0:
    print(f'{m} is divisible by 17')
else:
    print(f'{m} is not divisible by 17')

# student marks
student_marks = int(input('Enter Marks: '))
is_sick = input('Are You Sick? ')
if student_marks >= 75 and is_sick.lower() == 'no':
    print('You Can Take The Exam')
else:
    print('You Cannot Take The Exam')