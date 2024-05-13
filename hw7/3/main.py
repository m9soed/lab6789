from PySide6.QtWidgets import QWidget, QWizard, QWizardPage, QLabel, QCheckBox, QApplication, QLineEdit, QGridLayout, QDialog, QDialogButtonBox, QMainWindow, QPushButton
from PySide6.QtCore import Slot


class Wizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wizard")
        
        self.addPage(LoginPage())
        self.addPage(NamePage())
        self.addPage(InterestsPage())

    def accept(self):
        return super().accept()



class LoginPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Логин и пароль")

        layout = QGridLayout(self)

        login_label = QLabel("Логин", self)
        login = QLineEdit(parent=self)
        passwd_label = QLabel("Пароль", self)
        passwd = QLineEdit(parent=self)

        layout.addWidget(login_label, 0, 0)
        layout.addWidget(login, 0, 1)
        layout.addWidget(passwd_label, 1, 0)
        layout.addWidget(passwd, 1, 1)

        self.registerField("login", login)
        self.registerField("passwd", passwd)


class NamePage(QWizardPage):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setTitle("Имя пользователя")

        name_label = QLabel("Имя", self)
        surname_label = QLabel("Фамилия", self)
        patronymic_label = QLabel("Отчество", self)
        name = QLineEdit(self)
        surname = QLineEdit(self)
        patronymic = QLineEdit(self)

        self.registerField("name", name)
        self.registerField("surname", surname)
        self.registerField("patronymic", patronymic)


        layout = QGridLayout(self)
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(surname_label, 1, 0)
        layout.addWidget(patronymic_label, 2, 0)
        layout.addWidget(name, 0, 1)
        layout.addWidget(surname, 1, 1)
        layout.addWidget(patronymic, 2, 1)


class InterestsPage(QWizardPage):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.setTitle("Интересы")
        layout = QGridLayout(self)

        football = QCheckBox("Футбол", self)
        cooking = QCheckBox("Рецепты и готовка", self)
        car = QCheckBox("Машины", self)

        agreement = QCheckBox("Согласен на рассылку", self)

        self.registerField("football", football)
        self.registerField("cooking", cooking)
        self.registerField("car", car)
        self.registerField("agreement", agreement)

        layout.addWidget(football, 0, 0)
        layout.addWidget(cooking, 1, 0)
        layout.addWidget(car, 2, 0)
        layout.addWidget(QLabel(""), 3, 0)
        layout.addWidget(QLabel(""), 4, 0)
        layout.addWidget(agreement, 5, 0)



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget(self)
        layout = QGridLayout(widget)

        self.wizard = Wizard(widget)
        start_wizard_button = QPushButton(text="open_wizard",parent=widget)
        self.info = QLabel("test", widget)

        start_wizard_button.clicked.connect(self.open_wizard)
        self.wizard.accepted.connect(self.show_info)

        self.setMinimumSize(700, 700)
        self.setCentralWidget(widget)
        widget.setMinimumSize(700, 700)

        layout.addWidget(start_wizard_button, 0, 0)
        layout.addWidget(self.info, 1, 0)


    @Slot()
    def open_wizard(self):
        self.wizard.open()
    
    @Slot()
    def show_info(self):
        self.info.setText(f"""Логин: {self.wizard.field("login")}
Пароль: {self.wizard.field("passwd")}
Имя: {self.wizard.field("name")}
Фамилия: {self.wizard.field("surname")}
Отчество: {self.wizard.field("patronymic")}
Футбол любит? {self.wizard.field("football")}
Готовить любит? {self.wizard.field("cooking")}
Тачки любит? {self.wizard.field("car")}
Согласен? {self.wizard.field("agreement")}""")






if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
        
