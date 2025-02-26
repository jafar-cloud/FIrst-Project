def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_digits(a):
    if a % 10 == a:
        return 1
    return count_digits(a // 10) + 1


def binary_search(numbers: list, a: int):
    mid_point = int((len(numbers)) / 2)
    if len(numbers) == 1:
        if a in numbers:
            print("a found at index 0")
            return
        print("a not found")
    else:
        if a < numbers[mid_point]:
            binary_search(numbers[:mid_point],a)
        elif a > numbers[mid_point]:
            binary_search(numbers[mid_point + 1:],a)
        else:
            print(f'a found at index {mid_point}')

binary_search([1,2,5], 2)
