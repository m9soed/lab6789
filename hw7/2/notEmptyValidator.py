from PySide6.QtGui import QValidator


class notEmptyValidator(QValidator):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.line_edit = parent

    def validate(self, s: str, p: int) -> object:
        if self.line_edit.hasFocus():
            return QValidator.Acceptable
        if not s.strip():
            return QValidator.Invalid
        return QValidator.Acceptable
    
    def fixup(self, s):
        self.line_edit.setText("write a new note here")
    
    
    def validate_string(s):
        return bool(s.strip())
