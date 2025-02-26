try:
    age = int(input("Enter Your Age: "))
except Exception as e:
    print(e)
else:
    if age % 2 == 0:
        print("Age is even.")
    else:
        print("Age is odd.")