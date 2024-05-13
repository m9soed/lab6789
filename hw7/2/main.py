from PySide6.QtWidgets import QMainWindow, QWidget, QListView, QLineEdit, QPushButton, QTabWidget, QApplication, QGridLayout, QDialog, QDialogButtonBox, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot, Signal


from noteListModel import NotesListModel
from note import Note

        

class Window(QMainWindow):
    note_count = 1
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 700)
        self.add_menu()

        # LIST OF NOTES TAB
        # model
        self.model = NotesListModel()
        self.model.add_note(Note("test"))
        notes_widget = QWidget()
        self.setCentralWidget(notes_widget)
        notes_widget.setMinimumSize(700, 700)
        # list view
        self.notes_list = QListView(notes_widget)
        self.notes_list.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.notes_list.setMinimumSize(700, 700)
        # self.notes_list.clicked.connect(self.delete_note)
        self.notes_list.setModel(self.model)

        # list view context menu
        add_note_action = QAction(text="Add Note", parent=self)
        edit_note_action = QAction(text="Edit Note", parent=self)
        self.notes_list.addActions([add_note_action, edit_note_action])

        self.add_note_dialog = AddNoteDialog()
        self.edit_note_dialog = EditNoteDialog()

        new_note_signal = self.add_note_dialog.new_note_signal.connect(self.add_note)
        edit_note_signal = self.edit_note_dialog.edit_note_signal.connect(self.edit_note)

        add_note_action.triggered.connect(self.open_add_note_dialog)
        edit_note_action.triggered.connect(self.open_edit_note_dialog)
        

    def add_menu(self):
        menu_bar = self.menuBar()
        menu_bar.resize(100, 20)
        menu_edit = menu_bar.addMenu("Изменить")
        menu_add_note = menu_edit.addAction("Добавить заметку")
        menu_edit_note = menu_edit.addAction("Изменить заметку")

        menu_add_note.triggered.connect(self.open_add_note_dialog)
        menu_edit_note.triggered.connect(self.open_edit_note_dialog)



    @Slot()
    def open_add_note_dialog(self):
        self.add_note_dialog.open()

    @Slot()
    def open_edit_note_dialog(self):
        model_index = self.notes_list.selectedIndexes()[0]
        note = model_index.model().get_note(model_index, Qt.ItemDataRole.DisplayRole)
        self.edit_note_dialog.edited_line.setText(note.data)
        self.edit_note_dialog.open()

    @Slot()
    def add_note(self, note: Note):
        self.model.add_note(note)

    @Slot()
    def edit_note(self, data):
        model_index = self.notes_list.selectedIndexes()[0]
        note = model_index.model().get_note(model_index, Qt.ItemDataRole.DisplayRole)
        note.data = data



class AddNoteDialog(QDialog):
    new_note_signal = Signal(Note)
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)
        layout = QGridLayout(self)

        self.data = QLineEdit(parent=self)
        layout.addWidget(self.data, 0, 0)

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel, parent=self)
        layout.addWidget(buttonBox, 1, 0)
        buttonBox.accepted.connect(self.save_edit_button_clicked)
        buttonBox.rejected.connect(self.cancel_edit_button_clicked)

    @Slot()
    def save_edit_button_clicked(self):
        note = Note(self.data.text())
        self.new_note_signal.emit(note)
        self.data.clear()
        self.close()

    @Slot()
    def cancel_edit_button_clicked(self):
        self.close()

class EditNoteDialog(QDialog):
    edit_note_signal = Signal(str)
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 100)

        layout = QGridLayout(self)
        self.edited_line = QLineEdit(self)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.NoButton)

        layout.addWidget(self.edited_line, 0, 0)
        layout.addWidget(button_box, 1, 0)

        button_box.clicked.connect(self.save_edit)

    @Slot()
    def save_edit(self):
        self.edit_note_signal.emit(self.edited_line.text())
        self.close()
        self.edited_line.clear()
        


if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()