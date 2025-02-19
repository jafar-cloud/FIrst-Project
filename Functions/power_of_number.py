def power(a,b):
    if b == 0:
        return 1
    else:
        return power(a,b - 1) * a
    

# print(power(2,3))

def reverse_a_string(s):
    if len(s) == 1:
        return s
    else:
        return reverse_a_string(s[1:]) + s[0]


# print(reverse_a_string('abc'))

def tower_of_hanoi(n):
    if n == 1:
        print("A -> B")

        



# 
#     
#     
#     
# 
#         1
# 3       2 
# A   B   C

