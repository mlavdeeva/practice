import sys
from mainMenu import Ui_MainWindow
from THEORY import Ui_TheoryW
from EXAMPLE import Ui_ExampleW
from calculatorDialog import Ui_Calculator
from PyQt5 import QtCore, QtWidgets
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

        self.uiCalc.BtnPerestanovki.clicked.connect(self.showFramePerestanovki)
        self.uiCalc.BtnRazmeshenie.clicked.connect(self.showFrameRazmeshenie)
        self.uiCalc.BtnSochetanie.clicked.connect(self.showFrameSochetanie)
        self.uiCalc.BtnMathojidanie.clicked.connect(self.showFrameMathojidanie)
        self.uiCalc.BtnDispersion.clicked.connect(self.showFrameDispersion)
        self.uiCalc.BtnOtkloneniye.clicked.connect(self.showFrameOtkloneniye)

        self.frameOtkloneniye = QFrame(self)
        self.frameOtkloneniye.setGeometry(QtCore.QRect(170, 300, 736, 300))  # Меняем размер и положение.
        self.frameOtkloneniye.setStyleSheet('background-color: rgb(255, 0, 255)')
        self.frameOtkloneniye.hide()

        self.frameDispersion = QFrame(self)
        self.frameDispersion.setGeometry(QtCore.QRect(170, 300, 736, 300))  # Меняем размер и положение.
        self.frameDispersion.setStyleSheet('background-color: rgb(100, 119, 111)')
        self.frameDispersion.hide()

        self.framePerestanovki = QFrame(self)
        self.framePerestanovki.setGeometry(QtCore.QRect(170, 300, 736, 300))  # Меняем размер и положение.
        self.framePerestanovki.setStyleSheet('background-color: rgb(0, 229, 228)')
        self.framePerestanovki.hide()

        self.frameMathojidanie = QFrame(self)
        self.frameMathojidanie.setGeometry(QtCore.QRect(170, 300, 736, 300))  # Меняем размер и положение.
        self.frameMathojidanie.setStyleSheet('background-color: rgb(200, 229, 100)')
        self.frameMathojidanie.hide()

        self.frameSochetanie = QFrame(self)
        self.frameSochetanie.setGeometry(QtCore.QRect(170, 300, 736, 300))  # Меняем размер и положение.
        self.frameSochetanie.setStyleSheet('background-color: rgb(200, 229, 228)')
        self.frameSochetanie.hide()

        self.frameRazmeshenie = QFrame(self)
        self.frameRazmeshenie.setGeometry(QtCore.QRect(170, 300, 736, 300))  # Меняем размер и положение.
        self.frameRazmeshenie.setStyleSheet('background-color: rgb(100, 200, 228)')
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

        self.lePerestanovki = QLineEdit(self)
        self.lePerestanovki.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.lePerestanovki.setFixedWidth(200)
        self.layoutPerestanovki.addWidget(self.lePerestanovki, 0, 1)

        self.BtnCalcPerestanokvi = QPushButton(self)
        self.BtnCalcPerestanokvi.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcPerestanokvi.setText("Вычислить")
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

        self.leRazmeshenie = QLineEdit(self)
        self.leRazmeshenie.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leRazmeshenie.setFixedWidth(200)
        self.layoutRazmeshenie.addWidget(self.leRazmeshenie, 0, 2)

        self.leRazmeshenie = QLineEdit(self)
        self.leRazmeshenie.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leRazmeshenie.setFixedWidth(200)
        self.layoutRazmeshenie.addWidget(self.leRazmeshenie, 1, 2)

        self.BtnCalcRazmeshenie = QPushButton(self)
        self.BtnCalcRazmeshenie.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcRazmeshenie.setText("Вычислить")
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

        self.leSochetanie = QLineEdit(self)
        self.leSochetanie.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leSochetanie.setFixedWidth(200)
        self.layoutSochetanie.addWidget(self.leSochetanie, 0, 2)

        self.leSochetanie = QLineEdit(self)
        self.leSochetanie.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leSochetanie.setFixedWidth(200)
        self.layoutSochetanie.addWidget(self.leSochetanie, 1, 2)

        self.BtnCalcSochetanie = QPushButton(self)
        self.BtnCalcSochetanie.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcSochetanie.setText("Вычислить")
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

        self.leMathojidanie = QLineEdit(self)
        self.leMathojidanie.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leMathojidanie.setFixedWidth(200)
        self.layoutMathojidanie.addWidget(self.leMathojidanie, 0, 2)

        self.leMathojidanie = QLineEdit(self)
        self.leMathojidanie.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leMathojidanie.setFixedWidth(200)
        self.layoutMathojidanie.addWidget(self.leMathojidanie, 1, 2)

        self.BtnCalcMathojidanie = QPushButton(self)
        self.BtnCalcMathojidanie.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcMathojidanie.setText("Вычислить")
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

        self.leDispersion = QLineEdit(self)
        self.leDispersion.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leDispersion.setFixedWidth(200)
        self.layoutDispersion.addWidget(self.leDispersion, 0, 2)

        self.leDispersion = QLineEdit(self)
        self.leDispersion.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leDispersion.setFixedWidth(200)
        self.layoutDispersion.addWidget(self.leDispersion, 1, 2)

        self.BtnCalcDispersion = QPushButton(self)
        self.BtnCalcDispersion.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcDispersion.setText("Вычислить")
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

        self.leOtkloneniye = QLineEdit(self)
        self.leOtkloneniye.setGeometry(QtCore.QRect(10, 90, 0, 0))
        self.leOtkloneniye.setFixedWidth(200)
        self.layoutOtkloneniye.addWidget(self.leOtkloneniye, 0, 2)

        self.leOtkloneniye = QLineEdit(self)
        self.leOtkloneniye.setGeometry(QtCore.QRect(10, 90, 50, 50))
        self.leOtkloneniye.setFixedWidth(200)
        self.layoutOtkloneniye.addWidget(self.leOtkloneniye, 1, 2)

        self.BtnCalcOtkloneniye = QPushButton(self)
        self.BtnCalcOtkloneniye.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.BtnCalcOtkloneniye.setText("Вычислить")
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


App = QtWidgets.QApplication([])  # создаём рабочее пространство
application = MyWindow()  # создаём объект главного окна
application.show()  # отрисовка проекта
sys.exit(App.exec())  # завершение программы при закрытии окна
