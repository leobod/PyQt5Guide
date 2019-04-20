# Author: Leobod
# Date  : 2019-04-20 21:59
# Description: 这是一个简单的登录界面的实现

# import PyQt5 Package
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QCheckBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Demo_Login(QWidget):
    def __init__(self):
        super(Demo_Login, self).__init__()
        self.initUI()
        self.initLayout()
        self.initEvents()
        self.initStyle()
        self.winInfo()

    def initUI(self):
        self.wTitle = QLabel("HI系统登录界面")
        self.wAccountLbl = QLabel("账号：")
        self.wAccountLed = QLineEdit()
        self.wPinLbl = QLabel("密码：")
        self.wPinLed = QLineEdit()
        self.wPinLed.setEchoMode(QLineEdit.Password)
        self.wRememberPin = QCheckBox("记住密码")
        self.wRegister = QPushButton("注册")
        self.wLogin = QPushButton("登录")

    def initLayout(self):
        # 声明布局对象
        contentBox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        # 先加载界面结构化布局
        contentBox.addStretch(2)
        contentBox.addLayout(hbox1)
        contentBox.addLayout(hbox2)
        contentBox.addLayout(hbox3)
        contentBox.addLayout(hbox4)
        contentBox.addLayout(hbox5)
        contentBox.addStretch(2)

        # 内部布局的装载
        hbox1.addStretch(1)
        hbox1.addWidget(self.wTitle, stretch=10)
        hbox1.addStretch(1)

        hbox2.addStretch(1)
        hbox2.addWidget(self.wAccountLbl, stretch=1)
        hbox2.addWidget(self.wAccountLed, stretch=9)
        hbox2.addStretch(1)

        hbox3.addStretch(1)
        hbox3.addWidget(self.wPinLbl, stretch=1)
        hbox3.addWidget(self.wPinLed, stretch=9)
        hbox3.addStretch(1)

        hbox4.addStretch(1)
        hbox4.addWidget(QLabel(""), stretch=1)
        hbox4.addWidget(self.wRememberPin, stretch=9)
        hbox4.addStretch(1)

        hbox5.addStretch(2)
        hbox5.addWidget(self.wRegister, stretch=4)
        hbox5.addWidget(self.wLogin, stretch=5)
        hbox5.addStretch(1)


        # 布局对象装入到界面中
        self.setLayout(contentBox)


    def initEvents(self):
        self.wLogin.clicked.connect(self.eventLogin)

    def initStyle(self):
        self.wTitle.setAlignment(Qt.AlignCenter)
        self.wAccountLbl.setAlignment(Qt.AlignRight)
        self.wAccountLed.setAlignment(Qt.AlignLeft)
        self.wPinLbl.setAlignment(Qt.AlignRight)
        self.wPinLed.setAlignment(Qt.AlignLeft)
        pass

    def winInfo(self):
        self.setWindowTitle("HI系统用户登录界面")
        self.setWindowIcon(QIcon("icon/shield.png"))

    def eventLogin(self):
        account = self.wAccountLed.text()
        pin = self.wPinLed.text()
        if account == "admin" and pin == "admin":
            QMessageBox.information(self, "登录提示", "登录成功", QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "登录提示", "用户名或者密码错误", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)




from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Login()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec_())