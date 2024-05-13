from PySide6.QtCore import Qt, QModelIndex, QAbstractListModel
from note import Note


class NotesListModel(QAbstractListModel):
    def __init__(self, notes: list[Note] = None) -> None:
        super().__init__()
        self._notes = notes or []

    def data(self, index: QModelIndex, role):
        note = self._notes[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return str(note)
        return None
    
    def get_note(self, index:QModelIndex, role):
        note = self._notes[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return note
        return None

    def rowCount(self, parent=QModelIndex()):
        return len(self._notes)

    def add_note(self, note: Note):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._notes.append(note)
        self.endInsertRows()


    def del_note(self, note: Note):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._notes.remove(note)
        self.endInsertRows()
