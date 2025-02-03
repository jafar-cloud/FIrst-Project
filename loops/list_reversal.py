numbers = [1,2,3,4,5]

i = 0

length = len(numbers)

for i in range((length + 1) //2):
    temp = numbers[i]
    numbers[i] = numbers[len(numbers) - 1 - i]
    numbers[len(numbers) - 1 - i] = temp

print(numbers)


# [1,2,3,4] (4 + 1) // 2