# Author: Leobod
# Date  : 2019-04-20 22:32
# Description: QSpinBox,QSlider的基本使用

# import PyQt5 Package
# import usual widget
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton
# import this chapter's widget
from PyQt5.QtWidgets import QSpinBox,QSlider
# import layout widget
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt

class Demo_QSpinBox(QWidget):
    def __init__(self):
        super(Demo_QSpinBox, self).__init__()
        self.initUI()
        self.initLayout()
        self.initEvents()

    def initUI(self):
        self.lbl_001 = QLabel("计数器:")
        self.lbl_003 = QLabel()
        self.wid_001 = QSpinBox()
        self.wid_001.setMaximum(100)
        self.wid_001.setMinimum(0)
        self.wid_001.setSingleStep(1)

        self.lbl_002 = QLabel("计数滑块:")
        self.lbl_004 = QLabel("")
        # 默认为垂直滑块，需要添加Qt.Horizontal来变成水平
        self.wid_002 = QSlider(Qt.Horizontal)
        self.wid_002.setRange(0,100)
        self.wid_002.setSingleStep(10)
        self.wid_002.setTickInterval(10)
        self.wid_002.setTickPosition(QSlider.TicksBelow)
        pass

    def initLayout(self):
        contentLayout = QVBoxLayout()
        contentLayout.addWidget(self.lbl_001)
        contentLayout.addWidget(self.lbl_003)
        contentLayout.addWidget(self.wid_001)

        contentLayout.addWidget(self.lbl_002)
        contentLayout.addWidget(self.lbl_004)

        box1 = QHBoxLayout()
        box1.addWidget(self.wid_002)
        contentLayout.addLayout(box1)

        self.setLayout(contentLayout)
        pass

    def initEvents(self):
        self.wid_001.valueChanged.connect(self.eventValue)
        self.wid_002.valueChanged.connect(self.eventValue)

    def eventValue(self, value):
        self.wid_001.setValue(value)
        self.wid_002.setValue(value)
        self.lbl_003.setText(str(value))
        self.lbl_004.setText(str(value))




from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_QSpinBox()
    demo.show()
    sys.exit(app.exec_())