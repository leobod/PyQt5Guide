# Author:   Leobod
# Date  :   2019-04-20 16:05
# Description: 让鼠标移动到控件上变成其他鼠标形状
#                   + Qt.PointHandCursor 标准手型
#                   + Qt.ArrorCursor     标准鼠标箭头状，Windows下不变换
#                   + Qt.BlankCursor     空白箭头，等于箭头隐藏
#                   + Qt.BusyCursor      带箭头的忙碌型
#                   + Qt.CloseHandCursor 非标准手型
#                   + Qt.CrossCursor     十字型 ，类似于标图软件的手型
#                   + Qt.DragCopyCursor
#                   + Qt.DragLinkCursor
#                   + Qt.DragMoveCursor
#                   + Qt.ForbiddenCursor 红色禁止鼠标型
#                   + Qt.IBeamCursor     文本编辑型

# 导入对应的包
from PyQt5.QtWidgets import QLabel,QWidget,QVBoxLayout
# 导入手型相关的包
from PyQt5.QtGui import QCursor
# 导入PyQt5的核心包的Qt，用于获取全局变量
from PyQt5.QtCore import Qt

class Demo_Label(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        # ---------- 手型Cursor ----------
        self.label_001 = QLabel("你好，欢迎学习PyQt5！,在这个Label上标识为PointingHandCursor")
        self.label_001.setCursor(QCursor(Qt.PointingHandCursor))
        # ----------  ----------
        self.label_002 = QLabel("在这个Label上标识为ArrorCursor")
        self.label_002.setCursor(QCursor(Qt.ArrowCursor))
        # ----------  ----------
        self.label_003 = QLabel("在这个Label上标识为BitmapCursor")
        self.label_003.setCursor(QCursor(Qt.BitmapCursor))
        # ----------  ----------
        self.label_004 = QLabel("在这个Label上标识为BlankCursor")
        self.label_004.setCursor(QCursor(Qt.BlankCursor))
        # ----------  ----------
        self.label_005 = QLabel("在这个Label上标识为BusyCursor")
        self.label_005.setCursor(QCursor(Qt.BusyCursor))
        # ----------  ----------
        self.label_006 = QLabel("在这个Label上标识为ClosedHandCursor")
        self.label_006.setCursor(QCursor(Qt.ClosedHandCursor))
        # ----------  ----------
        self.label_007 = QLabel("在这个Label上标识为CrossCursor")
        self.label_007.setCursor(QCursor(Qt.CrossCursor))
        # ----------  ----------
        self.label_008 = QLabel("在这个Label上标识为DragCopyCursor")
        self.label_008.setCursor(QCursor(Qt.DragCopyCursor))
        # ----------  ----------
        self.label_009 = QLabel("在这个Label上标识为DragLinkCursor")
        self.label_009.setCursor(QCursor(Qt.DragLinkCursor))
        # ----------  ----------
        self.label_010 = QLabel("在这个Label上标识为DragMoveCursor")
        self.label_010.setCursor(QCursor(Qt.DragMoveCursor))
        # ----------  ----------
        self.label_011 = QLabel("在这个Label上标识为ForbiddenCursor")
        self.label_011.setCursor(QCursor(Qt.ForbiddenCursor))
        # ----------  ----------
        self.label_012 = QLabel("在这个Label上标识为IBeamCursor")
        self.label_012.setCursor(QCursor(Qt.IBeamCursor))


    def initLayout(self):
        contentBox = QVBoxLayout()
        contentBox.addWidget(self.label_001, stretch=2, alignment=Qt.AlignRight)
        contentBox.addWidget(self.label_002, stretch=2, alignment=Qt.AlignCenter)
        contentBox.addWidget(self.label_003, stretch=2, alignment=Qt.AlignLeft)
        contentBox.addWidget(self.label_004, stretch=2, alignment=Qt.AlignCenter)
        contentBox.addWidget(self.label_005, stretch=2, alignment=Qt.AlignRight)
        contentBox.addWidget(self.label_006, stretch=2, alignment=Qt.AlignCenter)
        contentBox.addWidget(self.label_007, stretch=2, alignment=Qt.AlignLeft)
        contentBox.addWidget(self.label_008, stretch=2, alignment=Qt.AlignCenter)
        contentBox.addWidget(self.label_009, stretch=2, alignment=Qt.AlignRight)
        contentBox.addWidget(self.label_010, stretch=2, alignment=Qt.AlignCenter)
        contentBox.addWidget(self.label_011, stretch=2, alignment=Qt.AlignLeft)
        contentBox.addWidget(self.label_012, stretch=2, alignment=Qt.AlignCenter)

        self.setLayout(contentBox)


import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Label()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())