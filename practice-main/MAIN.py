import sys
from mainMenu import UiMainWindow
from THEORY import Ui_Theory
from calculatorDialog import Ui_Calculator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout


class MyWindow(QtWidgets.QMainWindow):  # класс главного окна (унаследует свойства QtWidgets.QMainWindow)

    def __init__(self):
        super(MyWindow, self).__init__()  # точное определение, что это родитель
        self.ui = UiMainWindow()  # достаём и присваиваем главное окно
        self.ui.setupUi(self)  # достаём компоненты из ui

        self.ui.theorybutton.clicked.connect(self.opentheory)
        self.ui.pushButton_2.clicked.connect(self.opencalc)

    def opentheory(self):
        theory = Theory(self)
        theory.exec_()

    def openformula(self):
        pass

    def opencalc(self):
        calculator = Calculator(self)
        calculator.exec_()


class Theory(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Theory, self).__init__(parent)
        self.uiTheory = Ui_Theory()  # достаём и присваиваем диалоговое окно
        self.uiTheory.setupUi(self)  # достаём компоненты из ui


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
        self.frameOtkloneniye.setGeometry(QtCore.QRect(65, 200, 500, 200))  # Меняем размер и положение.
        self.frameOtkloneniye.setStyleSheet('background-color: rgb(255, 0, 255)')
        self.frameOtkloneniye.hide()

        self.frameDispersion = QFrame(self)
        self.frameDispersion.setGeometry(QtCore.QRect(65, 200, 500, 200))  # Меняем размер и положение.
        self.frameDispersion.setStyleSheet('background-color: rgb(100, 119, 111)')
        self.frameDispersion.hide()

        self.framePerestanovki = QFrame(self)
        self.framePerestanovki.setGeometry(QtCore.QRect(65, 200, 500, 200))  # Меняем размер и положение.
        self.framePerestanovki.setStyleSheet('background-color: rgb(0, 229, 228)')
        self.framePerestanovki.hide()

        self.frameMathojidanie = QFrame(self)
        self.frameMathojidanie.setGeometry(QtCore.QRect(65, 200, 500, 200))  # Меняем размер и положение.
        self.frameMathojidanie.setStyleSheet('background-color: rgb(200, 229, 100)')
        self.frameMathojidanie.hide()

        self.frameSochetanie = QFrame(self)
        self.frameSochetanie.setGeometry(QtCore.QRect(65, 200, 500, 200))  # Меняем размер и положение.
        self.frameSochetanie.setStyleSheet('background-color: rgb(300, 229, 228)')
        self.frameSochetanie.hide()

        self.frameRazmeshenie = QFrame(self)
        self.frameRazmeshenie.setGeometry(QtCore.QRect(65, 200, 500, 200))  # Меняем размер и положение.
        self.frameRazmeshenie.setStyleSheet('background-color: rgb(100, 200, 228)')
        self.frameRazmeshenie.hide()

        self.layoutPerestanovki = QVBoxLayout(self)
        self.layoutRazmeshenie = QVBoxLayout(self)
        self.layoutSochetanie = QVBoxLayout(self)
        self.layoutMathojidanie = QVBoxLayout(self)
        self.layoutDispersion = QVBoxLayout(self)
        self.layoutOtkloneniye = QVBoxLayout(self)

        self.lblPerestanovki = QLabel(self)
        self.lblPerestanovki.setText('проверка')
        self.lblPerestanovki.setGeometry(QtCore.QRect(65, 330, 900, 450))
        self.layoutPerestanovki.addWidget(self.lblPerestanovki)

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
