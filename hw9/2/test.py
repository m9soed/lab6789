import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Image Viewer")
        self.layout = QVBoxLayout()
        
        self.image_list = QListWidget()
        self.image_list.setIconSize(QSize(300,300))
        self.layout.addWidget(self.image_list)
        
        self.add_button = QPushButton("Add Image")
        self.add_button.clicked.connect(self.add_image)
        self.layout.addWidget(self.add_button)
        
        self.setLayout(self.layout)
    
    def add_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                image_item = QListWidgetItem()
                image_item.setIcon(QIcon(file_path))
                self.image_list.addItem(image_item)
    
def main():
    app = QApplication(sys.argv)
    
    window = ImageViewer()
    with open("style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
