from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget



class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Кнопка")

        layout = QVBoxLayout(self)

        encrease = QPushButton("+")
        encrease.clicked.connect(self.increaseCounter)
        layout.addWidget(encrease)

        decrease = QPushButton("-")
        decrease.clicked.connect(self.decreaseCounter)
        layout.addWidget(decrease)

        self.counter = QLabel()
        self.counter.setNum(0)
        layout.addWidget(self.counter)

    @Slot()
    def increaseCounter(self):
        self.counter.setNum(int(self.counter.text()) + 1)

    @Slot()
    def decreaseCounter(self):
        self.counter.setNum(int(self.counter.text()) - 1)



if __name__=="__main__":
    app = QApplication([])
    window = Window()
    with open("style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    window.resize(400, 400)
    window.show()
    app.exec()