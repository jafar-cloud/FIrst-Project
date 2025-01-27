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