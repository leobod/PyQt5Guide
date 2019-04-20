# Author: Leobod
# Date  : 2019-04-20 17:27
# Description: QLineEdit,QTextEdit的基本使用

# 引用包
from PyQt5.QtWidgets import QWidget,QLineEdit,QTextEdit,QVBoxLayout
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class Demo_QLineEdit(QWidget):
    def __init__(self):
        super(Demo_QLineEdit, self).__init__()
        self.initUI()
        self.initLayout()
        self.initData()

    def initUI(self):
        # 单行文本框，设置预占提示文字
        self.led_001 = QLineEdit()
        self.led_001.setPlaceholderText("请在此处输入文本")

        # 密码框制作
        self.led_002 = QLineEdit()
        self.led_002.setEchoMode(QLineEdit.Password)
        self.led_002.setText("hello")

        # 输入数据格式限制（允许在输入框里面输入什么，或者不允许输入什么）
        self.led_003 = QLineEdit()
        self.led_003.setValidator(QIntValidator())
        self.led_003.setText("100000")
        ### 下面的语句使用前 from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
        # # 整形 范围：[1, 99]
        # pIntValidator = QIntValidator(self)
        # pIntValidator.setRange(1, 99)
        #
        # # 浮点型 范围：[-360, 360] 精度：小数点后2位
        # pDoubleValidator = QDoubleValidator(self)
        # pDoubleValidator.setRange(-360, 360)
        # pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # pDoubleValidator.setDecimals(2)
        #
        # # 正则表达式匹配
        # reg = QRegExp("[a-zA-Z0-9]+$")
        # pValidator = QRegExpValidator(self)
        # pValidator.setRegExp(reg)

        # 限制数据显示格式，比如输入软件序列号时的输入框
        self.led_004 = QLineEdit()
        self.led_004.setInputMask("0000-0000-0000-00")
        # self.led_004.setInputMask("AAAA-0000-HH")


        # 文本域的使用
        self.ted_001 = QTextEdit()


    def initLayout(self):
        contentBox = QVBoxLayout()
        contentBox.addWidget(QLabel("文本 框、域的演示"), alignment=Qt.AlignCenter)
        contentBox.addStretch(1)
        contentBox.addWidget(self.led_001)
        contentBox.addWidget(self.led_002)
        contentBox.addWidget(self.led_003)
        contentBox.addWidget(self.led_004)
        contentBox.addStretch(1)
        contentBox.addWidget(self.ted_001)
        contentBox.addStretch(10)

        self.setLayout(contentBox)

    def initData(self):
        f = open("Sample.txt", "r", encoding="utf-8")
        self.ted_001.setText(f.read())
        f.close()


import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_QLineEdit()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())