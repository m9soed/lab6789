from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QGridLayout, QWidget, QLineEdit, QLabel, QPushButton
from PySide6.QtCore import Slot
from productListModel import ProductListModel
from product import Product


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 700)

        main_widget = QWidget(self)
        layout = QGridLayout(main_widget)
        self.setCentralWidget(main_widget)

        self.name = QLineEdit(main_widget)
        layout.addWidget(QLabel("Name"), 0, 0)
        layout.addWidget(self.name, 0, 1)

        self.num = QLineEdit(main_widget)
        layout.addWidget(QLabel("Number"), 1, 0)
        layout.addWidget(self.num, 1, 1)

        self.weight_per_unit = QLineEdit(main_widget)
        layout.addWidget(QLabel("Weight per unit"), 2, 0)
        layout.addWidget(self.weight_per_unit, 2, 1)

        add_product_button = QPushButton("Add", main_widget)
        add_product_button.clicked.connect(self.add_product_button_clicked)
        layout.addWidget(add_product_button, 3, 1)

        product_list = QListView(main_widget)
        layout.addWidget(product_list, 4, 0, 2, 2)

        self.model = ProductListModel()
        self.model.add_product(Product("butter", 4, 0.5))
        product_list.setModel(self.model)

        self.total_weight = QLabel(str(self.model.total_weight) + " kg", main_widget)
        layout.addWidget(self.total_weight, 7, 0, 2, 2)

    @Slot()
    def add_product_button_clicked(self):
        name = self.name.text()
        num = int(self.num.text())
        weight_per_unit = float(self.weight_per_unit.text())

        if name and num and weight_per_unit:
            product = Product(name, num, weight_per_unit)
            self.model.add_product(product)
            self.total_weight.setText(str(self.model.total_weight)+" kg")
        else:
            pass 





if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
