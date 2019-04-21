# Author: Leobod
# Date  : 2019-04-21 20:59
# Description: 表格视图

# 导入包
from PyQt5.QtWidgets import QWidget, QTableView
from PyQt5.QtWidgets import QVBoxLayout,QHeaderView,QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class Demo_TabelView(QWidget):
    def __init__(self):
        super(Demo_TabelView, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        # 表格视图控件
        self.view = QTableView()
        # 使用QStandardItemModel(row,col)
        self.model = QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(["列1","列2","列3"])

        self.model.setItem(0,0, QStandardItem("1"))
        self.model.setItem(1,0, QStandardItem("2"))
        self.model.setItem(2,0, QStandardItem("3"))

        self.view.setModel(self.model)

        # 设置表格头部占满窗体
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置是否可编辑
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置选中方式
        self.view.setSelectionBehavior(QAbstractItemView.SelectRows)

    def initLayout(self):
        contentLayout = QVBoxLayout()
        contentLayout.addWidget(self.view)

        self.setLayout(contentLayout)


from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_TabelView()
    demo.show()
    sys.exit(app.exec_())