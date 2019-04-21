# Author: Leobod
# Date  : 2019-04-21 12:29
# Description: QWidget的自定义2
#                   + 问题：结构没有经过排版，相对混乱
#                   + 窗体为了，自定义标题栏，并且使得标题栏带圆角，放弃了原始界面的元素，需要自己写移动的相关事件
#                   + 界面的最底下一个win做了透明化，放在这个win上的如果不设置背景颜色，默认也会透明

# 导入包
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QBoxLayout,QSizePolicy
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtGui import QIcon

class MainWindow_UI(QWidget):
    def __init__(self):
        super(MainWindow_UI, self).__init__()
        # 确定要使用的布局
        contentLayout = QVBoxLayout()
        top = QHBoxLayout()
        content = QHBoxLayout()
        # 重定义设置界面标题
        wTop = QWidget()
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
        # 界面标题布局
        top.addWidget(self.logo, stretch=1)
        top.addWidget(QLabel("Titile"), stretch=16)
        top.addWidget(self.min, stretch=1)
        top.addWidget(self.max, stretch=1)
        top.addWidget(self.clo, stretch=1)
        top.setContentsMargins(0,0,0,0)
        wTop.setLayout(top)
        wTop.setStyleSheet("background-color: #3A7B67; border-top-left-radius: 10px; border-top-right-radius: 10px;")

        # 重定义文本区域
        wContent = QWidget()
        content.addWidget(QLabel("Hello，World!",), stretch=1, alignment=Qt.AlignCenter)
        wContent.setLayout(content)
        wContent.setStyleSheet("background-color: #FFFFFF;")
        # 文本区域布局
        contentLayout.addWidget(wTop, stretch=1)
        contentLayout.addWidget(wContent, stretch=20)
        contentLayout.setSpacing(0)

        # 布局装载到界面中
        self.setLayout(contentLayout)

        # 事件
        self.min.clicked.connect(self.showMinimized)
        self.max.clicked.connect(self.showMaximized)
        # 使用QCoreApplication完全退出
        self.clo.clicked.connect(QCoreApplication.instance().quit)

        # # 窗体背景透明，控件不透明，消除背景导致的多余元素
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景色




from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow_UI()
    win.resize(800,600)
    # 显示界面
    win.show()
    sys.exit(app.exec_())