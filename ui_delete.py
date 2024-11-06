"""筛选窗口UI"""
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QMenu, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)


class del_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1042, 709)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.choose_all_checkBox = QCheckBox(self.centralwidget)
        self.choose_all_checkBox.setObjectName(u"choose_all_checkBox")
        self.choose_all_checkBox.setGeometry(QRect(470, 370, 91, 31))
        font = QFont()
        font.setPointSize(13)
        self.choose_all_checkBox.setFont(font)
        self.choose_all_checkBox.setChecked(False)
        self.delete_pushButton = QPushButton(self.centralwidget)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setGeometry(QRect(580, 460, 141, 81))
        font1 = QFont()
        font1.setPointSize(20)
        self.delete_pushButton.setFont(font1)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(470, 20, 101, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.n_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.n_checkBox.setObjectName(u"n_checkBox")

        self.verticalLayout.addWidget(self.n_checkBox)

        self.d_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.d_checkBox.setObjectName(u"d_checkBox")

        self.verticalLayout.addWidget(self.d_checkBox)

        self.a_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.a_checkBox.setObjectName(u"a_checkBox")

        self.verticalLayout.addWidget(self.a_checkBox)

        self.v_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.v_checkBox.setObjectName(u"v_checkBox")

        self.verticalLayout.addWidget(self.v_checkBox)

        self.i_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.i_checkBox.setObjectName(u"i_checkBox")

        self.verticalLayout.addWidget(self.i_checkBox)

        self.x_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.x_checkBox.setObjectName(u"x_checkBox")

        self.verticalLayout.addWidget(self.x_checkBox)

        self.c_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.c_checkBox.setObjectName(u"c_checkBox")

        self.verticalLayout.addWidget(self.c_checkBox)

        self.m_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.m_checkBox.setObjectName(u"m_checkBox")

        self.verticalLayout.addWidget(self.m_checkBox)

        self.un_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.un_checkBox.setObjectName(u"un_checkBox")

        self.verticalLayout.addWidget(self.un_checkBox)

        self.z_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.z_checkBox.setObjectName(u"z_checkBox")

        self.verticalLayout.addWidget(self.z_checkBox)

        self.eng_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.eng_checkBox.setObjectName(u"eng_checkBox")

        self.verticalLayout.addWidget(self.eng_checkBox)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(590, 20, 101, 331))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nr_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.nr_checkBox.setObjectName(u"nr_checkBox")

        self.verticalLayout_2.addWidget(self.nr_checkBox)

        self.ns_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.ns_checkBox.setObjectName(u"ns_checkBox")

        self.verticalLayout_2.addWidget(self.ns_checkBox)

        self.nt_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.nt_checkBox.setObjectName(u"nt_checkBox")

        self.verticalLayout_2.addWidget(self.nt_checkBox)

        self.nz_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.nz_checkBox.setObjectName(u"nz_checkBox")

        self.verticalLayout_2.addWidget(self.nz_checkBox)

        self.vd_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.vd_checkBox.setObjectName(u"vd_checkBox")

        self.verticalLayout_2.addWidget(self.vd_checkBox)

        self.vn_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.vn_checkBox.setObjectName(u"vn_checkBox")

        self.verticalLayout_2.addWidget(self.vn_checkBox)

        self.ad_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.ad_checkBox.setObjectName(u"ad_checkBox")

        self.verticalLayout_2.addWidget(self.ad_checkBox)

        self.an_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.an_checkBox.setObjectName(u"an_checkBox")

        self.verticalLayout_2.addWidget(self.an_checkBox)

        self.t_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.t_checkBox.setObjectName(u"t_checkBox")

        self.verticalLayout_2.addWidget(self.t_checkBox)

        self.r_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.r_checkBox.setObjectName(u"r_checkBox")

        self.verticalLayout_2.addWidget(self.r_checkBox)

        self.f_checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.f_checkBox.setObjectName(u"f_checkBox")

        self.verticalLayout_2.addWidget(self.f_checkBox)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(710, 20, 107, 331))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.u_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.u_checkBox.setObjectName(u"u_checkBox")

        self.verticalLayout_3.addWidget(self.u_checkBox)

        self.b_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.b_checkBox.setObjectName(u"b_checkBox")

        self.verticalLayout_3.addWidget(self.b_checkBox)

        self.e_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.e_checkBox.setObjectName(u"e_checkBox")

        self.verticalLayout_3.addWidget(self.e_checkBox)

        self.p_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.p_checkBox.setObjectName(u"p_checkBox")

        self.verticalLayout_3.addWidget(self.p_checkBox)

        self.q_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.q_checkBox.setObjectName(u"q_checkBox")

        self.verticalLayout_3.addWidget(self.q_checkBox)

        self.o_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.o_checkBox.setObjectName(u"o_checkBox")

        self.verticalLayout_3.addWidget(self.o_checkBox)

        self.s_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.s_checkBox.setObjectName(u"s_checkBox")

        self.verticalLayout_3.addWidget(self.s_checkBox)

        self.l_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.l_checkBox.setObjectName(u"l_checkBox")

        self.verticalLayout_3.addWidget(self.l_checkBox)

        self.j_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.j_checkBox.setObjectName(u"j_checkBox")

        self.verticalLayout_3.addWidget(self.j_checkBox)

        self.others_checkBox = QCheckBox(self.verticalLayoutWidget_3)
        self.others_checkBox.setObjectName(u"others_checkBox")

        self.verticalLayout_3.addWidget(self.others_checkBox)

        self.word_frequency_checkBox = QCheckBox(self.centralwidget)
        self.word_frequency_checkBox.setObjectName(u"word_frequency_checkBox")
        self.word_frequency_checkBox.setGeometry(QRect(870, 70, 101, 31))
        self.word_frequency_lineEdit = QLineEdit(self.centralwidget)
        self.word_frequency_lineEdit.setObjectName(u"word_frequency_lineEdit")
        self.word_frequency_lineEdit.setGeometry(QRect(850, 40, 131, 20))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 421, 571))
        self.selected_pushButton = QPushButton(self.centralwidget)
        self.selected_pushButton.setObjectName(u"selected_pushButton")
        self.selected_pushButton.setGeometry(QRect(850, 220, 131, 71))
        font2 = QFont()
        font2.setPointSize(19)
        self.selected_pushButton.setFont(font2)
        self.pic = QLabel(self.centralwidget)
        self.pic.setObjectName(u"pic")
        self.pic.setGeometry(QRect(840, 290, 151, 261))
        self.pic.setPixmap(QPixmap(u"./res/qt/img/pic.png"))
        self.head_lineEdit = QLineEdit(self.centralwidget)
        self.head_lineEdit.setObjectName(u"head_lineEdit")
        self.head_lineEdit.setGeometry(QRect(850, 110, 141, 20))
        self.head_checkBox = QCheckBox(self.centralwidget)
        self.head_checkBox.setObjectName(u"head_checkBox")
        self.head_checkBox.setGeometry(QRect(870, 150, 78, 19))
        self.choose_all_table_checkBox = QCheckBox(self.centralwidget)
        self.choose_all_table_checkBox.setObjectName(u"choose_all_table_checkBox")
        self.choose_all_table_checkBox.setGeometry(QRect(590, 370, 121, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.choose_all_table_checkBox.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1042, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u5206\u8bcd\u7ed3\u679c\u8fc7\u6ee4", None))
        self.choose_all_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009\u8bcd\u6027", None))
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.n_checkBox.setText(QCoreApplication.translate("MainWindow", u"n \u540d\u8bcd", None))
        self.d_checkBox.setText(QCoreApplication.translate("MainWindow", u"d \u526f\u8bcd", None))
        self.a_checkBox.setText(QCoreApplication.translate("MainWindow", u"a \u5f62\u5bb9\u8bcd", None))
        self.v_checkBox.setText(QCoreApplication.translate("MainWindow", u"v \u52a8\u8bcd", None))
        self.i_checkBox.setText(QCoreApplication.translate("MainWindow", u"i \u6210\u8bed", None))
        self.x_checkBox.setText(QCoreApplication.translate("MainWindow", u"x \u975e\u8bed\u7d20\u5b57", None))
        self.c_checkBox.setText(QCoreApplication.translate("MainWindow", u"c \u8fde\u8bcd", None))
        self.m_checkBox.setText(QCoreApplication.translate("MainWindow", u"m \u6570\u8bcd", None))
        self.un_checkBox.setText(QCoreApplication.translate("MainWindow", u"un \u672a\u77e5\u8bcd", None))
        self.z_checkBox.setText(QCoreApplication.translate("MainWindow", u"z \u72b6\u6001\u8bcd", None))
        self.eng_checkBox.setText(QCoreApplication.translate("MainWindow", u"eng \u82f1\u8bed", None))
        self.nr_checkBox.setText(QCoreApplication.translate("MainWindow", u"nr \u4eba\u540d", None))
        self.ns_checkBox.setText(QCoreApplication.translate("MainWindow", u"ns \u5730\u540d", None))
        self.nt_checkBox.setText(QCoreApplication.translate("MainWindow", u"nt \u673a\u6784\u56e2\u4f53", None))
        self.nz_checkBox.setText(QCoreApplication.translate("MainWindow", u"nz \u5176\u4ed6\u4e13\u540d", None))
        self.vd_checkBox.setText(QCoreApplication.translate("MainWindow", u"vd \u526f\u52a8\u8bcd", None))
        self.vn_checkBox.setText(QCoreApplication.translate("MainWindow", u"vn \u540d\u52a8\u8bcd", None))
        self.ad_checkBox.setText(QCoreApplication.translate("MainWindow", u"ad \u526f\u5f62\u8bcd", None))
        self.an_checkBox.setText(QCoreApplication.translate("MainWindow", u"an \u540d\u5f62\u8bcd", None))
        self.t_checkBox.setText(QCoreApplication.translate("MainWindow", u"t \u65f6\u95f4\u8bcd", None))
        self.r_checkBox.setText(QCoreApplication.translate("MainWindow", u"r \u4ee3\u8bcd", None))
        self.f_checkBox.setText(QCoreApplication.translate("MainWindow", u"f \u65b9\u4f4d\u8bcd", None))
        self.u_checkBox.setText(QCoreApplication.translate("MainWindow", u"u \u52a9\u8bcd", None))
        self.b_checkBox.setText(QCoreApplication.translate("MainWindow", u"b \u533a\u522b\u8bcd", None))
        self.e_checkBox.setText(QCoreApplication.translate("MainWindow", u"e \u53f9\u8bcd", None))
        self.p_checkBox.setText(QCoreApplication.translate("MainWindow", u"p \u4ecb\u8bcd", None))
        self.q_checkBox.setText(QCoreApplication.translate("MainWindow", u"q \u91cf\u8bcd", None))
        self.o_checkBox.setText(QCoreApplication.translate("MainWindow", u"o \u62df\u58f0\u8bcd", None))
        self.s_checkBox.setText(QCoreApplication.translate("MainWindow", u"s \u5904\u6240\u8bcd", None))
        self.l_checkBox.setText(QCoreApplication.translate("MainWindow", u"l \u4e60\u7528\u8bed", None))
        self.j_checkBox.setText(QCoreApplication.translate("MainWindow", u"j 	\u7b80\u79f0\u7565\u8bed", None))
        self.others_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u8bcd\u6027", None))
        self.word_frequency_checkBox.setText(
            QCoreApplication.translate("MainWindow", u"\u8bcd\u9891\u8fc7\u6ee4", None))
        self.word_frequency_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8bcd\u9891\u8fc7\u6ee4\u9ed8\u8ba4\u4e3a<=2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u52fe\u9009", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u6027", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8bcd", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u9891", None));
        self.selected_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u9009\u4e2d", None))
        self.pic.setText("")
        self.head_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u4fdd\u7559\u524d(\u9ed8\u8ba4100)\u4e2a", None))
        self.head_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7559\u8fc7\u6ee4", None))
        self.choose_all_table_checkBox.setText(
            QCoreApplication.translate("MainWindow", u"\u5168\u9009\u8868\u683c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi
