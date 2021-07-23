import math


# функция получает int
def Perestanovki(n):
    return math.factorial(n)


# функция получает 2 int
def Razmesheniya(n, m):
    if m > n:
        return 'K не может быть больше N'
    else:
        nm = n - m
        nF = (math.factorial(n))
        nmF = (math.factorial(nm))

        a = nF / nmF
        return a


# функция получает 2 int
def Sochetanie(n, k):
    if k > n:
        return 'K не может быть больше N'
    else:
        nFact = (math.factorial(n))
        kFact = (math.factorial(k))
        nk = n - k
        nkFact = (math.factorial(nk))
        c = (nFact / (nkFact * kFact))
        return c

# функция получает 2 массива типа float
def Mathojidanie(x, p):
    """x = []
    print('Вводите значения x, нажимайте enter\nДля окончания ввода нажмите enter')
    a = int(input('x-> '))
    while True:
        try:
            x.append(a)
            a = int(input('x-> '))
        except:
            break
    print(x)

    p = []
    print('Вводите значения p, нажимайте enter\nДля окончания ввода нажмите enter')
    a = float(input('p-> '))
    while True:
        try:
            p.append(a)
            a = float(input('p-> '))
        except:
            break
    print(p)
    """
    finalResult = []

    for i in range(len(x)):
        result = (x[i] * p[i])
        finalResult.append(result)
    return sum(finalResult)

# функция получает 2 массива типа float
def Dispersion(x, p):
    """
    print('Вводите значения x, нажимайте enter\nДля окончания ввода нажмите enter')

    a = int(input('x-> '))
    x = []
    while True:
        try:
            x.append(a)
            a = int(input('x-> '))
        except:
            break

    print(x)

    xcvdr = [i ** 2 for i in x]

    print(xcvdr)

    print('Вводите значения p, нажимайте enter\nДля окончания ввода нажмите enter')

    a = float(input('p-> '))
    p = []
    while True:
        try:
            p.append(a)
            a = float(input('p-> '))
        except:
            break
    print(p)
    """
    xcvdr = [i ** 2 for i in x]
    finalResult1 = []
    finalResult2 = []

    for i in range(len(x)):
        result = (xcvdr[i] * p[i])
        finalResult1.append(result)
    print(sum(finalResult1))

    for i in range(len(x)):
        result = (x[i] * p[i])
        finalResult2.append(result)
    print(sum(finalResult2))

    return sum(finalResult1) - (sum(finalResult2) ** 2)

# функция получает 2 массива типа float
def Otclonenie(x, p):
    """
    print('Вводите значения x, нажимайте enter\nДля окончания ввода нажмите enter')

    a = int(input('x-> '))
    x = []
    while True:
        try:
            x.append(a)
            a = int(input('x-> '))
        except:
            break

    print(x)

    xcvdr = [i ** 2 for i in x]

    print(xcvdr)

    print('Вводите значения p, нажимайте enter\nДля окончания ввода нажмите enter')

    a = float(input('p-> '))
    p = []
    while True:
        try:
            p.append(a)
            a = float(input('p-> '))
        except:
            break
    print(p)
    """
    xcvdr = [i ** 2 for i in x]
    finalResult1 = []
    finalResult2 = []

    for i in range(len(x)):
        result = (xcvdr[i] * p[i])
        finalResult1.append(result)
    print(sum(finalResult1))

    for i in range(0, len(x)):
        result = (x[i] * p[i])
        for i in range(1):
            finalResult2.append(result)
    print(sum(finalResult2))

    otvet = (sum(finalResult1) - (sum(finalResult2) ** 2))
    return otvet ** (1 / 2)
