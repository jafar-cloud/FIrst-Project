# I have tried my best
# find the first 1 in a binary bit
binary_number = str(input("enter Number: "))

decimal = 0

for digit in range(len(binary_number)):
    decimal += int(binary_number[digit]) * (2 ** (len(binary_number) - 1 - digit))

for i in range(len(binary_number),-1,-1):
    if decimal & 1 == 0:
        print(f"First 1 found at position {len(binary_number) - i - 1}")
        break
    else:
        decimal >>= 1
else:
    print("Not found.")


# find whether the n'th bit (from the last (and  starts at one) is a 1 or not.)

dec = input("Enter Number: ")
position = int(input("Enter Position: "))
l = []
i = int(dec)
while i != 0:
    l.append(str(i % 2))
    i //= 2
l = l[::-1]
binary = ''.join(l)

dec = int(dec) >> (position - 1)

l = []
i = int(dec)
while i != 0:
    l.append(str(i % 2))
    i //= 2
l = l[::-1]
binary2 = ''.join(l)

print(f"At {position}st/nd/rd/th Position There Is A {binary2[-1]}.")

# mirrored right angle triangle
# my best attempt
for i in range(5):
    for j in range(i):
        if j == 0:
            print("        *",end=' ')
        else:
            print("*",end=' ')
    if i != 4:
        print()
    
for i in range(5):
    for j in range(i):
        print("*",end=' ')
    print()

# lazy way of doing it
print("          *  *          ")
print("        * *  * *        ")
print("      * * *  * * *      ")
print("    * * * *  * * * *    ")
print("  * * * * *  * * * * *  ")
print("* * * * * *  * * * * * *")
