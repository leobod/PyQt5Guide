# Author: Leobod
# Date  : 2019-04-22
# Description: QTableWidget的基本使用

# 导入包
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QAbstractItemView
from PyQt5.QtWidgets import QWidget,QMainWindow,QVBoxLayout


class Demo_Table(QMainWindow):
    def __init__(self):
        super(Demo_Table, self).__init__()
        self.initUI()
        self.initLayout()
        self.initBar()

    def initUI(self):
        self.dataGrid = QTableWidget()
        self.dataGrid.setColumnCount(3)
        self.dataGrid.setRowCount(4)

        self.dataGrid.setItem(0,0,QTableWidgetItem("1"))
        self.dataGrid.setItem(1, 0, QTableWidgetItem("2"))
        self.dataGrid.setItem(2, 0, QTableWidgetItem("3"))
        self.dataGrid.setItem(3, 0, QTableWidgetItem("4"))

        self.dataGrid.setItem(0,1, QTableWidgetItem("Leo"))
        self.dataGrid.setItem(1, 1, QTableWidgetItem("Bod"))
        self.dataGrid.setItem(2, 1, QTableWidgetItem("Leobod"))
        self.dataGrid.setItem(3, 1, QTableWidgetItem("Lee"))

        self.dataGrid.setItem(0, 2, QTableWidgetItem(""))
        self.dataGrid.setItem(1, 2, QTableWidgetItem(""))
        self.dataGrid.setItem(2, 2, QTableWidgetItem(""))
        self.dataGrid.setItem(3, 2, QTableWidgetItem(""))

        self.dataGrid.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.dataGrid.clicked.connect(self.eventShowData)

    def initLayout(self):
        self.setCentralWidget(self.dataGrid)

    def initBar(self):
        pass

    def eventShowData(self):
        currentRow = self.dataGrid.currentIndex().row()

        print("text1:"+self.dataGrid.item(currentRow, 0).text())
        print("text2:"+self.dataGrid.item(currentRow, 1).text())
        print("text3:"+self.dataGrid.item(currentRow, 2).text())



from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Table()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())