import sys
# импортируем формы (ui)
from mainMenu import Ui_MainWindow
from THEORY import Ui_TheoryW
from EXAMPLE import Ui_ExampleW
from calculatorDialog import Ui_Calculator
# импортируем модули с вычислениями

from allCalc import Perestanovki, Razmesheniya, Sochetanie, Mathojidanie, Dispersion, Otclonenie

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFrame, QLabel, qApp, QLineEdit, QGridLayout, QPushButton


class MyWindow(QtWidgets.QMainWindow):  # класс главного окна (унаследует свойства QtWidgets.QMainWindow)

    def __init__(self):
        super(MyWindow, self).__init__()  # точное определение, что это родитель
        self.ui = Ui_MainWindow()  # достаём и присваиваем главное окно
        self.ui.setupUi(self)  # достаём компоненты из ui

        self.ui.theorybutton.clicked.connect(self.opentheory)
        self.ui.calcBtn.clicked.connect(self.opencalc)
        self.ui.examplebutton.clicked.connect(self.openexample)
        self.ui.exitBtn.clicked.connect(qApp.quit)

    def opentheory(self):
        theory = Theory(self)
        theory.exec_()

    def openexample(self):
        example = Example(self)
        example.exec_()

    def opencalc(self):
        calculator = Calculator(self)
        calculator.exec_()


class Theory(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Theory, self).__init__(parent)
        self.uiTheory = Ui_TheoryW()  # достаём и присваиваем диалоговое окно
        self.uiTheory.setupUi(self)  # достаём компоненты из ui


class Example(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.uiExample = Ui_ExampleW()  # достаём и присваиваем диалоговое окно
        self.uiExample.setupUi(self)  # достаём компоненты из ui


class Calculator(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.uiCalc = Ui_Calculator()  # достаём и присваиваем диалоговое окно
        self.uiCalc.setupUi(self)  # достаём компоненты из ui

        # Для ввода только int-чисел и float-чисел
        self.validatorInt = QtGui.QIntValidator(self)
        self.validatorFloat = QtGui.QDoubleValidator(self)

        self.uiCalc.BtnPerestanovki.clicked.connect(self.showFramePerestanovki)
        self.uiCalc.BtnRazmeshenie.clicked.connect(self.showFrameRazmeshenie)
        self.uiCalc.BtnSochetanie.clicked.connect(self.showFrameSochetanie)
        self.uiCalc.BtnMathojidanie.clicked.connect(self.showFrameMathojidanie)
        self.uiCalc.BtnDispersion.clicked.connect(self.showFrameDispersion)
        self.uiCalc.BtnOtkloneniye.clicked.connect(self.showFrameOtkloneniye)

        self.frameOtkloneniye = QFrame(self)
        self.frameOtkloneniye.setGeometry(QtCore.QRect(170, 300, 736, 200))  # Меняем размер и положение.
        self.frameOtkloneniye.setStyleSheet('background-color: rgb(255, 229, 228)')
        self.frameOtkloneniye.hide()

        self.frameDispersion = QFrame(self)
        self.frameDispersion.setGeometry(QtCore.QRect(170, 300, 736, 200))  # Меняем размер и положение.
        self.frameDispersion.setStyleSheet('background-color: rgb(255, 229, 228)')
        self.frameDispersion.hide()

        self.framePerestanovki = QFrame(self)
        self.framePerestanovki.setGeometry(QtCore.QRect(170, 300, 736, 200))  # Меняем размер и положение.
        self.framePerestanovki.setStyleSheet('background-color: rgb(255, 229, 228)')
        self.framePerestanovki.hide()

        self.frameMathojidanie = QFrame(self)
        self.frameMathojidanie.setGeometry(QtCore.QRect(170, 300, 736, 200))  # Меняем размер и положение.
        self.frameMathojidanie.setStyleSheet('background-color: rgb(255, 229, 228)')
        self.frameMathojidanie.hide()

        self.frameSochetanie = QFrame(self)
        self.frameSochetanie.setGeometry(QtCore.QRect(170, 300, 736, 200))  # Меняем размер и положение.
        self.frameSochetanie.setStyleSheet('background-color: rgb(255, 229, 228)')
        self.frameSochetanie.hide()

        self.frameRazmeshenie = QFrame(self)
        self.frameRazmeshenie.setGeometry(QtCore.QRect(170, 300, 736, 200))  # Меняем размер и положение.
        self.frameRazmeshenie.setStyleSheet('background-color: rgb(255, 229, 228)')
        self.frameRazmeshenie.hide()

        self.layoutPerestanovki = QGridLayout(self)
        self.layoutRazmeshenie = QGridLayout(self)
        self.layoutSochetanie = QGridLayout(self)
        self.layoutMathojidanie = QGridLayout(self)
        self.layoutDispersion = QGridLayout(self)
        self.layoutOtkloneniye = QGridLayout(self)

        self.lblPerestanovki = QLabel(self)
        self.lblPerestanovki.setText('Введите число n и нажимайте на кнопку Вычислить:')
        self.lblPerestanovki.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutPerestanovki.addWidget(self.lblPerestanovki, 0, 0)

        self.lblPerestanovki1 = QLabel(self)
        self.lblPerestanovki1.setText('Ответ:')
        self.lblPerestanovki1.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutPerestanovki.addWidget(self.lblPerestanovki1, 1, 0)

        self.lblPerestanovki2 = QLabel(self)
        self.lblPerestanovki2.setText('')
        self.lblPerestanovki2.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutPerestanovki.addWidget(self.lblPerestanovki2, 1, 1)

        self.lePerestanovki = QLineEdit(self)
        self.lePerestanovki.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.lePerestanovki.setFixedWidth(200)
        self.lePerestanovki.setValidator(self.validatorInt)  # разрешается ввод только целых чисел
        self.layoutPerestanovki.addWidget(self.lePerestanovki, 0, 1)

        self.BtnCalcPerestanokvi = QPushButton(self)
        self.BtnCalcPerestanokvi.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcPerestanokvi.setText("Вычислить")
        self.BtnCalcPerestanokvi.clicked.connect(self.calcPerestanovki)
        self.layoutPerestanovki.addWidget(self.BtnCalcPerestanokvi, 0, 2)

        self.lblRazmeshenie = QLabel(self)
        self.lblRazmeshenie.setText('Введите числа n и k,\nнажимайте на кнопку Вычислить:')
        self.lblRazmeshenie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutRazmeshenie.addWidget(self.lblRazmeshenie, 0, 0)

        self.lblRazmeshenie = QLabel(self)
        self.lblRazmeshenie.setText('                      n =  ')
        self.lblRazmeshenie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutRazmeshenie.addWidget(self.lblRazmeshenie, 0, 1)

        self.lblRazmeshenie = QLabel(self)
        self.lblRazmeshenie.setText('                      k =  ')
        self.lblRazmeshenie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutRazmeshenie.addWidget(self.lblRazmeshenie, 1, 1)

        self.lblRazmeshenie = QLabel(self)
        self.lblRazmeshenie.setText('Ответ:')
        self.lblRazmeshenie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutRazmeshenie.addWidget(self.lblRazmeshenie, 2, 1)

        self.lblRazmeshenie1 = QLabel(self)
        self.lblRazmeshenie1.setText('')
        self.lblRazmeshenie1.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutRazmeshenie.addWidget(self.lblRazmeshenie1, 2, 2)

        self.leRazmeshenie = QLineEdit(self)
        self.leRazmeshenie.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leRazmeshenie.setFixedWidth(200)
        self.leRazmeshenie.setValidator(self.validatorInt)  # разрешается ввод только целых чисел
        self.layoutRazmeshenie.addWidget(self.leRazmeshenie, 0, 2)

        self.leRazmeshenie1 = QLineEdit(self)
        self.leRazmeshenie1.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leRazmeshenie1.setFixedWidth(200)
        self.leRazmeshenie1.setValidator(self.validatorInt)  # разрешается ввод только целых чисел
        self.layoutRazmeshenie.addWidget(self.leRazmeshenie1, 1, 2)

        self.BtnCalcRazmeshenie = QPushButton(self)
        self.BtnCalcRazmeshenie.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcRazmeshenie.setText("Вычислить")
        self.BtnCalcRazmeshenie.clicked.connect(self.calcRazmeshenie)
        self.layoutRazmeshenie.addWidget(self.BtnCalcRazmeshenie, 0, 3)

        self.lblSochetanie = QLabel(self)
        self.lblSochetanie.setText('Введите числа n и k,\nнажимайте на кнопку Вычислить:')
        self.lblSochetanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutSochetanie.addWidget(self.lblSochetanie, 0, 0)

        self.lblSochetanie = QLabel(self)
        self.lblSochetanie.setText('                      n =  ')
        self.lblSochetanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutSochetanie.addWidget(self.lblSochetanie, 0, 1)

        self.lblSochetanie = QLabel(self)
        self.lblSochetanie.setText('                      k =  ')
        self.lblSochetanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutSochetanie.addWidget(self.lblSochetanie, 1, 1)

        self.lblSochetanie = QLabel(self)
        self.lblSochetanie.setText('Ответ: ')
        self.lblSochetanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutSochetanie.addWidget(self.lblSochetanie, 2, 1)

        self.lblSochetanie1 = QLabel(self)
        self.lblSochetanie1.setText('')
        self.lblSochetanie1.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutSochetanie.addWidget(self.lblSochetanie1, 2, 2)

        self.leSochetanie = QLineEdit(self)
        self.leSochetanie.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leSochetanie.setFixedWidth(200)
        self.leSochetanie.setValidator(self.validatorInt)  # разрешается ввод только целых чисел
        self.layoutSochetanie.addWidget(self.leSochetanie, 0, 2)

        self.leSochetanie1 = QLineEdit(self)
        self.leSochetanie1.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leSochetanie1.setFixedWidth(200)
        self.leSochetanie1.setValidator(self.validatorInt)  # разрешается ввод только целых чисел
        self.layoutSochetanie.addWidget(self.leSochetanie1, 1, 2)

        self.BtnCalcSochetanie = QPushButton(self)
        self.BtnCalcSochetanie.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcSochetanie.setText("Вычислить")
        self.BtnCalcSochetanie.clicked.connect(self.calcSochetanie)
        self.layoutSochetanie.addWidget(self.BtnCalcSochetanie, 0, 3)

        self.lblMathojidanie = QLabel(self)
        self.lblMathojidanie.setText('Введите через пробел Xi и Pi,\nнажимайте на кнопку Вычислить:')
        self.lblMathojidanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutMathojidanie.addWidget(self.lblMathojidanie, 0, 0)

        self.lblMathojidanie = QLabel(self)
        self.lblMathojidanie.setText('                      Xi =  ')
        self.lblMathojidanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutMathojidanie.addWidget(self.lblMathojidanie, 0, 1)

        self.lblMathojidanie = QLabel(self)
        self.lblMathojidanie.setText('                      Pi =  ')
        self.lblMathojidanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutMathojidanie.addWidget(self.lblMathojidanie, 1, 1)

        self.lblMathojidanie = QLabel(self)
        self.lblMathojidanie.setText('Ответ: ')
        self.lblMathojidanie.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutMathojidanie.addWidget(self.lblMathojidanie, 2, 1)

        self.lblMathojidanie1 = QLabel(self)
        self.lblMathojidanie1.setText('')
        self.lblMathojidanie1.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutMathojidanie.addWidget(self.lblMathojidanie1, 2, 2)

        self.leMathojidanie = QLineEdit(self)
        self.leMathojidanie.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leMathojidanie.setFixedWidth(200)
        self.layoutMathojidanie.addWidget(self.leMathojidanie, 0, 2)

        self.leMathojidanie1 = QLineEdit(self)
        self.leMathojidanie1.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leMathojidanie1.setFixedWidth(200)
        self.layoutMathojidanie.addWidget(self.leMathojidanie1, 1, 2)

        self.BtnCalcMathojidanie = QPushButton(self)
        self.BtnCalcMathojidanie.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcMathojidanie.setText("Вычислить")
        self.BtnCalcMathojidanie.clicked.connect(self.calcMathojidanie)
        self.layoutMathojidanie.addWidget(self.BtnCalcMathojidanie, 0, 3)

        self.lblDispersion = QLabel(self)
        self.lblDispersion.setText('Введите через пробел Xi и Pi,\nнажимайте на кнопку Вычислить:')
        self.lblDispersion.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutDispersion.addWidget(self.lblDispersion, 0, 0)

        self.lblDispersion = QLabel(self)
        self.lblDispersion.setText('                      Xi =  ')
        self.lblDispersion.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutDispersion.addWidget(self.lblDispersion, 0, 1)

        self.lblDispersion = QLabel(self)
        self.lblDispersion.setText('                      Pi =  ')
        self.lblDispersion.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutDispersion.addWidget(self.lblDispersion, 1, 1)

        self.lblDispersion = QLabel(self)
        self.lblDispersion.setText('Ответ: ')
        self.lblDispersion.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutDispersion.addWidget(self.lblDispersion, 2, 1)

        self.lblDispersion1 = QLabel(self)
        self.lblDispersion1.setText('')
        self.lblDispersion1.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutDispersion.addWidget(self.lblDispersion1, 2, 2)

        self.leDispersion = QLineEdit(self)
        self.leDispersion.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leDispersion.setFixedWidth(200)
        self.layoutDispersion.addWidget(self.leDispersion, 0, 2)

        self.leDispersion1 = QLineEdit(self)
        self.leDispersion1.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leDispersion1.setFixedWidth(200)
        self.layoutDispersion.addWidget(self.leDispersion1, 1, 2)

        self.BtnCalcDispersion = QPushButton(self)
        self.BtnCalcDispersion.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcDispersion.setText("Вычислить")
        self.BtnCalcDispersion.clicked.connect(self.calcDispersion)
        self.layoutDispersion.addWidget(self.BtnCalcDispersion, 0, 3)

        self.lblOtkloneniye = QLabel(self)
        self.lblOtkloneniye.setText('Введите через пробел Xi и Pi,\nнажимайте на кнопку Вычислить:')
        self.lblOtkloneniye.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutOtkloneniye.addWidget(self.lblOtkloneniye, 0, 0)

        self.lblOtkloneniye = QLabel(self)
        self.lblOtkloneniye.setText('                      Xi =  ')
        self.lblOtkloneniye.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutOtkloneniye.addWidget(self.lblOtkloneniye, 0, 1)

        self.lblOtkloneniye = QLabel(self)
        self.lblOtkloneniye.setText('                      Pi =  ')
        self.lblOtkloneniye.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutOtkloneniye.addWidget(self.lblOtkloneniye, 1, 1)

        self.lblOtkloneniye = QLabel(self)
        self.lblOtkloneniye.setText('Ответ: ')
        self.lblOtkloneniye.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutOtkloneniye.addWidget(self.lblOtkloneniye, 2, 1)

        self.lblOtkloneniye1 = QLabel(self)
        self.lblOtkloneniye1.setText('')
        self.lblOtkloneniye1.setGeometry(QtCore.QRect(0, 0, 700, 10))
        self.layoutOtkloneniye.addWidget(self.lblOtkloneniye1, 2, 2)

        self.leOtkloneniye = QLineEdit(self)
        self.leOtkloneniye.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leOtkloneniye.setFixedWidth(200)
        self.layoutOtkloneniye.addWidget(self.leOtkloneniye, 0, 2)

        self.leOtkloneniye1 = QLineEdit(self)
        self.leOtkloneniye1.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leOtkloneniye1.setFixedWidth(200)
        self.layoutOtkloneniye.addWidget(self.leOtkloneniye1, 1, 2)

        self.BtnCalcOtkloneniye = QPushButton(self)
        self.BtnCalcOtkloneniye.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcOtkloneniye.setText("Вычислить")
        self.BtnCalcOtkloneniye.clicked.connect(self.calcOtclonenie)
        self.layoutOtkloneniye.addWidget(self.BtnCalcOtkloneniye, 0, 3)

        self.framePerestanovki.setLayout(self.layoutPerestanovki)
        self.frameRazmeshenie.setLayout(self.layoutRazmeshenie)
        self.frameSochetanie.setLayout(self.layoutSochetanie)
        self.frameMathojidanie.setLayout(self.layoutMathojidanie)
        self.frameDispersion.setLayout(self.layoutDispersion)
        self.frameOtkloneniye.setLayout(self.layoutOtkloneniye)

        # self.uiCalc.BtnPerestanovki
        # self.uiCalc.BtnRazmeshenie
        # self.uiCalc.BtnSochetanie
        # self.uiCalc.BtnMathojidanie
        # self.uiCalc.BtnDispersion
        # self.uiCalc.BtnOtkloneniye

    def showFramePerestanovki(self):
        self.framePerestanovki.show()
        self.frameRazmeshenie.hide()
        self.frameSochetanie.hide()
        self.frameMathojidanie.hide()
        self.frameDispersion.hide()
        self.frameOtkloneniye.hide()

        # скрываем фрейм через hide

    def showFrameRazmeshenie(self):
        self.frameRazmeshenie.show()
        self.framePerestanovki.hide()
        self.frameSochetanie.hide()
        self.frameMathojidanie.hide()
        self.frameDispersion.hide()
        self.frameOtkloneniye.hide()

    def showFrameSochetanie(self):
        self.frameSochetanie.show()
        self.framePerestanovki.hide()
        self.frameRazmeshenie.hide()
        self.frameMathojidanie.hide()
        self.frameDispersion.hide()
        self.frameOtkloneniye.hide()

    def showFrameMathojidanie(self):
        self.frameMathojidanie.show()
        self.frameRazmeshenie.hide()
        self.frameSochetanie.hide()
        self.framePerestanovki.hide()
        self.frameDispersion.hide()
        self.frameOtkloneniye.hide()

    def showFrameDispersion(self):
        self.frameDispersion.show()
        self.frameRazmeshenie.hide()
        self.frameSochetanie.hide()
        self.framePerestanovki.hide()
        self.frameMathojidanie.hide()
        self.frameOtkloneniye.hide()

    def showFrameOtkloneniye(self):
        self.frameOtkloneniye.show()
        self.frameRazmeshenie.hide()
        self.frameSochetanie.hide()
        self.framePerestanovki.hide()
        self.frameMathojidanie.hide()
        self.frameDispersion.hide()

    # при нажатии на кнопку вычислить обращаемся к данным функциям
    def calcPerestanovki(self):
        self.lblPerestanovki2.setText(str(Perestanovki(int(self.lePerestanovki.text()))))

    def calcRazmeshenie(self):
        self.lblRazmeshenie1.setText(str(Razmesheniya(int(self.leRazmeshenie.text()), int(self.leRazmeshenie1.text()))))

    def calcSochetanie(self):
        self.lblSochetanie1.setText(str(Sochetanie(int(self.leSochetanie.text()), int(self.leSochetanie1.text()))))

    def calcMathojidanie(self):
        x = (self.leMathojidanie.text()).split()
        for i in range(len(x)):
            x[i] = int(x[i])

        p = (self.leMathojidanie1.text()).split()
        for i in range(len(p)):
            p[i] = float(p[i])

        self.lblMathojidanie1.setText(str(Mathojidanie(x, p)))

    def calcDispersion(self):
        x = (self.leDispersion.text()).split()
        for i in range(len(x)):
            x[i] = int(x[i])

        p = (self.leDispersion1.text()).split()
        for i in range(len(p)):
            p[i] = float(p[i])

        self.lblDispersion1.setText(str(Dispersion(x, p)))
        print(x, p)


    def calcOtclonenie(self):
        x = (self.leOtkloneniye.text()).split()
        for i in range(len(x)):
            x[i] = int(x[i])

        p = (self.leOtkloneniye1.text()).split()
        for i in range(len(p)):
            p[i] = float(p[i])

        self.lblOtkloneniye1.setText(str(Otclonenie(x, p)))
        print(x, p)


App = QtWidgets.QApplication([])  # создаём рабочее пространство
application = MyWindow()  # создаём объект главного окна
application.show()  # отрисовка проекта
sys.exit(App.exec())  # завершение программы при закрытии окна
