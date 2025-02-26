def remove_and_return(l: list, a):
    l2 = [element for element in l]
    try:
        l2.remove(a)
    except ValueError:
        pass
    return l2

def josephus(n: int, k: int):
    def gcd(a: int, b: int):
        if b == 0: return a
        return gcd(b, a % b)

    if n <= k:
        return f"{k = } is too big!"

    numbs = [j for j in range(1, n + 1)]
    i = 0
    while len(numbs) > 1:
        try:
            if len(numbs) == len(remove_and_return(numbs, (i * k) % n + 1)):
                break
            else:
                numbs = remove_and_return(numbs, (i * k) % n + 1)
            i += 1
        except ValueError:
            pass

    return sum(numbs) if len(numbs) == 1 else numbs

