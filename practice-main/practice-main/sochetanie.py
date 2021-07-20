import math


class S:
    n = int(input("n = "))
    k = int(input("k = "))
    nFact = (math.factorial(n))
    kFact = (math.factorial(k))
    nk = n - k
    nkFact = (math.factorial(nk))
    c = (nFact / (nkFact * kFact))
    print(c)
