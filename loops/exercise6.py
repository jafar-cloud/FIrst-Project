# a = int(input("Enter Lower Boundary: "))
# b = int(input("Enter upper boundary: "))
# for i in range(0,b):
#     print(a * (3 ** i))


# j = 0
# while j < b:
#     print(a * (3 ** j))
#     j += 1


s = input("Enter A String: ")

reverse_string = ''

for i in s:
    reverse_string = i + reverse_string

print(reverse_string)