numbers = [1,2,3,4,5,6,7,8,9,10]

temp = numbers

x = int(input("Enter Number To Be Found: "))

first = 0

last = len(numbers) - 1

while first < last:
    middle = (last + first) // 2
    if x == numbers[middle]:
        print(f"Element found at index {middle}")
        break
    elif x < numbers[middle]:
        last = middle - 1
    else:
        first = middle + 1
else:
    print("Element Not Found")