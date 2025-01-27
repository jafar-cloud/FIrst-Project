print("1. Bikes")
print("2. Cars")

choice = int(input("Which one do you want? "))

if choice == 1:
    print("1. Electic Bike")
    print("2. Petrol Bike")

    choice2 = int(input("Which one do you want? "))

    if choice2 == 1:
        print("You have chosen electric bike")
    elif choice2 == 2:
        print("You have chosen petrol bike.")
    else:
        print("Invalid choice.")

elif choice == 2:
    print("1. Electric Car.")
    print("2. gasoline car")

    choice3 = int(input("Which one do you want? "))

    if choice3 == 1:
        print("You chose electric car")
    elif choice3 == 2:
        print("You chose gasoline car.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice")