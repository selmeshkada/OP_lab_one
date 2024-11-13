
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication
Form, Window = uic.loadUiType("lab_four_design.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.lineEditX.setValidator(QtGui.QDoubleValidator())
form.lineEditY.setValidator(QtGui.QDoubleValidator())
form.lineEditR.setValidator(QtGui.QDoubleValidator())

rez = "Попадает в область"
not_rez = "Не попадает в область"


def pryam(x, y, r):
    if (0 <= x <= 2*r) and (-r <= y <= 0):
        return 1


def circle(x, y, r):
    if ((x + r) ** 2 + (y - r) ** 2) <= r ** 2:
        return 1


def push():
    x = float(form.lineEditX.text().replace(',','.'))
    y = float(form.lineEditY.text().replace(',','.'))
    r = float(form.lineEditR.text().replace(',','.'))

    if pryam(x, y, r) == 1:
        print("Попадает в область")
        form.labelPryam.move(270, 355)
        form.labelPryam.setText(rez)
    else:
        if circle(x, y, r) == 1:
            print("Попадает в область")
            form.labelPryam.move(110, 240)
            form.labelPryam.setText(rez)
        else:
            print("Не попадает в область")
            form.labelPryam.move(550, 330)
            form.labelPryam.setText(not_rez)


form.pushButton_2.clicked.connect(push)
form.pushButtonExit.clicked.connect(exit)
window.show()
app.exec()
