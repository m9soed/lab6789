from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
                              QChartView, QValueAxis, QLineSeries, QScatterSeries)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
import pandas as pd


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        df = pd.read_csv("trees.csv")
        self.chart = QChart()
        for col in df.columns[1:]:
            series = QScatterSeries()
            for i in range(len(df.index)):
                series.append(df.iloc[i]['ID'], df.iloc[i][col])
            series.setName(col)
            self.chart.addSeries(series)


        self.chart.setAnimationOptions(QChart.SeriesAnimations)


        self.axis_x = QValueAxis()
        # self.axis_x.setRange(0, 100)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 150)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        series.attachAxis(self.axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        #self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)




if __name__=="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    window.resize(700, 700)
    app.exec()
