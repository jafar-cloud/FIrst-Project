d = {
    1 : 'jafar',
    '2' : 'akash',
}
print(d)
print(d['2'])
d[3] = 'me'
print(d[3])

for something in d.keys():
    print(something)

for other in d.values():
    print(other)

for x,y in d.items():
    print(x,y)

word = 'akashjafarme'

dictionary = {}

for ch in word:
    if ch not in dictionary.keys():
        dictionary[ch] = 1
    else:
        dictionary[ch] += 1
    
for char,count in dictionary.items():
    print(f"{char} : {count}")