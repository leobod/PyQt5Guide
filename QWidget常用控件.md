## QWidget()

### 设置大小

#### 设置大小，可修改

```python
QWidget.resize(width, height)

QWidget.resize(QSize)
```

#### 设置大小，固定

```python
QWidget.setFixedWidth(width)

QWidget.setFixedHeight(height)

QWidget.setFixedSize(QSize)

QWidget.setFixedSize(width, height)
```

#### 设置大小与窗口位置，相对于右上角

```python
QWidget.setGeometry(x, y, width, height)
QWidget.setGeometry(QRect)
```

### 获取宽度与高度

```python
QWidget.width()

QWidget.height()
```

### 获取窗口位置

```python
QWidget.pos()
```

### 设置窗口图标

```python
QWidget.setWindowIcon(QIcon)
```

### 设置窗口标题

```ython
QWidget.setWindowTitle(title)
```



### 窗口位置居中

#### 方案1

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.center()
        self.setWindowTitle('窗口居中')
        self.show()
        
    def center(self):
        qr = self.frameGeometry()							# 得到应用主窗体大小
        cp = QDesktopWidget().availableGeometry().center()	# 获取桌面当前位置和大小的中心
        qr.moveCenter(cp)									# 将 应用中间点 移到 屏幕中间点
        self.move(qr.topLeft())								# 将 应用左上标 设为 矩形左上标

if __name__ == '__main__':
    app = QApplication(sys.argv)							# 加载
    ex = Example()
    sys.exit(app.exec_())									# 退出功能
```

#### 方案2

```python
def center(self):
    screen = QDesktopWidget().screenGeometry()			# 获取桌面 大小
    size = self.geometry()								# 获取应用窗体大小
    self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)									# （桌面宽度- 窗体宽度）/2 …………………………
```



## QLabel()

### 设置文本对齐方式

```python
QLabel.setAlignment()
				Qt.AlignLeft		(水平左对齐)
    			Qt.AlignRight		(水平右对齐)
        		Qt.AlignCenter		(水平居中)
            	Qt.AlignJustify		(水平2端对齐)
                Qt.AlignTop			(垂直靠上)
                Qt.AlignBottom		(垂直靠下)
                Qt.AlignVCenter		(垂直居中)
```

### 设置文本缩进

```python
QLabel.setIndent()
```

### 设置Pixmap图片

```python
QLabel.setPixmap()
```

### 获取文本值与设置文本值

```python
QLabel.text()
QLabel.setText()				# 支持HTML格式
QLabel.selectedText()			# 获取选中的文字
```

### 设置快捷键

```python
QLabel.setBuddy()
```

### 是否允许换行

```python
QLabel.setWordWrap()
```

### 信号槽函数

```python
QLabel.linkActivated.connect()			# 标签中的超链接，希望在新窗口打开时，需要设置 setOpenExternalLinks为True
QLabel.linkHovered.connect()
```



## QLineEdit()

### 设置对齐方式

```python
QLineEdit.setAlignment()
```

### 文本框文字设置，修改，清空

```python
QLineEdit.clear()					# 清空
QLineEdit.setText()					# 设置文本
QLineEdit.text						# 获取文本
QLineEdit.setPlaceholderText()		# 设置占位符文本
QLineEdit.setEchoMode()				# 设置文本回显方式
			# QLineEdit.Normal
    		# QLineEdit.NoEcho
        	# QLineEdit.Password
            # QLineEdit.PasswordEchoOnEdit
```

### 其他

```python
QLineEdit.setMaxLength()		# 设置文本 最大长度
QLineEdit.setReadOnly()			# 设置文本只读
QLineEdit.setFocus()
QLineEdit.selectAll()
QLineEdit.setInputMask()
QLineEdit.setValidator()
			# QIntValidator			# 限制输入为整数
    		# QDoubleValidator		# 限制输入为 浮点数
        	# QRegexpValidator		# 限制输入为 符合正则表达式的内容
```

### 信号槽函数

```python
QLineEdit.selectionChanged.connect()		# 选择改变时 触发
QLineEdit.textChanged.connect()				# 文本改变时 触发
QLineEdit.editingFinished.connect()			# 编辑文本结束后 触发，一般是失去焦点时
```

