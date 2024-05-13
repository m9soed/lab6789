from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QPieSeries

import pandas

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        series = QPieSeries()
        df = pandas.read_csv("hurricanes.csv")

        for i in range(len(df.index)):
            series.append(df.iloc[i]["Month"], df.iloc[i]["2007"])
            # print(df.iloc[i]["2007"], df.iloc[i]["Month"])

        # self.slice = series.slices()[1]
        slices = series.slices()
        self.slice = slices[0]
        for sl in slices:
            if sl.value() > self.slice.value():
                self.slice = sl
        
        self.slice.setExploded()
        self.slice.setLabelVisible()
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.addSeries(series)
        self.chart.setTitle('ураганы...')
        # self.chart.legend().hide()

        self._chart_view = QChartView(self.chart)

        self.setCentralWidget(self._chart_view)

if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    window.resize(700, 700)
    app.exec()