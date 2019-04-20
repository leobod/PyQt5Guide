# 代码引用于： CSDN https://blog.csdn.net/richenyunqi/article/details/80546952

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        lbl = QLabel(self)
        pixmap = QPixmap("images/monitor.png")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        lbl.setPixmap(pixmap)                   # 在label上显示图片
        lbl.setScaledContents(True)             # 让图片自适应label大小
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())