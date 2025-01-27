# inverted triangle
n = int(input("Number: "))
for i in range(n,0,-1):
    for j in range(1,i + 1):
        print(f"{j}",end = ' ')
    print()

units = float(input("Enter Number Of units consumed: "))
bill = 0

if units < 50:
    bill = (units * 2.60) + 25
    print(f"bill = (units) * 2.60 + 25 = {bill} ")

elif units <= 100:
    bill = (50 * 2.60) + ((units - 50) * 3.25) + 35
    print(f"bill =  (50 * 2.60) + ((units - 50) * 3.25) + 35 = {bill}")

elif units <= 200:
    bill = (50 * 2.60) + (50 * 3.25) + ((units - 100) * 5.26) + 45
    print(f"bill = (50 * 2.60) + (50 * 3.25) + ((units - 100) * 5.26) + 45 = {bill}")

else:
    bill = (50 * 2.6) + (50 * 3.25) + (100 * 5.26) + ((units - 200) * 8.25) + 75
    print(f"bill = (50 * 2.6) + (50 * 3.25) + (100 * 5.26) + ((units - 200) * 8.25) + 75 = {bill}")


# star pattern 
# i have tried my bext with it. it is not centered
# output:
# *
# ***
# *****
# ***
# *
for i in range(1):
    for j in range(1,6,2):
        print("*"*j)
for i in range(1):
    for j in range(3,0,-2):
        print("*"*j)
    print()


