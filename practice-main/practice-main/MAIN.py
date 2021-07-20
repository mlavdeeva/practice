import sys
from mainMenu import Ui_MainWindow
from THEORY import Ui_Theory
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow):  # класс главного окна (унаследует свойства QtWidgets.QMainWindow)

    def __init__(self):
        super(MyWindow, self).__init__()  # точное определение, что это родитель
        self.ui = Ui_MainWindow()  # достаём и присваиваем главное окно
        self.ui.setupUi(self)  # достаём компоненты из ui

        self.ui.theorybutton.clicked.connect(self.openTheory)

    def openTheory(self):
        theory = Theory(self)
        theory.exec_()

    def openFormula(self):
        pass

    def openCalc(self):
        pass


class Theory(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Theory, self).__init__(parent)
        self.uiTheory = Ui_Theory()  # достаём и присваиваем диалоговое окно
        self.uiTheory.setupUi(self)  # достаём компоненты из ui


App = QtWidgets.QApplication([])  # создаём рабочее пространство
application = MyWindow()  # создаём объект главного окна
application.show()  # отрисовка проекта
sys.exit(App.exec())  # завершение программы при закрытии окна
