## QTable

### 常见属性/方法

```python
setRowCount(int_row)						 # 设置表格行数
setColumnCount(int_col)						 # 设置表格列数
setHorizontalHeaderLabels([list结构])			# 设置水平标签 
setVerticalHeaderLabels([list结构])			# 设置垂直标签
setItem(int, int, Item)						 # 设置单元格
setEditTriggers(type)						 # 设置表格是否可以编辑
			# QAbstractItemView.NoEditTriggers0No		不可编辑
    		# QAbstractItemView.CurrentChanged1Editing	可以修改
        	# QAbstractItemView.DoubleClicked2Editing	双击修改
            # QAbstractItemView.SelectedClicked4Editing	选中修改
            # QAbstractItemView.EditKeyPressed8Editing	特定键按下修改
            # QAbstractItemView.AnyKeyPressed16Editing
            # QAbstractItemView.AllEditTrigger31Editing
setSelectionBehavior()						# 设置表格选中后行为
			# QAbstractItemView.SelectItems0Selecting	选中单元格
    		# QAbstractItemView.SelectRows1Selecting	选中行
        	# QAbstractItemView.SelectColumns2Selecting	选中列
setTextAlignment()
setSpan(int_row, int_colum, int_rowspan, int_colspan)	# 合并单元格
setShowGrid()		# 是否显示网格线   # True/False
setColumnWidth(int_col, int_width)
setRowHeight(int_row, int_height)
rowCount()
columnCount()

resizeColumnsToContents()
resizeRowsToContents()

sortItems(column, orderType)
			# Qt.DescendingOrder		# 降序
    		# Qt.AscendingOrder			# 升序
```

### 案例代码1

```python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        self.tab = QTableWidget()
        self.tab.setRowCount(4)
        self.tab.setColumnCount(3)
        self.tab.setHorizontalHeaderLabels(["姓名：","性别：","出生日期："])
        # 添加标准item 内容 到表格
        self.tab.setItem(0,0,QTableWidgetItem("李四"))
        # 添加组件到表格
        self.sex_item = QComboBox()
        self.sex_item.addItems(["男","女","未知"])
        self.sex_item.setCurrentIndex(2)
        self.tab.setCellWidget(0,1,self.sex_item)
        self.tab.setItem(0,2,QTableWidgetItem("2019-3-31"))

        # 设置表格拉伸
        self.tab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tab.itemClicked.connect(self.itemContext)
        self.sex_item.currentIndexChanged.connect(self.showSex)


    def initLayout(self):
        mainBox = QHBoxLayout()
        mainBox.addWidget(self.tab)
        self.setLayout(mainBox)

    def itemContext(self, item):
        print("item行号是:"+str(item.row()+1))
        print("item列号是:"+str(item.column()+1))
        print("item内容是:"+item.text())

    def showSex(self):
        print(self.sex_item.currentText())

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TableDemo()
    demo.show()
    sys.exit(app.exec_())

```



## QTableView

### 常见属性值

```python
QStringListModel		# 存储一组字符
QStandardItemModel		# 存储多样化数据
QDirModel				# 文件模型
QSqlQueryModel			# SQL 结果封装
QSqlTableModel			# SQL 的表格封装
QSqlRelationTableModel	# SQL 带外键的表格封装
QSortFilterProxyModel	# 对模型数据进行排序与过滤

QTableView.setHorizontalHeaderLabels([list结构])	# 添加 表头 列表项
QTableView.setModel(Model_type_object)			 # 添加 对应数据的数据模型对象
QTableView.horizontalHeader().setStretchLastSection(True)	# 表尾部 拉伸填满窗口
QTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 拉伸表格填满窗口
```

### 案例代码1

```python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table View 的练习界面")
        self.resize(800,600)
        self.tab = QStandardItemModel(4,4)
        self.tab.setHorizontalHeaderLabels(["列表1","列表2","列表3","列表4"])

        for row in range(4):
            for col in range(4):
                item = QStandardItem("row %s, col %s" %(row, col))
                self.tab.setItem(row, col , item)

        self.tableView = QTableView()
        self.tableView.setModel(self.tab)

        layout = QHBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        # self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TableDemo()
    demo.show()
    sys.exit(app.exec_())

```



