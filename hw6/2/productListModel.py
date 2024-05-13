from PySide6.QtCore import Qt, QModelIndex, QAbstractListModel
from product import Product


class ProductListModel(QAbstractListModel):
    def __init__(self, products: list[Product] = None):
        super().__init__()
        self._products = products or []

    def data(self, index: QModelIndex, role):
        product = self._products[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return str(product)
        return None

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self._products)

    def add_product(self, product: Product) -> None:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._products.append(product)
        self.endInsertRows()

    def del_product(self, product: Product) -> None:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._products.clear(product)
        self.endInsertRows()

    @property
    def total_weight(self) -> float:
        total = 0
        for product in self._products:
            total += product.total_weight
        return total