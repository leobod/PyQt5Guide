# Author: Leobod
# Date  : 2019-04-20 19:14
# Description: 键盘事件

# import PyQt5Package
from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt

# 用于快捷键绑定事件的包
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

class Demo_Win(QWidget):

    def __init__(self):
        super(Demo_Win, self).__init__()
        self.initUI()
        self.initLayout()
        # 快捷键绑定
        # QShortcut(QKeySequence("Escape"), self, self.close)

    def initUI(self):
        self.tips = QLabel()

    def initLayout(self):
        contentBox = QVBoxLayout()
        contentBox.addWidget(self.tips)

        self.setLayout(contentBox)


    def keyPressEvent(self, event):
        # # 这里event.key（）显示的是按键的编码
        print("按下：" + str(event.key()))

        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        # 单个按键事件测试
        if (event.key() == Qt.Key_Control):
            print('测试：Ctrl')
            self.tips.setText('测试：Ctrl')
        if (event.key() == Qt.Key_A):
            print('测试：A')
            self.tips.setText('测试：A')
        if (event.key() == Qt.Key_Enter):
            print('测试：Enter')
            self.tips.setText('测试：Enter')
        if (event.key() == Qt.Key_Space):
            print('测试：Space')
            self.tips.setText('测试：Space')

        # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
        if (event.key() == Qt.Key_P):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + p")
                self.tips.setText('测试：shift + p')
            elif QApplication.keyboardModifiers() == Qt.ControlModifier:
                print("Ctrl + p")
                self.tips.setText('测试：Ctrl + p')
            else:
                print("p")
                self.tips.setText('测试：p')

        # 多个按键组合的事件
        if (event.key() == Qt.Key_O) and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            print("shift + o")
            self.tips.setText('测试：shift + o')





import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_Win()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())