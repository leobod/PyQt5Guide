## QAbstractButton() [抽象按钮]

### 获取状态

```python
QAbstractButton.isDown()					# 是否按下
QAbstractButton.isChecked()					# 是否被标记
QAbstractButton.isEnable()					# 是否可用
QAbstractButton.isCheckAble()				# 是否可标记
QAbstractButton.setAutoRepeat()				# 是否长按时可以重复执行
```

### 信号槽函数

```python
QAbstractButton.Pressed.connect()			# 按压时触发
QAbstractButton.Released.connect()			# 释放时触发
QAbstractButton.Clicked.connect()			# 点击后触发
QAbstractButton.Toggled.connect()			# 标记发生变化时触发
```



## QPushButton() [按钮]

### 设置是否可以选中

```python
QPushButton.setEnable(bool)
```

### 按钮装饰

```python
QPushButton.setText()
QPushButton.setIcon()
QPushButton.setDefault()				# 设置默认状态
```

### 获取按钮信息

```python
QPushButton.isChecked()
QPushButton.text()
```

### 信号槽函数

```python
# 参考 QAbstractButton
```



## QRadioButton() [单选按钮]

### 设置是否选中

```python
QRadioButton.setCheckable(bool)
```

### 装饰与获取

```python
QRadioButton..setText()
QRadioButton..text()

QRadioButton.isChecked()
```

### 信号槽函数

```python
# 参考 QAbstractButton
# 主要是使用
QRadioButton.tooggled.connect()
```



## QCheckBox() [多选按钮]

### 方法

```py
QCheckBox.setText()						# 设置多选框提示文字
QCheckBox.text()						# 返回多选框提示文字
QCheckBox.setChecked()					# 设置选中与否
QCheckBox.isChecked()					# 返回是否选中
QCheckBox.setTriState()					# 设置为3 态选框
				# 对应状态值
				Qt.Checked
				Qt.PartiallyChecked
				Qt.Unchecked
```

### 代码片段

```python
groupBox = QGroupBox()
checkBox1 = QCheckBox('name1')
checkBox2 = QCheckBox('name2')
checkBox3 = QCheckBox('name3')
box = QHBoxLayout()
box.addWidget(checkBox1)
box.addWidget(checkBox2)
box.addWidget(checkBox3)
groupBox.setLayout(box)

checkBox1.stateChanged.connect()
```

