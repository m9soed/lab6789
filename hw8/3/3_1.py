from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QPieSeries

import pandas

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        series = QPieSeries()
        series.setHoleSize(0.5)
        df = pandas.read_csv("hurricanes.csv")

        for i in df.columns[2:]:
            series.append(i, sum(df[i].values))
            print(i)


        slices = series.slices()
        self.slice = slices[0]
        for sl in slices:
            if sl.value() > self.slice.value():
                self.slice = sl

        self.slice.setExploded()
        self.slice.setLabelVisible(True)
        
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.addSeries(series)
        self.chart.setTitle('ураганы...')

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)

if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    window.resize(700, 700)
    app.exec()