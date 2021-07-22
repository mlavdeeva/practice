import math


class Razmesheniya:
    n = int(input("n = "))
    m = int(input("m = "))
    if m > n:
        print('K не может быть больше N')
    nm = n - m
    nF = (math.factorial(n))
    nmF = (math.factorial(nm))

    a = nF / nmF
    print(a)
