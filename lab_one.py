
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("lab_one_design.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.lineEditA.setValidator(QtGui.QDoubleValidator())


def push():
    from math import cos, pi, sin, sqrt
    try:
        a = float(form.lineEditA.text().replace(',', '.'))

        z1 = cos((3 / 8) * pi - a / 4) ** 2 - cos((11 / 8) * pi + a / 4) ** 2
        print("{0:.1f} {1:.4f}".format(a, z1))
        form.lineEditZ1.setText(str(round(z1, 4)))

        z2 = (sqrt(2) / 2) * sin(a / 2)
        print("{0:.1f} {1:.4f}".format(a, z2))
        form.lineEditZ2.setText(str(round(z2, 4)))
    except:
        print("Ошибка ввода данных")


form.lineEditZ1.setReadOnly(True)
form.lineEditZ2.setReadOnly(True)

form.pushButton.clicked.connect(push)
form.pushButtonExit.clicked.connect(exit)
window.show()
app.exec()
