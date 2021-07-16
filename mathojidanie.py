class MX:

    def __init__(self):
        self.x = []
        print('Вводите значения x, нажимайте enter\nДля окончания ввода нажмите enter')
        self.a = int(input('x-> '))
        while True:
            try:
                self.x.append(self.a)
                self.a = int(input('x-> '))
            except:
                break
        print(self.x)

        self.p = []
        print('Вводите значения p, нажимайте enter\nДля окончания ввода нажмите enter')
        self.a = float(input('p-> '))
        while True:
            try:
                self.p.append(self.a)
                self.a = float(input('p-> '))
            except:
                break
        print(self.p)

        finalResult = []

        for i in range(0, len(self.x)):
            result = (self.x[i] * self.p[i])
            for i in range(1):
                finalResult.append(result)
        print(sum(finalResult))


MX()
