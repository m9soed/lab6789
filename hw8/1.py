# 1. Нарисуйте графики синуса и косинуса.
# В каждом должно быть хотя бы 30 точек.

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter, QColor

from random import randint

from math import sin, cos, pi

class Chart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 700)
        chart = QChart()
        chart.setAnimationOptions(QChart.AllAnimations)

        chart.addSeries(self.generate_series(sin))
        chart.addSeries(self.generate_series(cos))
        chart.createDefaultAxes()
        chart.setTitle("график")

        _chart_view = QChartView(chart)
        _chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(_chart_view)


    def generate_series(self, func) -> QLineSeries:
        series = QLineSeries()
        x = 0
        while x < 30:
            series.append(QPointF(x, func(x)))
            x += pi/128
        series.setName(func.__name__)
        series.setColor(QColor(randint(0, 256), randint(0, 256), randint(0, 256), 255))

        return series


if __name__=="__main__":
    app = QApplication([])
    chart = Chart()
    chart.show()
    app.exec()