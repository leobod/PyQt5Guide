# Author: Leobod
# Date  : 2019-04-21 11:43
# Description: QWidget的使用，前面基本都在用

# 导入包
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow_UI(QWidget):
    def __init__(self):
        super(MainWindow_UI, self).__init__()

        self.lbl = QLabel("这是一个QWidget的演示！,除了这个Label在无其他内容", self)

        # 使用下面的方法可以设置窗体的标题
        self.setWindowTitle("This is a demo Widget")

        # 使用下面的方法可以设置窗体的icon
        self.setWindowIcon(QIcon("icon/shield.png"))

        # 使用下面的方法可以设置窗体的大小
        self.resize(800,600)

        # 使用下面的方法可以设置窗体的左上角相对桌面的坐标
        self.move(100,100)

        # # 使用下面的方法同时设置位置与大小
        # self.setGeometry(100,100,800,600)

        # 使用下面的方法设置界面的透明度
        self.setWindowOpacity(0.9)

        # # 使用下面的方法设置界面的标题栏显示那些元素
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowMaximizeButtonHint)
        #           + Qt.FramelessWindowHint            标题栏不显示
        #           + Qt.WindowStaysOnTopHint: // 总在最上面的窗口
        #           + Qt.CustomizeWindowHint: // 自定义窗口标题栏, 以下标志必须与这个标志一起使用才有效, 否则窗口将有默认的标题栏
        #           + Qt.WindowTitleHint: 显示窗口标题栏
        #           + Qt.WindowSystemMenuHint: // 显示系统菜单
        #           + Qt.WindowMinimizeButtonHint: // 显示最小化按钮
        #           + Qt.WindowMaximizeButtonHint: // 显示最大化按钮
        #           + Qt.WindowMinMaxButtonsHint: // 显示最小化按钮和最大化按钮
        #           + Qt.WindowCloseButtonHint: // 显示关闭按钮

        # # 设置窗口是否为模态
        self.setWindowModality(Qt.ApplicationModal)
        #           + Qt.NonModal		# 非模态
        #           + Qt.WindowModal	# 窗口模态
        #           + Qt.ApplicationModal



from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow_UI()
    # 显示界面
    win.show()
    sys.exit(app.exec_())