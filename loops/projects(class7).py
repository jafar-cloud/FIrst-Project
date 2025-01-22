# multiplication table
num1 = 10
for i in range(0,num1 + 1):
    print(f'{num1} x {i} = {num1 * i}')

# armstrong number checker
n = 153
m = n
k = n
number_of_digits = 0
sum_of_digits_raised_to_length_of_digits = 0 # sorry for long name i wrote it so you can understand it

while m > 0:
    m //= 10
    number_of_digits += 1

while k > 0:
    sum_of_digits_raised_to_length_of_digits += (k % 10) ** number_of_digits
    k //= 10

if sum_of_digits_raised_to_length_of_digits == n:
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not an armstrong number.')

# doing the previous exercise about ASCII but with for-loops. (like you suggested)
for i in 'abcdefghijklmnopqrstuvwxyz0123456789':
    print(f'ASCII Value Of {i} is: {ord(i)}')

# prime number checker
num2 = 17
for i in range(2,num2):
    if num2 % i == 0:
        print(f"{num2} is not prime")
else:
    print(f"{num2} is prime.")

# reverse a number
# this is a really really clever way of doing it using string concatenation..
number = 1234
m2 = number
s = ''
while (m2 > 0):
    s = s + f'{m2 % 10}'
    m2 //= 10
reversed_number = int(s)
print(f'reverse of {number} is {reversed_number}')

# this uses the previous problem to solve the next one.. (palindrome checker)
number2 = 121
m3 = number2
s2 = ''
while m3 > 0:
    s2 = s2 + f'{m3 % 10}'
    m3 //= 10
reversed_number2 = int(s2)
if reversed_number2 == number2:
    print(f'{number2} is a palindrome')
else:
    print(f'{number2} is not a palindrome')

# check the pattern_printing.py file for patterns (note: the multiplication table is in this exercise)