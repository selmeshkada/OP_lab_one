
import math

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("lab_two_design.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.lineEditX.setValidator(QtGui.QDoubleValidator())
form.lineEditY.setValidator(QtGui.QDoubleValidator())


def zero(z):
    return not (z == 0)


def zero_or(z):
    return (z >= 0)
   


def push():
    from math import cos, log10, sin, sqrt, e
    x = float(form.lineEditX.text().replace(',', '.'))
    y = float(form.lineEditY.text().replace(',', '.'))

    try:
        if zero(y)+zero(x + y)+zero(x*y) == 3:
            d = ((math.e ** x) ** (1 / y) - log10(abs(x * y))) / (x + y)
        if zero_or(x * y):
            c = (d ** (sqrt(x * y))) + (math.e ** d)
        b = cos(c) ** 2 + sin(d) ** 2
        a = e ** (b + c + d)

    except:
        print("Ошибка ввода данных")
        form.lineEditA.setText("Ошибка ввода данных")


    else:
        print("{0:.1f} {1:.1f} {2:.4f}".format(x, y, a))
        form.lineEditA.setText(str(round(a, 4)))


form.lineEditA.setReadOnly(True)

form.pushButton_2.clicked.connect(push)
form.pushButtonExit.clicked.connect(exit)
window.show()
app.exec()
