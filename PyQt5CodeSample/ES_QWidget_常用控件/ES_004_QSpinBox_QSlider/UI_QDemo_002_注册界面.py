# Author: Leobod
# Date  : 2019-04-20 23:06
# Description: 简单的注册界面
# From  : 个人的历史工程记录
# Remark: 此界面仅包含简单的UI设计的部分，逻辑（信号与槽函数均不包含），特此说明

# 导入 package
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initLayout()
        self.initUIStyle()

    def initUI(self):
        self.WBackToLogin = QPushButton("返回登录")

        self.pagename = QLabel("嗨VIP管理系统——注册")
        self.pagename.setAlignment(Qt.AlignHCenter)

        self.WUserNameLbl = QLabel("<font style='color:red;'>*</font>用户姓名:")
        self.WUserNameLed = QLineEdit("")
        self.WUserNameInfo = QLabel("")

        self.WUserAccountLbl = QLabel("<font style='color:red;'>*</font>用户账号:")
        self.WUserAccountLed = QLineEdit()
        self.WUserAccountExist = QPushButton("用户账号检测")
        self.WUserAccountInfo = QLabel("")

        self.WUserPinLbl = QLabel("<font style='color:red;'>*</font>用户密码:")
        self.WUserPinLed = QLineEdit()
        self.WUserPinLed.setEchoMode(QLineEdit.Password)
        self.WUserPinInfo = QLabel("")

        self.WUserRePinLbl = QLabel("<font style='color:red;'>*</font>确认密码:")
        self.WUserRePinLed = QLineEdit()
        self.WUserRePinLed.setEchoMode(QLineEdit.Password)
        self.WUserRePinInfo = QLabel("")

        self.WUserPhoneLbl = QLabel("手机号:")
        self.WUserPhoneLed = QLineEdit()
        self.WUserPhoneInfo = QLabel("")

        self.WUserEmailLbl = QLabel("邮箱号:")
        self.WUserEmailLed = QLineEdit()
        self.WUserEmailInfo = QLabel("")

        self.WUserSexLbl = QLabel("性别:")
        self.WUserSexCmb = QComboBox()
        self.WUserSexCmb.addItems(['未知',"男","女"])
        self.WUserSexInfo = QLabel("")

        # 为了应用QSpinBox插入的内容
        self.WUserAgeLbl = QLabel("年龄:")
        self.WUserAgeSpb = QSpinBox()
        self.WUserAgeSpb.setRange(0,100)
        self.WUserAgeSpb.setValue(16)

        self.WUserAddressLbl = QLabel("地址:")
        self.WUserAddressLed = QLineEdit()
        self.WUserAddressInfo = QLabel("")

        self.WUserResetBtn = QPushButton("重 置")
        self.WUserSubmitBtn = QPushButton("提 交")


    def initLayout(self):
        self.contentContainer = QWidget()
        mainBox = QGridLayout()
        mainBox.addWidget(self.WBackToLogin,0,0,1,3)
        mainBox.addWidget(self.pagename, 0,3,1,12)
        mainBox.addWidget(QLabel(""),0,15,1,3)

        mainBox.addWidget(QLabel(""),1,0,2,18)

        mainBox.addWidget(self.WUserNameLbl, 3,1,1,2)
        mainBox.addWidget(self.WUserNameLed, 3,3,1,10)
        mainBox.addWidget(self.WUserNameInfo, 3,13,1,4)

        mainBox.addWidget(self.WUserAccountLbl, 4,1,1,2)
        mainBox.addWidget(self.WUserAccountLed, 4,3,1,7)
        mainBox.addWidget(self.WUserAccountExist, 4,10,1,3)
        mainBox.addWidget(self.WUserAccountInfo, 4,13,1,4)

        mainBox.addWidget(self.WUserPinLbl, 5,1,1,2)
        mainBox.addWidget(self.WUserPinLed, 5,3,1,10)
        mainBox.addWidget(self.WUserPinInfo, 5,13,1,4)

        mainBox.addWidget(self.WUserRePinLbl, 6,1,1,2)
        mainBox.addWidget(self.WUserRePinLed, 6,3,1,10)
        mainBox.addWidget(self.WUserRePinInfo, 6,13,1,4)

        mainBox.addWidget(self.WUserPhoneLbl, 7,1,1,2)
        mainBox.addWidget(self.WUserPhoneLed, 7,3,1,10)
        mainBox.addWidget(self.WUserPhoneInfo, 7,13,1,4)

        mainBox.addWidget(self.WUserEmailLbl, 8,1,1,2)
        mainBox.addWidget(self.WUserEmailLed, 8,3,1,10)
        mainBox.addWidget(self.WUserEmailInfo, 8,13,1,4)

        mainBox.addWidget(self.WUserSexLbl, 9,1,1,2)
        mainBox.addWidget(self.WUserSexCmb, 9,3,1,10)
        mainBox.addWidget(self.WUserSexInfo, 9,13,1,4)

        # 为了演示新插入的
        mainBox.addWidget(self.WUserAgeLbl, 10,1,1,2)
        mainBox.addWidget(self.WUserAgeSpb, 10,3,1,10)
        mainBox.addWidget(QLabel(""), 10,13,1,4)

        mainBox.addWidget(self.WUserAddressLbl, 11,1,1,2)
        mainBox.addWidget(self.WUserAddressLed, 11,3,1,10)
        mainBox.addWidget(self.WUserAddressInfo, 11,13,1,4)

        mainBox.addWidget(QLabel(""), 12,0,1,18)

        mainBox.addWidget(self.WUserResetBtn, 13,4,1,4)
        mainBox.addWidget(self.WUserSubmitBtn, 13,8,1,4)

        self.contentContainer.setLayout(mainBox)

        content = QFormLayout()
        content.addWidget(self.contentContainer)
        self.setLayout(content)

    # 由于未引用外部QSS样式表，这一部分的有些内容并不起作用
    def initUIStyle(self):
        self.setProperty("class", "register")
        self.contentContainer.setProperty("class", "register_content")

        self.WUserNameLbl.setAlignment(Qt.AlignRight)
        self.WUserAccountLbl.setAlignment(Qt.AlignRight)
        self.WUserPinLbl.setAlignment(Qt.AlignRight)
        self.WUserRePinLbl.setAlignment(Qt.AlignRight)
        self.WUserPhoneLbl.setAlignment(Qt.AlignRight)
        self.WUserEmailLbl.setAlignment(Qt.AlignRight)
        self.WUserSexLbl.setAlignment(Qt.AlignRight)
        self.WUserAddressLbl.setAlignment(Qt.AlignRight)
        self.WUserAgeLbl.setAlignment(Qt.AlignRight)

        self.WBackToLogin.setProperty("class", "register_backtologin")
        self.pagename.setProperty("class", "register_title")
        self.WUserResetBtn.setProperty("class", "register_btn")
        self.WUserSubmitBtn.setProperty("class", "register_btn")

from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow_UI()
    demo.show()
    sys.exit(app.exec_())