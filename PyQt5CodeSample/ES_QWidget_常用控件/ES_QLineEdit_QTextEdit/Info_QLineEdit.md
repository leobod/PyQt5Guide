## QLineEdit() [单行输入框]

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


## QTextEdit() [多行输入框]

### 获取/设置文本内容

```python
QTextEdit.setPlainText()					# 设置多行文本框内容
QTextEdit.toPlainText()						# 返回多行文本框内容
QTextEdit.setHtml()							# 设置Html格式文本
QTextEdit.toHtml()							# 返回Html文本格式内容
QTextEdit.clear()							# 清空内容
```

> 关于使用QTextEdit作为显示小部件的所有信息也适用于此处。<br />
> 通过setFontItalic()，setFontWeight()，setFontUnderline()，setFontFamily()，setFontPointSize()，setTextColor()和setCurrentFont()设置当前字符格式的属性。<br />
> 当前段落的对齐方式使用setAlignment()进行设置。