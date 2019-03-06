def czynnikiPierwsze(n):
    czynPier = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            czynPier.append(d)
            n //= d
        d += 1
    if n > 1:
        czynPier.append(n)
    return czynPier


hejka=(list(czynnikiPierwsze(8)))

def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

print (checkEqual1(hejka))
