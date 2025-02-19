print('Welcome To Music Library!')

library = []

def search(s):
    if s in library:
        return f"{s} Music is in the library.\n"
    else:
        return f"{s} Music is not in the library.\n"

def add(a):
    """The reason i removed * Is Becuase it's not needed."""
    for item in a:
        if item in library:
            print(f"{item} already in library.\n")
            return 1
    else:
        for i in a:
            library.append(i)

def remove(b):
    pass


while True:
    print("What do you want to do?")
    print("Option 1. Search")
    print("Option 2. Add")
    print("Option 3. Remove")
    print("Option 4. Display Library")
    print("Option 5. Exit\n")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        s = (input("Enter the name of the music you want to search for: "))
        print(search(s))

    elif choice == 2:
        while True:
            t = []
            name = input("Enter Names Of Music you want to add (type exit to stop): ")
            if name == 'exit':
                break
            else:
                t.append(name)
            a = add(t)
            if a == 1:
                break
    
    elif choice == 3:
        pass
    elif choice == 4:
        print(library)
    elif choice == 5:
        break
    else:
        print("Wrong choice, try again.")


