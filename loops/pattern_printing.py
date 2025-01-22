# star pattern right-angle triangle
for i in range(6):
    for j in range(i):
        print('*', end = '')
    print()

# please clarify what (2. pyramid of numbers) means. i cannot see a clear pattern.


# inverted pyramid of numbers
for i in range(6,0,-1):
    for j in range(1,i):
        print(j, end = '')
    print()
