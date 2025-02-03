# sort a list ez!

numbers = [5,4,3,2,1,1,2,3,4,5,6,7,8]

for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[j] < numbers[i]:
            numbers[j],numbers[i] = numbers[i],numbers[j] # genius way to swap 2 numbers

print(numbers)

# number of digits of a number

n = int(input("Enter Number: "))

m = n

count = 0

while m != 0:
    count += 1
    m //= 10

print(count)