from PySide6.QtWidgets import QMainWindow, QApplication, QGridLayout, QCheckBox, QPushButton, QWidget, QDialog, QLabel
from PySide6.QtCore import Slot


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 700)

        widget = QWidget(self)
        layout = QGridLayout(widget)
        self.setCentralWidget(widget)

        self.state = QLabel("", widget)
        layout.addWidget(self.state, 0, 0)

        button = QPushButton("Click me")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(button, 1, 0)

        self.dialog = Dialog()
        self.dialog.checkbox.stateChanged.connect(self.checkbox_state_changed)
        # self.dialog.checkbox_state_changed

    @Slot()
    def button_clicked(self):
        self.dialog.open()
    
    @Slot()
    def checkbox_state_changed(self):
        if self.dialog.checkbox.checkState().value == 2:
            self.state.setText("Выбран")
        else: 
            self.state.setText("Не выбран")


class Dialog(QDialog):
    # signal = Signal(str)
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.checkbox = QCheckBox("Соглашаюсь", self)
        layout.addWidget(self.checkbox, 0, 0)

        button = QPushButton("Close")
        layout.addWidget(button, 1, 0)
        button.clicked.connect(self.close_dialog)



    @Slot()
    def close_dialog(self):
        self.close()






if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()