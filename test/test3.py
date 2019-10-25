import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)
        self.pic_label.setPixmap(QPixmap('arrow.png'))

        self.listwidget_1 = QListWidget(self)  # 实例化列表控件
        self.listwidget_2 = QListWidget(self)
        self.listwidget_1.doubleClicked.connect(lambda: self.change_func(self.listwidget_1))
        # 双击列表控件时发出信号
        self.listwidget_2.doubleClicked.connect(lambda: self.change_func(self.listwidget_2))

        for i in range(6):
            text = 'Item {}'.format(i)
            self.item = QListWidgetItem(text)  # 把字符串转化为QListWidgetItem项目对象
            self.listwidget_1.addItem(self.item)  # 添加项目

        self.item_6 = QListWidgetItem('Item 6', self.listwidget_1)  # 实例化后直接添加

        self.listwidget_1.addItem('Item 7')  # 直接添加项目，不用QListWidgetItem对象，【功能可能不全】
        str_list = ['Item 9', 'Item 10']
        self.listwidget_1.addItems(str_list)  # 添加项目-列表

        self.item_8 = QListWidgetItem('Item 8')
        self.listwidget_1.insertItem(8, self.item_8)  # 插入项目。参数1：索引号,参数2：项目
        # self.listwidget_1.insertItem(8, 'Item 8')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listwidget_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listwidget_2)
        self.setLayout(self.h_layout)

        self.listwidget_1.itemClicked.connect(self.d)  # 单击列表控件时发出信号
        self.listwidget_1.currentItemChanged.connect(self.g)  # 当前项目发生变化时发出信号
        self.listwidget_1.addItem('Item_11')

    def g(self):
        print('项目总数发生了改变')

    def d(self):
        print('你单击了列表控件')

    def change_func(self, listwidget):
        if listwidget == self.listwidget_1:
            item = QListWidgetItem(self.listwidget_1.currentItem())  # 转化为QListWidgetItem对象
            # self.listwidget_1.currentItem()   返回当前项目。是个对象。<PyQt5.QtWidgets.QListWidgetItem object at 0x0000008425463A68>
            self.listwidget_2.addItem(item)  # 添加项目。参数是QListWidgetItem对象
            print(self.listwidget_2.count())  # 返回项目总数


        else:
            self.listwidget_2.takeItem(self.listwidget_2.currentRow())  # 删除指定索引号的项目
            # self.listwidget_2.currentRow()    返回当前项目的行索引号
            print(self.listwidget_2.count())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
