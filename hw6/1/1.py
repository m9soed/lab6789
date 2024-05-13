from PySide6.QtWidgets import QMainWindow, QWidget, QListView, QLineEdit, QPushButton, QTabWidget, QApplication, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot


from noteListModel import NotesListModel
from note import Note
from notEmptyValidator import notEmptyValidator

        

class Window(QMainWindow):
    note_count = 1
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 700)

        tabs = QTabWidget(self)
        tabs.setMinimumSize(700, 700)

        # ADD NOTE TAB
        add_note_widget = QWidget(self)
        add_note_widget.setMinimumSize(500, 500)
        add_note_layout = QGridLayout(add_note_widget)
        self.text_field = QLineEdit(add_note_widget)
        self.text_field.setMinimumSize(300, 300)

        validator = notEmptyValidator(self.text_field)
        self.text_field.setValidator(validator)

        add_note_layout.addWidget(self.text_field, 0, 0)

        add_note_button = QPushButton(text="Add note", parent=add_note_widget)
        add_note_button.clicked.connect(self.add_note_button_clicked)
        add_note_layout.addWidget(add_note_button, 0, 1)
        tabs.addTab(add_note_widget, "Add")


        self.model = NotesListModel()
        self.model.add_note(Note(0, "test"))

        # LIST OF NOTES TAB
        notes_widget = QWidget()
        notes_widget.setMinimumSize(500, 500)

        self.notes_list = QListView(notes_widget)
        self.notes_list.setMinimumSize(500, 500)
        self.notes_list.clicked.connect(self.delete_note)
        self.notes_list.setModel(self.model)


        tabs.addTab(notes_widget, "List")


    @Slot()
    def add_note_button_clicked(self):
        text = self.text_field.text()
        if notEmptyValidator.validate_string(text):
            self.model.add_note(Note(self.note_count, text))
            self.note_count+=1
            self.text_field.clear()
        else:
            self.text_field.clearFocus()

    @Slot()
    def delete_note(self, model_index):
        self.model.del_note(model_index.model().get_note(model_index, Qt.ItemDataRole.DisplayRole))



if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()