n = int(input("Enter Number: "))
m = n
even_count = 0
odd_count = 0
while (m > 0):
    if (m % 10) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    m //= 10

print(even_count)
print(odd_count)


