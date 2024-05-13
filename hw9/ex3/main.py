from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QGridLayout
from PySide6.QtGui import QIntValidator


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(400, 250)

        layoutMain = QGridLayout(self)

        self.num1 = QLineEdit()
        self.num1.setValidator(QIntValidator())
        layoutMain.addWidget(self.num1, 0, 0)
        self.num2 = QLineEdit()
        self.num2.setValidator(QIntValidator())
        layoutMain.addWidget(self.num2, 0, 1)

        plus = QPushButton("+")
        plus.clicked.connect(self.plusSlot)
        layoutMain.addWidget(plus, 1, 0)

        minus = QPushButton("-")
        minus.clicked.connect(self.minusSlot)
        layoutMain.addWidget(minus, 1, 1)

        multiplication = QPushButton("×")
        multiplication.clicked.connect(self.multiplicationSlot)
        layoutMain.addWidget(multiplication, 2, 0)

        division = QPushButton("/")
        division.clicked.connect(self.divisionSlot)
        layoutMain.addWidget(division, 2, 1)

        power = QPushButton("^")
        power.clicked.connect(self.powerSlot)
        layoutMain.addWidget(power, 3, 0, 2, 0)

        self.result = QLabel("Result: ")
        layoutMain.addWidget(self.result, 5, 0, 2, 0)


    @Slot()
    def plusSlot(self):
        a = self.num1.text()
        b = self.num2.text()
        try:
            self.result.setText(f"Result: {a} + {b} = {int(a)+int(b)}")
        except:
            self.result.setText("Error")

    @Slot()
    def minusSlot(self):
        a = self.num1.text()
        b = self.num2.text()
        try:
            self.result.setText(f"Result: {a} - {b} = {int(a)-int(b)}")
        except:
            self.result.setText("Error")

    @Slot()
    def multiplicationSlot(self):
        a = self.num1.text()
        b = self.num2.text()
        try:
            self.result.setText(f"Result: {a} × {b} = {int(a)*int(b)}")
        except:
            self.result.setText("Error")

    @Slot()
    def divisionSlot(self):
        a = self.num1.text()
        b = self.num2.text()
        try:
            self.result.setText(f"Result: {a} / {b} = {int(a)/int(b)}")
        except:
            self.result.setText("Error")

    @Slot()
    def powerSlot(self):
        a = self.num1.text()
        b = self.num2.text()
        try:
            self.result.setText(f"Result: {a}<sup>{b}</sup> = {int(a)**int(b)}")
        except:
            self.result.setText("Error")


if __name__=="__main__":
    app = QApplication([])
    window = Window()
    with open("style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    window.show()
    app.exec()