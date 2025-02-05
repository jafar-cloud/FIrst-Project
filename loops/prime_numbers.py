# prime numbers

lower = int(input("enter starting range: "))
high = int(input("enter ending range: "))

primes = []

for i in range(lower,high+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        primes.append(i)

for idx in range(len(primes)):
    if idx == len(primes) - 1: print(primes[idx])
    else: print(primes[idx],end=',')

# dec to bin conversion
dec = int(input("Enter Decimal Number: "))
l = []
i = dec

while i != 0:
    l.append(str(i % 2))
    i //= 2
l = l[::-1]

binary = ''.join(l)
print(binary)