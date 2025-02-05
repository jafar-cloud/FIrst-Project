string = input("Enter String: ")

list = []

for element in string:
    if element not in list:
        list.append(element)



for something in list:
    count = 0
    for i in string:
        if i == something:
            count += 1
    print(f"{something} occures {count} times.")
