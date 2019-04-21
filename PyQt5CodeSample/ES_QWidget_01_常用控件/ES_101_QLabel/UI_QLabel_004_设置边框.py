# Author:   Leobod
# Data  :   2019-04-20 15:40
# Description: 控件的边框设置


# 导入PyQt5的控件包，用于使用QLabel
from PyQt5.QtWidgets import QLabel,QWidget,QVBoxLayout,QFrame


class Demo_Label(QWidget):
    def __init__(self):
        super(Demo_Label, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        # 新建一个QLabel对象,使用HTML修改字体颜色
        self.label_2 = QLabel()
        self.label_2.setText("<font style='color: red;'>在Label中放入红色的字体</font>")

        # 新建一个QLabel对象,使用HTML修改字体的背景颜色，字体颜色，字体大小等样式
        self.label_3 = QLabel()
        self.label_3.setText("<h1 style='padding: 5px 10px; color: blue; background-color: orange; font-size: 50px;'>在Label中放入带样式的HTML文本</h1>")

        # 新建一个QLabel对象,使用HTML修改字体颜色
        self.label_4 = QLabel()
        self.label_4.setText("<font style='color: red;'>在Label中放入红色的字体</font>")


        # 使用样式修改QLabel的边框样子
        self.label_3.setStyleSheet("border-width: 2px; border-color: red; border-style: solid; border-radius: 5px;")

        # 使用QFrame设置边框
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Raised)
        self.label_4.setLineWidth(6)
        self.label_4.setMidLineWidth(10)


    def initLayout(self):
        contentBox = QVBoxLayout()
        contentBox.addWidget(self.label_2, stretch=2)
        contentBox.addWidget(self.label_3, stretch=1)
        contentBox.addWidget(self.label_4, stretch=1)
        contentBox.addStretch(20)

        contentBox.setContentsMargins(0,0,0,0)
        self.setLayout(contentBox)



import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Label()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())