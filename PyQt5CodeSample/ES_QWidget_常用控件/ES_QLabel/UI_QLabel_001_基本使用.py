# Author:   Leobod
# Data  :   2019-04-20 15:40
# Description: QLabel的简单使用
#               + 包括如何创建QLabel对象
#               + 如何设置QLabel上的文字（文本或者HTML格式的内容）
#               + 如何不用外部样式表的情况下对QLabel设置颜色
#               + 设置QLabel文字的对齐方式

# 导入PyQt5的控件包，用于使用QLabel
from PyQt5.QtWidgets import QLabel,QWidget,QVBoxLayout,QFrame
# 导入PyQt5的核心包的Qt，用于获取全局变量
from PyQt5.QtCore import Qt

class Demo_Label(QWidget):
    def __init__(self):
        super(Demo_Label, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        # 新建一个QLabel对象，并且直接加入到self页面
        self.label_1 = QLabel("Hello，World！", self)

        # 新建一个QLabel对象,使用HTML修改字体颜色
        self.label_2 = QLabel()
        self.label_2.setText("<font style='color: red;'>在Label中放入红色的字体</font>")
        self.label_2.setAlignment(Qt.AlignRight)

        # 新建一个QLabel对象,使用HTML修改字体的背景颜色，字体颜色，字体大小等样式
        self.label_3 = QLabel()
        self.label_3.setText("<h1 style='padding: 5px 10px; color: blue; background-color: orange; font-size: 50px;'>在Label中放入带样式的HTML文本</h1>")
        # 对于对齐方法，双属性如何设置
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignRight)



    def initLayout(self):
        contentBox = QVBoxLayout()
        contentBox.addWidget(self.label_2, stretch=1)
        contentBox.addWidget(self.label_3, stretch=1)
        contentBox.addStretch(20)

        # 将下面这句话的注释解除，可以使得布局无外边距
        # contentBox.setContentsMargins(0,0,0,0)
        self.setLayout(contentBox)



import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Label()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())