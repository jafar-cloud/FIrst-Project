number = int(input('Enter A Number: '))
square_root = number**0.5
print(f'Square root of {number} is {square_root}')
# doing this for extra credit
print("Now I'm Giving A Rounded Up Answer.")
d = int(input('How Many Rounded Digits: '))
r = round(square_root,d)
print(f'Square Root Of {number} with {d} rounded digits is: {r}')

# student marks project
marks1 = int(input('Enter Marks 1: '))
marks2 = int(input('Enter Marks 2: '))
marks3 = int(input('Enter Marks 3: '))
marks4 = int(input('Enter Marks 4: '))
marks5 = int(input('Enter Marks 5: '))
total = marks1 + marks2 + marks3 + marks4 + marks5
p1 = round((marks1/total)*100, 1)
p2 = round((marks2/total)*100, 1)
p3 = round((marks3/total)*100, 1)
p4 = round((marks4/total)*100, 1)
p5 = round((marks5/total)*100, 1)
print(f'Total Marks Are: {total}') ; print(f'Percentage of Marks 1 is: {p1}%') ; print(f'Percentage of Marks 2 is: {p2}%')
print(f'Percentage of Marks 3 is: {p3}%') ; print(f'Percentage of Marks 4 is: {p4}%') ; print(f'Percentage of Marks 5 is: {p5}%')