# QWidget
```python
# 使用下面的方法可以设置窗体的标题
self.setWindowTitle("title")
# 使用下面的方法可以设置窗体的icon
self.setWindowIcon(QIcon("path"))
# 使用下面的方法可以设置窗体的大小
self.resize(width,height)
# 使用下面的方法可以设置窗体的左上角相对桌面的坐标
self.move(x,y)
# # 使用下面的方法同时设置位置与大小
# self.setGeometry(x,y,width,height)
# 使用下面的方法设置界面的透明度
self.setWindowOpacity(float_op)  # 值取 0.0-1.0
# # 使用下面的方法设置界面的标题栏显示那些元素
# self.setWindowFlag()
# self.setWindowFlags()
#           + Qt.FramelessWindowHint            标题栏不显示
#           + Qt.WindowStaysOnTopHint: // 总在最上面的窗口
#           + Qt.CustomizeWindowHint: // 自定义窗口标题栏, 以下标志必须与这个标志一起使用才有效, 否则窗口将有默认的标题栏
#           + Qt.WindowTitleHint: 显示窗口标题栏
#           + Qt.WindowSystemMenuHint: // 显示系统菜单
#           + Qt.WindowMinimizeButtonHint: // 显示最小化按钮
#           + Qt.WindowMaximizeButtonHint: // 显示最大化按钮
#           + Qt.WindowMinMaxButtonsHint: // 显示最小化按钮和最大化按钮
#           + Qt.WindowCloseButtonHint: // 显示关闭按钮
```

# QDialog 对话框

## QDialog

```pyqt5
setWindowTitle()				# 设置对话框标题
setWindowModality()				# 设置窗口是否为模态
		# Qt.NonModal		# 非模态
		# Qt.WindowModal	# 窗口模态
		# Qt.ApplicationModal
```

### 代码案例

```pyqt5
from PyQt5.QtGui import *
from PyQt5.QtWidget import *

class DialogDemo(QMainWindow):
	def __init__(self, parent=None):
		super().__init__()
		self.setWindowTitle("Str")
		self.resize(350,300)
		self.btn = QPushButton(self)		############
		self.btn.setText("str_name")
		self.btn.move(50,50)
		self.btn.clicked.connect(self.showDialog)
	def showDialog(self):
		dialog = QDialog
		btn = QPushButton("ok",dialog)		###########
		btn.move(50,50)
		dialog.setWindowTitle("Dialog")
		dialog.setWindowModality(Qt.ApplicationModal)
		dialog.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DialogDemo()
	demo.show()
	sys.exit(app.exec_())
		
```

## QMessageBox

```PyQt5
information(QWidget parent, title, text, buttons, defaultButton)
			# parent	指定父窗口
			# title		指定标题
			# text		指定文本
			# button	指定标准按钮
			# defaultButton	默认选中
question(QWidget parent, title, text, buttons, defaultButton)
warning(……………………)
ctitical(……………………)
about(QWidget parent, title, text)
setTitle()
setText()
setIcon()
```

```PyQt5
QMessage.OK
QMessage.Cancel
QMessage.Yes
QMessage.No
QMessage.Abort
QMessage.Retry
QMessage.Ignore
```

### 案例代码

```python
QMessageBox.information(self, "title", "text", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
```

## QInputDialog

```PyQt5
getInt()
getDouble()
getText()
getItem()
```

## QFontDialog

```PyQt5
def getFont(self):
	font,ok = QFontDialog.getFont()
	if ok:
		self.fontLineEdit.setFont(font)
```

## QFileDialog

```PyQt5
getOpenFileName()
getSaveFileName()
setFileMode()
	# QFileDialog.AnyFile
	# QFileDialog.ExistingFile
	# QFileDialog.Directory
	# QFileDialog.ExistingFiles
setFilter()
```

### 案例代码

```python
def getfile(self):
    fname, _ = QFileDialog.getOpenFileName(self, "open file", "c:\\","Image files (*.jpg *.gif)")
    self.le.setPixmap(QPixmap(fname))
```