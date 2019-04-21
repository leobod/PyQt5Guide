# Author: Leobod
# Date  : 2019-04-21 13:48
# Description: MainWindow的基本使用

# 导入包
from PyQt5.QtWidgets import QMainWindow,QWidget, QLabel,QPushButton,QMenu,QAction
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt,QCoreApplication

class MainWindow_UI(QMainWindow):
    def __init__(self):
        super(MainWindow_UI, self).__init__()
        self.initUI()
        self.initLayout()
        self.initEvents()
        self.statusBar().showMessage("Ready")

    def initUI(self):
        self.lbl = QLabel("Hello,World!")
        self.lbl.setStatusTip("Hello")


        self.exit = QPushButton("退出")
        self.exit.setStatusTip('Exit application')



    def initLayout(self):
        contentWidget = QWidget()
        box = QVBoxLayout()
        box.addWidget(self.lbl)
        box.addWidget(self.exit)
        contentWidget.setLayout(box)

        # 设置界面的主控件
        self.setCentralWidget(contentWidget)

        # 设置菜单栏
        # 菜单或者工具栏动作项
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(QCoreApplication.instance().quit)

        menubar = self.menuBar()                            # 菜单项目
        self.fileMenu = menubar.addMenu('&File')            # 子菜单项目
        self.menu101 = self.fileMenu.addMenu("&Open")       # 子菜单项目
        self.menu102 = self.fileMenu.addAction(exitAction)  # 动作项目

        self.helloMenu = menubar.addMenu('&Hello')

        # 设置状态栏
        self.statusBar()


    def initEvents(self):
        self.exit.clicked.connect(QCoreApplication.instance().quit)



from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow_UI()
    win.resize(800,600)
    win.show()
    sys.exit(app.exec_())