# Author: Leobod
# Date  : 2019-04-21
# Description: 一个简单的由 3个slider获取颜色的小工具

# 导入包
from PyQt5.QtWidgets import QWidget,QPushButton,QSlider,QSpinBox
from PyQt5.QtWidgets import QGridLayout,QSizePolicy
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class Demo_Color(QWidget):

    color_r = 0
    color_g = 0
    color_b = 0

    def __init__(self):
        super(Demo_Color, self).__init__()
        self.initUI()                           # # 声明控件对象，为界面的元素
        self.initLayout()                       # # 将控件装入到布局中，并将布局放入界面中
        self.initEvents()                       # # 为界面的控件添加 （信号与槽函数）用于处理事件

    # 声明控件对象，为界面的元素
    def initUI(self):
        self.slider_r = QSlider(Qt.Horizontal)
        self.slider_g = QSlider(Qt.Horizontal)
        self.slider_b = QSlider(Qt.Horizontal)

        self.spin_r = QSpinBox()
        self.spin_g = QSpinBox()
        self.spin_b = QSpinBox()

        self.slider_r.setRange(0,255)
        self.slider_g.setRange(0,255)
        self.slider_b.setRange(0,255)

        self.spin_r.setRange(0,255)
        self.spin_g.setRange(0,255)
        self.spin_b.setRange(0,255)

        self.color = QPushButton()
        self.color.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.changeColor(self.color_r, self.color_g, self.color_b)

    # 将控件装入到布局中，并将布局放入界面中
    def initLayout(self):
        contentLayout = QGridLayout()
        contentLayout.addWidget(self.slider_r, 0, 0, 1, 7)
        contentLayout.addWidget(self.spin_r, 0, 7, 1, 1)

        contentLayout.addWidget(self.slider_g, 1, 0, 1, 7)
        contentLayout.addWidget(self.spin_g, 1, 7, 1, 1)

        contentLayout.addWidget(self.slider_b, 2, 0, 1, 7)
        contentLayout.addWidget(self.spin_b, 2, 7, 1, 1)

        contentLayout.addWidget(self.color, 0,8,3,3)

        self.setLayout(contentLayout)

    # 为界面的控件添加 （信号与槽函数）用于处理事件
    def initEvents(self):
        self.slider_r.valueChanged.connect(self.eventRedChange)         # 关联槽函数eventRedChange
        self.spin_r.valueChanged.connect(self.eventRedChange)           # 关联槽函数eventRedChange

        self.slider_g.valueChanged.connect(self.eventGreenChange)       # 关联槽函数eventGreenChange
        self.spin_g.valueChanged.connect(self.eventGreenChange)         # 关联槽函数eventGreenChange

        self.slider_b.valueChanged.connect(self.eventBlueChange)        # 关联槽函数eventBlueChange
        self.spin_b.valueChanged.connect(self.eventBlueChange)          # 关联槽函数eventBlueChange

    # 与红色基础色，值改变的事件
    def eventRedChange(self, value):
        self.color_r = value
        self.slider_r.setValue(value)
        self.spin_r.setValue(value)
        self.changeColor(self.color_r, self.color_g, self.color_b)

    # 与绿色基础色，值改变的事件
    def eventGreenChange(self, value):
        self.color_g = value
        self.slider_g.setValue(value)
        self.spin_g.setValue(value)
        self.changeColor(self.color_r, self.color_g, self.color_b)

    # 与蓝色基础色，值改变的事件
    def eventBlueChange(self, value):
        self.color_b = value
        self.slider_b.setValue(value)
        self.spin_b.setValue(value)
        self.changeColor(self.color_r, self.color_g, self.color_b)

    # 修改color显示区域的颜色，此处使用qss修改
    def changeColor(self, r,g,b):
        self.color.setStyleSheet('background-color: rgb('+str(r)+','+str(g)+','+str(b)+');')
        # # 下面这段并未使用，用于后面的细节工作
        # xr_16 = hex(r)
        # xg_16 = hex(g)
        # xb_16 = hex(b)
        # r_16 = xr_16[2:]
        # g_16 = xg_16[2:]
        # b_16 = xb_16[2:]
        # # 由3组0-255装换为16进制的颜色值。存在一些缺陷， 转换后不是自动为2位的16进制，是按照实际的值来确定值的位数，待修改
        # str_rgb_16 = r_16 + g_16 + b_16





from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Color()
    demo.resize(300,100)
    demo.show()
    sys.exit(app.exec_())