# Author:   Leobod
# Data  :   2019-04-20 17:21
# Description: QLabel制作超链接
#       linkActiveted
#           当单击标签中的超链接，希望在新窗口打开这个超链接时，setOpenExternalLinks特性必须设置为True，即setOpenExternalLinks（True）

from PyQt5.QtWidgets import QWidget,QLabel

class Demo_Label(QWidget):
    def __init__(self):
        super(Demo_Label, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        self.alink = QLabel("<a href='http://blog.eside.cn'>http://blog.eside.cn", self)
        # 必须加上下面一句，上方的链接才会具有点击自动使用游览器打开的效果
        self.alink.setOpenExternalLinks(True)

    def initLayout(self):
        pass



import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Label()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())