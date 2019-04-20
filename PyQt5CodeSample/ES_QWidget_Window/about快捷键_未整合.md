## 2.设置快捷键
+ 快捷键(也要称热键)一些特别键的组合，用来快速设置输入焦点。按下输入焦点所在按钮的快捷键，按钮将被按下。
+ 要设置快捷键，需要在相应字母前加上“&”，程序运行后，在相应字母下加上下划线以提示用户。 按下+带下划线的字母，对应的控件获得输入焦点。
+ 对于编辑框这类没有文本的控件，在设置快捷键时，要先创建一个QLabel对象，并通过调用 setBuddy(component)与控件相关联。
+ 如果不想创建QLabel对象，可使用QWidget的下列方法：
+ grabShortcut (Keys [,Context]) 
    + 登记快捷键，返回一个标识符。
        + 参数Keys为QKeySequence对象。设置+快捷键的Keys设置方式为：
+ QtQui.QKeySequence.mmemonic("&e")
+ QtGui.QKeySequence("Alt+e")
+ QtGui.QKeySequence(QtCore.Qt.ALT + QtCore.Qt.Key_E)

+ Context参数可设置为Qt中的枚举变量：WidgetShortcut、WidgetWithChildrenShortcut、WindowsShortcut(默认值 )和ApplicationShortcut。
releaseshortcut (ID) - 删除标识符为ID的组合键；
+ setShortcutEnabled(ID[,Flag]) 
    + Flag为True时，标识符为ID的组合键有效；否则，无效。
+ 按下快捷键时，产生QEvent.Shortcut事件，可在函数event(self,event)中处理。event参数是QShortcutEvent对象，有以下方法：
    + shortcutId():返回快捷键的标识符。
    + isAmbiguous():如果事件同时发送给几个控件，返回True；否则，返回Fasle.
    + key():返回代表所按下快捷键的QkeySequence对象。