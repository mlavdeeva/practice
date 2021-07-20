class DX(object):

    def __init__(self):
        print('Вводите значения x, нажимайте enter\nДля окончания ввода нажмите enter')

        self.a = int(input('x-> '))
        self.x = []
        while True:
            try:
                self.x.append(self.a)
                self.a = int(input('x-> '))
            except:
                break

        print(self.x)

        self.xcvdr = [i ** 2 for i in self.x]

        print(self.xcvdr)

        print('Вводите значения p, нажимайте enter\nДля окончания ввода нажмите enter')

        self.a = float(input('p-> '))
        self.p = []
        while True:
            try:
                self.p.append(self.a)
                self.a = float(input('p-> '))
            except:
                break
        print(self.p)

        finalResult1 = []
        finalResult2 = []

        for i in range(0, len(self.x)):
            result = (self.xcvdr[i] * self.p[i])
            for i in range(1):
                finalResult1.append(result)
        print(sum(finalResult1))

        for i in range(0, len(self.x)):
            result = (self.x[i] * self.p[i])
            for i in range(1):
                finalResult2.append(result)
        print(sum(finalResult2))

        self.otvet = (sum(finalResult1) - (sum(finalResult2) ** 2))
        self.finotvet = self.otvet**(1/2)
        print(self.finotvet)


DX()

