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

def tower_of_hanoi(n,x,y,z):
    if n == 1:
        print(f"{x} -> {y}")
    else:
        tower_of_hanoi(n - 1,x,z,y)
        print(f"{x} -> {y}")
        tower_of_hanoi(n - 1,z,y,x)
        

tower_of_hanoi(4,'A','B','C')



