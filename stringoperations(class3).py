a = 'akash'
b = ' kumar roy'
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-1]) # last index
print(a[-2]) # second to last index...and so on
print(a[-3])
print(a[-4])
print(a[-5])
# spaces are also considered characters

# displays the length of a string (including spaces)
print(f'length of {a} is {len(a)}')
print(f'length of {b} is {len(b)}')
# concatenation of 2 (or more are allowed) strings
c = a + b
print(c)
print(f'length of {c} is {len(c)}')
# reverses a string
print(a[::-1])
# slicing
# this return a string starting at index 1 of string a until the end
print(a[1:])
# this returns a string starting at index 0 and ends just before index 2 (it ends at an index one less than the number)
print(a[:2])
# this returns a string starting at index 3 and ending at index 4 (which is one less than 5)
print(a[3:5])
# lower function turns everything lower case
d = 'HI'
print(d)
print(d.lower())
# upper function returns upper case
f = 'hi'
print(f)
print(f.upper())
# arithmetic operators (i already know about it LOL)
print(25%7) # % returns remainder
print(25//7) # // ignores decimal part, is called floor division (also know about it LOL)
print(2**3) # power 
