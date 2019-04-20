# Author: Leobod
# Date  : 2019-04-20 19:33
# Description: QPushButton,QRadioButton,QComboBox的基本使用

# 引用包
from PyQt5.QtWidgets import QWidget,QPushButton,QRadioButton,QCheckBox,QComboBox,QButtonGroup,QLabel
from PyQt5.QtWidgets import QGridLayout,QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtCore import Qt

class Demo_QPushButton(QWidget):
    def __init__(self):
        super(Demo_QPushButton, self).__init__()
        self.initUI()
        self.initLayout()
        self.initEvents()
        self.initStyle()

    def initUI(self):
        # 标准文字按钮
        self.btn_001 = QPushButton("标准样式按钮")
        self.btn_002 = QPushButton("Warnning按钮")
        self.btn_003 = QPushButton("Success按钮")
        self.btn_004 = QPushButton("Tips按钮")
        self.btn_005 = QPushButton("不可用按钮")
        self.btn_005.setEnabled(False)
        # 控件基本都可以设置鼠标形状
        self.btn_001.setCursor(QCursor(Qt.ClosedHandCursor))

        # 标准按钮文字加icon
        self.btn_006 = QPushButton()
        self.btn_006.setIcon(QIcon("icon/draw.png"))
        self.btn_006.setText("图片名称draw")
        self.btn_007 = QPushButton()
        self.btn_007.setIcon(QIcon("icon/paper-plane.png"))
        self.btn_007.setText("图片名称paper-plane")
        self.btn_008 = QPushButton()
        self.btn_008.setIcon(QIcon("icon/shield.png"))
        self.btn_008.setText("图片名称shield")
        self.btn_009 = QPushButton()
        self.btn_009.setIcon(QIcon("icon/talk.png"))
        self.btn_009.setText("图片名称talk")
        self.btn_010 = QPushButton("扁平化按钮，不带样式")
        self.btn_010.setFlat(True)

        # 单选按钮
        self.btn_101 = QRadioButton()
        self.btn_101.setText("男")
        self.btn_102 = QRadioButton()
        self.btn_102.setText("女")
        self.btn_103 = QRadioButton()
        self.btn_103.setText("未知")

        # 多选按钮
        self.btn_201 = QCheckBox("篮球")
        self.btn_202 = QCheckBox("足球")
        self.btn_203 = QCheckBox("乒乓球")
        self.btn_204 = QCheckBox("羽毛球")
        self.btn_204.setTristate(True)
        # # 对应状态值 Qt.Checked    Qt.PartiallyChecked     Qt.Unchecked

        # # 加上 QButtonGroup 互斥开启
        # self.btn_group = QButtonGroup()
        # # setExclusive(bool)，默认Trus互斥，False关闭互斥
        # self.btn_group.setExclusive(False)
        # self.btn_group.addButton(self.btn_201)
        # self.btn_group.addButton(self.btn_202)
        # self.btn_group.addButton(self.btn_203)
        # self.btn_group.addButton(self.btn_204)
        # # 使用removeButton()解除
        # self.btn_group.removeButton()

        self.cbx = QComboBox()
        self.cbx.addItems(["2019", "2018", "2017", "2016", "2015"])

        pass

    def initLayout(self):
        contentBox = QGridLayout()
        contentBox.addWidget(self.btn_001, 0,0,1,1)
        contentBox.addWidget(self.btn_002, 0,1,1,1)
        contentBox.addWidget(self.btn_003, 0,2,1,1)
        contentBox.addWidget(self.btn_004, 0,3,1,1)
        contentBox.addWidget(self.btn_005, 0,4,1,1)

        contentBox.addWidget(self.btn_006, 1, 0, 1, 1)
        contentBox.addWidget(self.btn_007, 1, 1, 1, 1)
        contentBox.addWidget(self.btn_008, 1, 2, 1, 1)
        contentBox.addWidget(self.btn_009, 1, 3, 1, 1)
        contentBox.addWidget(self.btn_010, 1, 4, 1, 1)

        container1 = QWidget()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.btn_101)
        hbox1.addWidget(self.btn_102)
        hbox1.addWidget(self.btn_103)
        hbox1.setContentsMargins(0,0,0,0)
        container1.setLayout(hbox1)
        contentBox.addWidget(container1, 2,0,1,5)

        contentBox.addWidget(self.btn_201, 3,0,1,1)
        contentBox.addWidget(self.btn_202, 3,1,1,1)
        contentBox.addWidget(self.btn_203, 3,2,1,1)
        contentBox.addWidget(self.btn_204, 3,3,1,1)

        contentBox.addWidget(self.cbx, 4,0,1,2)

        contentBox.addWidget(QLabel(), 5, 0, 5, 1)

        self.setLayout(contentBox)
        pass

    def initEvents(self):
        self.btn_001.clicked.connect(self.eventDemo)
        self.btn_002.clicked.connect(self.eventDemo)
        self.btn_003.clicked.connect(self.eventDemo)
        self.btn_004.clicked.connect(self.eventDemo)

    def initStyle(self):
        self.btn_002.setStyleSheet("border-width: 2px; border-color: red; border-style: solid; border-radius: 5px; padding: 5px 10px;")
        self.btn_003.setStyleSheet("border-width: 2px; border-color: green; border-style: solid; border-radius: 5px; padding: 5px 10px;")
        self.btn_004.setStyleSheet("border-width: 2px; border-color: orange; border-style: solid; border-radius: 5px; padding: 5px 10px;")

    def eventDemo(self):
        QMessageBox.information(self, "提示信息对话框——标题","提示信息对话框——内容", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        pass


import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_QPushButton()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())