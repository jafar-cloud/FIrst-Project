# bmi
weight_in_kilograms = int(input("Enter weight in kilograms: "))
height_in_meters = int(input('Enter height in meters: '))
bmi = weight_in_kilograms/(height_in_meters**2)
# yes sir, i promise this works. the reason is that the elif's only run when all the previous elif's are False. So there is no need to put and here.
if bmi < 18.5:
    print('you are underweight')
elif bmi <= 24.9:
    print('your bmi is normal')
elif bmi <= 29.9:
    print("you are overweight")
elif bmi <= 39.9:
    print("you are obese")
else:
    print("You are severly obese.")

# student grade
# for simplicity, i am only taking total marks of all subjects combined out of (highest marks possible) 1000
student_marks = int(input("Enter Your Marks: "))
percentage = (student_marks / 1000) * 100
if percentage > 100:
    print("Invalid Marks. Please Try Again.")
    student_marks = int(input("Enter Your Marks Again: "))

# similarly here you don't need and statement.
else:
    if percentage >= 90:
        print("Your Grade Is A")
    elif percentage >= 85:
        print("Your Grade Is: B")
    elif percentage >= 75:
        print("Your Grade Is: C")
    elif percentage >= 65:
        print("Your Grade Is: D")
    else:
        print("Your Grade Is: F")
