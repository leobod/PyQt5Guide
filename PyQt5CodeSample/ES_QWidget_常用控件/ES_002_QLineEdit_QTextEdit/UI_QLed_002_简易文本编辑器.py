# Author: Leobod
# Date  : 2019-04-20 18:13
# Description: 制作简单的文本编辑器
#                   + 实现： 选择文件，弹出文件选择框
#                   +       保存文件时，如何未关联文件，弹出文件选择框，选择要保存的路径，如果关联了文件直接保存
#                   +       实现 ctrl+s 快捷键保存文件

# import PyQt5Package
from PyQt5.QtWidgets import QWidget,QPushButton,QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QShortcut
from PyQt5.QtGui import QTextCharFormat,QKeySequence
from PyQt5.QtCore import Qt

class Demo_QLineEdit(QWidget):
    fname = ""
    def __init__(self):
        super(Demo_QLineEdit, self).__init__()
        self.initUI()
        self.initLayout()
        self.initEvents()
        # 快捷键绑定
        # QShortcut(QKeySequence("Escape"), self, self.close)

    def initUI(self):
        self.wChooseFile = QPushButton("选择文件")
        self.wSaveFile = QPushButton("保存")

        self.wEditArea = QTextEdit()

    def initLayout(self):
        # 建立布局对象
        contentBox = QVBoxLayout()
        menuBox = QHBoxLayout()
        areaBox = QHBoxLayout()

        # 转载menu布局的内容
        menuBox.addWidget(self.wChooseFile, stretch=1)
        menuBox.addStretch(20)
        menuBox.addWidget(self.wSaveFile, stretch=1)


        # 转载arae编辑区域布局的内容
        areaBox.addWidget(self.wEditArea)


        # 转载容器基本布局
        contentBox.addLayout(menuBox, stretch=1)
        contentBox.addLayout(areaBox, stretch=10)
        contentBox.setContentsMargins(0,0,0,0)

        # 将布局装入界面中
        self.setLayout(contentBox)


    def initEvents(self):
        self.wChooseFile.clicked.connect(self.eventChooseFile)
        self.wSaveFile.clicked.connect(self.eventSaveFile)
        # 绑定快捷键
        self.qs = QShortcut(QKeySequence("Ctrl+S"), self.wEditArea, self.eventSaveFile)

    def keySaveFile(self, event):
        print("按下：" + str(event.key()))


    def eventChooseFile(self):
        self.fname, f_type = QFileDialog.getOpenFileName(self, "选择一个文本文件", "", "文本文件 (*.txt *.md *)")
        # print(fname)      # fname 获取的文件路径
        # print(f_type)     # 获取的文件类型
        file_f = open(self.fname, "r", encoding='utf-8')
        content = file_f.read()
        self.wEditArea.setText(content)
        file_f.close()

    def eventSaveFile(self):
        s = self.wEditArea.toPlainText()
        if self.fname == "":
            self.fname, f_type = QFileDialog.getOpenFileName(self, "选择一个文本文件", "", "文本文件 (*.txt *.md *)")
        file_f = open(self.fname, "w", encoding="utf-8")
        file_f.write(s)
        file_f.close()
        QMessageBox.information(self, "文件保存提示", "文件保存成功", QMessageBox.Yes, QMessageBox.Yes)





import sys
from PyQt5.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo_QLineEdit()
    demo.resize(800,600)
    demo.show()
    sys.exit(app.exec())