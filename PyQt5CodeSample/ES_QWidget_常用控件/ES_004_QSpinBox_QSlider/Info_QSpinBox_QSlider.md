## QSpinBox() [计数器]

### 方法

```python
QSpinBox.setMinimum()				# 设置最小值（下界）
QSpinBox.setMaximum()				# 设置最大值（上界）
QSpinBox.singleStep()				# 设置步长
QSpinBox.setRange()					# 设置区间，步长
QSpinBox.setValue()					# 设置当前值
QSpinBox.value()					# 获取当前值

```

### 信号槽函数

```python
QSpinBox.valueChanged.connect()
```



## QSlider() [滑动条]

### 方法

```python
QSlider.setMinimum()				# 设置最小值（下界）
QSlider.setMaximum()				# 设置最大值（上界）
QSlider.singleStep()				# 设置步长
QSlider.setRange()					# 设置区间，步长
QSlider.setValue()					# 设置当前值
QSlider.value()						# 获取当前值
QSlider.setTickInterval()			# 设置刻度间隔
QSlider.setTrickPosition()			# 设置刻度标记位置
			# 有以下值
    `		QSlider.NoTicks				# 无刻度
    		QSlider.TicksBothSides		# 2侧刻度
        	QSlider.TicksAbove			# 上方刻度
            QSlider.TicksBelow			# 下方刻度
            QSlider.TicksLeft			# 左侧刻度
            QSlider.TicksRight			# 右侧刻度
```

### 信号槽函数

```python
QSlider.valueChanged.connect()
QSlider.sliderPressed.connect()			# 按下滑块时 触发
QSlider.sliderMoved.connect()			# 拖动滑块时 触发
QSlider.sliderReleased.connect()		# 释放滑块时 触发
```

