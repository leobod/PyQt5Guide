# Author: Leobod
# Date  : 2019-04-21 12:09
# Description: QWidget的自定义

# 导入包
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QGridLayout,QSizePolicy
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtGui import QIcon

class MainWindow_UI(QWidget):
    def __init__(self):
        super(MainWindow_UI, self).__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.logo = QPushButton()
        self.logo.setIcon(QIcon('icon/shield.png'))
        self.logo.setFlat(True)

        self.min = QPushButton()
        self.min.setIcon(QIcon("icon/min.png"))
        self.min.setFlat(True)

        self.max = QPushButton()
        self.max.setIcon(QIcon("icon/max.png"))
        self.max.setFlat(True)

        self.clo = QPushButton()
        self.clo.setIcon(QIcon("icon/close.png"))
        self.clo.setFlat(True)


        contentLayout = QGridLayout()
        contentLayout.setContentsMargins(0,0,0,0)
        contentLayout.addWidget(self.logo, 0,0,1,1)
        contentLayout.addWidget(QLabel("title"),0,1,1,16)
        contentLayout.addWidget(self.min, 0,17,1,1)
        contentLayout.addWidget(self.max, 0,18,1,1)
        contentLayout.addWidget(self.clo, 0,19,1,1)
        contentLayout.addWidget(QLabel("hello"), 1,0,100,20)

        self.setLayout(contentLayout)

        self.min.clicked.connect(self.showMinimized)
        self.max.clicked.connect(self.showMaximized)
        # 使用QCoreApplication完全退出
        self.clo.clicked.connect(QCoreApplication.instance().quit)

        # # 窗体背景透明，控件不透明
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # self.setAttribute(Qt.WA_TranslucentBackground)





from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow_UI()
    win.resize(800,600)
    # 显示界面
    win.show()
    sys.exit(app.exec_())