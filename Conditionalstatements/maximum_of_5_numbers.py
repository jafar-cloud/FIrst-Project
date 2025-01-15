n1 = int(input('Enter First Number: '))
n2 = int(input('Enter Second Number: '))
n3 = int(input('Enter Third Number: '))
n4 = int(input('Enter Fourth Number: '))
n5 = int(input('Enter Fifth Number: '))
max = n1
second_max = n2
if n3 > max:
    temp = max
    max = n3
    second_max = temp
if n4 > max:
    temp = max
    max = n4
    second_max = temp
if n5 > max:
    temp = max
    max = n5
    second_max = temp

print(f'Maximum Is: {max},Second Max Is {second_max}')


