class Employee:
    def __init__(self):
        self.x = 1
        print("INIT called")

    def __del__(self):
        print("OBJECT DELETED!")


def create_and_delete_obj():
    print("Making object...")
    a = Employee()
    print("Object created...")
    print("Deleting object...")
    del a
    print("Object deleted.")


create_and_delete_obj()
