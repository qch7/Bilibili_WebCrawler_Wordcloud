"""筛选功能窗口"""
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox
from PySide6.QtCore import Qt
from ui_delete import del_Ui_MainWindow


class DelMainWindow(QMainWindow):
    """筛选功能窗口类"""
    def __init__(self):
        """初始化"""
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = del_Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        # 初始化默认筛选词性和词性勾选框列表
        self.cx_list = ["n", "d", "a", "v", "i", "x", "c", "m", "un", "z", "eng", "nr", "ns", "nt", "nz", "vd", "vn",
                        "ad", "an", "t", "r", "f", "u", "b", "e", "p", "q", "o", "s", "l", "j"]
        self.cx_checkBox_list = [self.ui.n_checkBox, self.ui.d_checkBox, self.ui.a_checkBox, self.ui.v_checkBox,
                                 self.ui.i_checkBox, self.ui.x_checkBox, self.ui.c_checkBox, self.ui.m_checkBox,
                                 self.ui.un_checkBox, self.ui.z_checkBox, self.ui.eng_checkBox, self.ui.nr_checkBox,
                                 self.ui.ns_checkBox, self.ui.nt_checkBox, self.ui.nz_checkBox, self.ui.vd_checkBox,
                                 self.ui.vn_checkBox, self.ui.ad_checkBox, self.ui.an_checkBox, self.ui.t_checkBox,
                                 self.ui.r_checkBox, self.ui.f_checkBox, self.ui.u_checkBox, self.ui.b_checkBox,
                                 self.ui.e_checkBox, self.ui.p_checkBox, self.ui.q_checkBox, self.ui.o_checkBox,
                                 self.ui.s_checkBox, self.ui.l_checkBox, self.ui.j_checkBox, self.ui.others_checkBox]
        # 筛选条件字典
        self.choose_dict = {}
        # 在窗口开启的时候进行初始化，防止调用上次的数据
        self.cx = None
        self.cx_others = None
        # 用循环初始化每个词性筛选勾选框的回调函数
        for cx_checkBox in self.cx_checkBox_list:
            cx_checkBox.stateChanged.connect(self.cx_select)
        # 初始化保留筛选勾选框的回调函数
        self.ui.head_checkBox.stateChanged.connect(self.head_select)
        # 初始化词频筛选勾选框的回调函数
        self.ui.word_frequency_checkBox.stateChanged.connect(self.word_frequency_select)
        # 初始化各个按钮的回调函数
        self.ui.delete_pushButton.clicked.connect(self.handle)
        self.ui.selected_pushButton.clicked.connect(self.select)
        # 初始化全选词性勾选框的回调函数
        self.ui.choose_all_checkBox.stateChanged.connect(self.choose_all_cx)
        # 初始化全选表格勾选框的回调函数
        self.ui.choose_all_table_checkBox.stateChanged.connect(self.update_table_full)

    def handle(self):
        """更新统计数据实现删除"""
        with open("./res/result/words.json", "r", encoding="utf-8") as f:
            words = dict(json.load(f))
        f.close()
        with open("./res/result/words_count.json", "r", encoding="utf-8") as f:
            words_count = dict(json.load(f))
        f.close()
        del_list = []
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox_item = self.ui.tableWidget.item(row, 0)
            if checkbox_item.checkState() == Qt.Checked:
                del_list.append(self.ui.tableWidget.item(row, 2).text())
        for del_word in del_list:
            del words[del_word]
            del words_count[del_word]
        with open("./res/result/words.json", "w", encoding="utf-8") as f:
            json.dump(words, f, indent=4)
        f.close()
        with open("./res/result/words_count.json", "w", encoding="utf-8") as f:
            json.dump(words_count, f, indent=4)
        f.close()
        # 更新筛选表格
        self.delete_table()
        self.ganerate_table()

    def head_select(self):
        """是否开启保留筛选"""
        self.choose_dict["head"] = True if self.ui.head_checkBox.checkState() == Qt.Checked else False

    def word_frequency_select(self):
        """是否开启词频筛选"""
        self.choose_dict["word_frequency"] = True if self.ui.word_frequency_checkBox.checkState() == Qt.Checked else False

    def cx_select(self):
        """是否开启词性筛选"""
        sender = QWidget.sender(self)  # 通过sender确定是哪个词性
        if sender == self.ui.others_checkBox:  # 对”其他词性“进行特殊处理
            for cx in self.cx_others:
                self.choose_dict[cx] = True if sender.checkState() == Qt.Checked else False
            return
        self.choose_dict[sender.text().split(" ")[0]] = True if sender.checkState() == Qt.Checked else False

    def select(self):
        """更新表格中的选择情况"""
        word_frequency = 2 if self.ui.word_frequency_lineEdit.text() == '' else int(self.ui.word_frequency_lineEdit.text())
        head = 100 if self.ui.head_lineEdit.text() == '' else int(self.ui.head_lineEdit.text())
        rows = self.ui.tableWidget.rowCount()
        for choose, state in self.choose_dict.items():
            # 处理词频筛选逻辑
            if choose == "word_frequency":
                for row in range(rows):
                    checkbox_item = self.ui.tableWidget.item(row, 0)
                    word_frequency_item = int(self.ui.tableWidget.item(row, 3).text())
                    if checkbox_item and word_frequency_item <= word_frequency:
                        checkbox_item.setCheckState(Qt.Checked if state else Qt.Unchecked)
            # 处理保留筛选逻辑
            elif choose == "head":
                if head > rows:  # 当保留过多数据时抛出警告
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setText(f"总共只有{rows}行！请重新设置保留值！")
                    msg_box.setWindowTitle("警告消息框")
                    msg_box.exec()
                    continue
                for row in range(head, rows):
                    checkbox_item = self.ui.tableWidget.item(row, 0)
                    if checkbox_item:
                        checkbox_item.setCheckState(Qt.Checked if state else Qt.Unchecked)
            # 处理词性筛选逻辑
            else:
                for row in range(rows):
                    checkbox_item = self.ui.tableWidget.item(row, 0)
                    cx_item = self.ui.tableWidget.item(row, 1).text()
                    if checkbox_item and cx_item == choose:
                        checkbox_item.setCheckState(Qt.Checked if state else Qt.Unchecked)

    def update_table_full(self):
        """是否全选表格中的数据"""
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox_item = self.ui.tableWidget.item(row, 0)
            if checkbox_item and self.ui.choose_all_table_checkBox.checkState() == Qt.Checked:
                checkbox_item.setCheckState(Qt.Checked)
            elif checkbox_item:
                checkbox_item.setCheckState(Qt.Unchecked)

    def choose_all_cx(self):
        """是否全选词性"""
        for cx_checkBox in self.cx_checkBox_list:
            if self.ui.choose_all_checkBox.checkState() == Qt.Checked:
                cx_checkBox.setCheckState(Qt.Checked)
            else:
                cx_checkBox.setCheckState(Qt.Unchecked)

    def ganerate_table(self):
        """根据words.json的数据更新表格"""
        try:
            with open("./res/result/words.json", "r", encoding="utf-8") as f:
                words = dict(json.load(f))
            f.close()
        except FileNotFoundError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(f"未找到words.json文件！请先爬取评论！")
            msg_box.setWindowTitle("警告消息框")
            msg_box.exec()
            self.close()
            return None
        row = 0
        cx = []
        for word, data in words.items():
            cx.append(data[1])
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox_item.setCheckState(Qt.Unchecked)
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, checkbox_item)
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(word))
            for i in range(2):
                self.ui.tableWidget.setItem(row, 3-2*i, QTableWidgetItem(data[i]))
            row += 1
        return set(cx)  # 利用集合进行去重

    def delete_table(self):
        """从最后一行逐行删除数据，以便展示更新后的表格"""
        for row in range(self.ui.tableWidget.rowCount()-1, -1, -1):
            self.ui.tableWidget.removeRow(row)
