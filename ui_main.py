"""主窗口UI"""
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(915, 695)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.video_bv_lineEdit = QLineEdit(self.centralwidget)
        self.video_bv_lineEdit.setObjectName(u"video_bv_lineEdit")
        self.video_bv_lineEdit.setGeometry(QRect(80, 60, 221, 61))
        self.wordcloud_name_lineEdit = QLineEdit(self.centralwidget)
        self.wordcloud_name_lineEdit.setObjectName(u"wordcloud_name_lineEdit")
        self.wordcloud_name_lineEdit.setGeometry(QRect(570, 70, 231, 21))
        self.video_bv_label = QLabel(self.centralwidget)
        self.video_bv_label.setObjectName(u"video_bv_label")
        self.video_bv_label.setGeometry(QRect(10, 60, 71, 51))
        self.wordcloudAttribute = QLabel(self.centralwidget)
        self.wordcloudAttribute.setObjectName(u"wordcloudAttribute")
        self.wordcloudAttribute.setGeometry(QRect(490, 30, 91, 31))
        font = QFont()
        font.setPointSize(12)
        self.wordcloudAttribute.setFont(font)
        self.generate_wordcloud_pushButton = QPushButton(self.centralwidget)
        self.generate_wordcloud_pushButton.setObjectName(u"generate_wordcloud_pushButton")
        self.generate_wordcloud_pushButton.setGeometry(QRect(350, 430, 201, 61))
        font1 = QFont()
        font1.setPointSize(19)
        self.generate_wordcloud_pushButton.setFont(font1)
        self.wordcloud_name_label = QLabel(self.centralwidget)
        self.wordcloud_name_label.setObjectName(u"wordcloud_name_label")
        self.wordcloud_name_label.setGeometry(QRect(470, 60, 111, 51))
        self.crawlerSettings = QLabel(self.centralwidget)
        self.crawlerSettings.setObjectName(u"crawlerSettings")
        self.crawlerSettings.setGeometry(QRect(10, 30, 81, 21))
        font2 = QFont()
        font2.setPointSize(13)
        self.crawlerSettings.setFont(font2)
        self.max_pages_label = QLabel(self.centralwidget)
        self.max_pages_label.setObjectName(u"max_pages_label")
        self.max_pages_label.setGeometry(QRect(0, 150, 91, 31))
        self.max_pages_lineEdit = QLineEdit(self.centralwidget)
        self.max_pages_lineEdit.setObjectName(u"max_pages_lineEdit")
        self.max_pages_lineEdit.setGeometry(QRect(90, 150, 211, 31))
        self.wordcloud_path_label = QLabel(self.centralwidget)
        self.wordcloud_path_label.setObjectName(u"wordcloud_path_label")
        self.wordcloud_path_label.setGeometry(QRect(480, 110, 91, 16))
        self.wordcloud_path_lineEdit = QLineEdit(self.centralwidget)
        self.wordcloud_path_lineEdit.setObjectName(u"wordcloud_path_lineEdit")
        self.wordcloud_path_lineEdit.setGeometry(QRect(570, 100, 231, 31))
        self.mask_pic_path_label = QLabel(self.centralwidget)
        self.mask_pic_path_label.setObjectName(u"mask_pic_path_label")
        self.mask_pic_path_label.setGeometry(QRect(490, 140, 61, 51))
        self.mask_pic_path_lineEdit = QLineEdit(self.centralwidget)
        self.mask_pic_path_lineEdit.setObjectName(u"mask_pic_path_lineEdit")
        self.mask_pic_path_lineEdit.setGeometry(QRect(570, 150, 231, 31))
        self.mask_pic_name_label = QLabel(self.centralwidget)
        self.mask_pic_name_label.setObjectName(u"mask_pic_name_label")
        self.mask_pic_name_label.setGeometry(QRect(450, 200, 141, 41))
        self.mask_pic_name_lineEdit = QLineEdit(self.centralwidget)
        self.mask_pic_name_lineEdit.setObjectName(u"mask_pic_name_lineEdit")
        self.mask_pic_name_lineEdit.setGeometry(QRect(570, 210, 231, 20))
        self.font_path_label = QLabel(self.centralwidget)
        self.font_path_label.setObjectName(u"font_path_label")
        self.font_path_label.setGeometry(QRect(500, 260, 51, 16))
        self.font_path_lineEdit = QLineEdit(self.centralwidget)
        self.font_path_lineEdit.setObjectName(u"font_path_lineEdit")
        self.font_path_lineEdit.setGeometry(QRect(570, 260, 231, 20))
        self.background_color_label = QLabel(self.centralwidget)
        self.background_color_label.setObjectName(u"background_color_label")
        self.background_color_label.setGeometry(QRect(500, 300, 51, 16))
        self.background_color_lineEdit = QLineEdit(self.centralwidget)
        self.background_color_lineEdit.setObjectName(u"background_color_lineEdit")
        self.background_color_lineEdit.setGeometry(QRect(570, 300, 231, 20))
        self.width_label = QLabel(self.centralwidget)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setGeometry(QRect(480, 340, 21, 16))
        self.width_lineEdit = QLineEdit(self.centralwidget)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setGeometry(QRect(510, 340, 111, 20))
        self.height_label = QLabel(self.centralwidget)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setGeometry(QRect(640, 340, 21, 16))
        self.height_lineEdit = QLineEdit(self.centralwidget)
        self.height_lineEdit.setObjectName(u"height_lineEdit")
        self.height_lineEdit.setGeometry(QRect(670, 340, 131, 20))
        self.crab_pic = QLabel(self.centralwidget)
        self.crab_pic.setObjectName(u"crab_pic")
        self.crab_pic.setGeometry(QRect(640, 420, 181, 141))
        self.crab_pic.setPixmap(QPixmap(u"./res/qt/img/crab.png"))
        self.bilibili_logo_pic = QLabel(self.centralwidget)
        self.bilibili_logo_pic.setObjectName(u"bilibili_logo_pic")
        self.bilibili_logo_pic.setGeometry(QRect(0, 200, 241, 91))
        self.bilibili_logo_pic.setPixmap(QPixmap(u"./res/qt/img/bilibili_logo.png"))
        self.about = QLabel(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(20, 420, 211, 71))
        font3 = QFont()
        font3.setPointSize(22)
        self.about.setFont(font3)
        self.about2 = QLabel(self.centralwidget)
        self.about2.setObjectName(u"about2")
        self.about2.setGeometry(QRect(160, 480, 71, 21))
        self.about_pic = QLabel(self.centralwidget)
        self.about_pic.setObjectName(u"about_pic")
        self.about_pic.setGeometry(QRect(20, 520, 281, 131))
        self.about_pic.setPixmap(QPixmap(u"./res/qt/img/about.png"))
        self.pachong_pushButton = QPushButton(self.centralwidget)
        self.pachong_pushButton.setObjectName(u"pachong_pushButton")
        self.pachong_pushButton.setGeometry(QRect(0, 340, 121, 61))
        font4 = QFont()
        font4.setPointSize(15)
        self.pachong_pushButton.setFont(font4)
        self.del_checkBox = QCheckBox(self.centralwidget)
        self.del_checkBox.setObjectName(u"del_checkBox")
        self.del_checkBox.setGeometry(QRect(140, 350, 151, 41))
        font5 = QFont()
        font5.setPointSize(14)
        self.del_checkBox.setFont(font5)
        self.login_pushButton = QPushButton(self.centralwidget)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setGeometry(QRect(210, 220, 111, 51))
        self.login_pushButton.setFont(font2)
        self.cookies_lineEdit = QLineEdit(self.centralwidget)
        self.cookies_lineEdit.setObjectName(u"cookies_lineEdit")
        self.cookies_lineEdit.setGeometry(QRect(80, 290, 141, 20))
        self.cookies_label = QLabel(self.centralwidget)
        self.cookies_label.setObjectName(u"cookies_label")
        self.cookies_label.setGeometry(QRect(10, 290, 61, 21))
        self.cookies_label.setFont(font)
        self.cookies_pushButton = QPushButton(self.centralwidget)
        self.cookies_pushButton.setObjectName(u"cookies_pushButton")
        self.cookies_pushButton.setGeometry(QRect(240, 280, 151, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 915, 33))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bilibili Web Crawler && Wordcloud", None))
        self.video_bv_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"video_bv\u82e5\u4e0d\u586b\u5219\u9ed8\u8ba4\u83b7\u53d6\u4e0a\u6b21\u7ed3\u679c", None))
        self.wordcloud_name_lineEdit.setText("")
        self.wordcloud_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"wordcloud_name\u9ed8\u8ba4\u4e3awordcloud.png", None))
        self.video_bv_label.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7684BV\u53f7", None))
        self.wordcloudAttribute.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u4e91\u56fe\u5c5e\u6027", None))
        self.generate_wordcloud_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.wordcloud_name_label.setText(QCoreApplication.translate("MainWindow", u"    \u8bcd\u4e91\u56fe\u540d\u5b57\n"
"(\u9ed8\u8ba4\u540e\u7f00\u4e3a.png)", None))
        self.crawlerSettings.setText(QCoreApplication.translate("MainWindow", u"\u722c\u866b\u8bbe\u7f6e", None))
        self.max_pages_label.setText(QCoreApplication.translate("MainWindow", u"\u722c\u53d6\u8bc4\u8bba\u533a\u9875\u6570", None))
        self.max_pages_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max_pages\u9ed8\u8ba4\u4e3a10(\u4e0d\u5b9c\u8fc7\u5927)", None))
        self.wordcloud_path_label.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u4e91\u56fe\u5b58\u653e\u8def\u5f84", None))
        self.wordcloud_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"wordcloud_path\u9ed8\u8ba4\u4e3a\u5f53\u524d\u6587\u4ef6\u5939\u4e0b", None))
        self.mask_pic_path_label.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u4e91\u56fe\u5f62\u72b6\n"
"(\u8499\u7248\u8def\u5f84)", None))
        self.mask_pic_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mask_pic_path\u9ed8\u8ba4\u4e3a./mask_pic/", None))
        self.mask_pic_name_label.setText(QCoreApplication.translate("MainWindow", u"       \u8bcd\u4e91\u56fe\u5f62\u72b6\n"
"(\u8499\u7248\u56fe\u7247\u540d\u79f0+\u540e\u7f00)", None))
        self.mask_pic_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mask_pic_name\u9ed8\u8ba4\u4e3a1.png", None))
        self.font_path_label.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u8def\u5f84", None))
        self.font_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"font_path\u9ed8\u8ba4\u4e3a./font/simfang.ttf", None))
        self.background_color_label.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f\u989c\u8272", None))
        self.background_color_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"background_color\u9ed8\u8ba4\u4e3awhite", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"\u5bbd", None))
        self.width_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"width\u9ed8\u8ba4\u4e3a800", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"\u957f", None))
        self.height_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"height\u9ed8\u8ba4\u4e3a600", None))
        self.crab_pic.setText("")
        self.bilibili_logo_pic.setText("")
        self.about.setText(QCoreApplication.translate("MainWindow", u"Made by \u9648\u6000\u5b87", None))
        self.about2.setText(QCoreApplication.translate("MainWindow", u"(24062013)", None))
        self.about_pic.setText("")
        self.pachong_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u722c\u53d6\u8bc4\u8bba", None))
        self.del_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u5206\u8bcd\u7ed3\u679c\u8fc7\u6ee4", None))
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.cookies_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u82e5\u6210\u529f\u767b\u5f55\u5219\u65e0\u9700\u586b\u5199", None))
        self.cookies_label.setText(QCoreApplication.translate("MainWindow", u"cookies", None))
        self.cookies_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u77e5\u9053\u600e\u4e48\u83b7\u53d6cookies?\n"
"\u70b9\u6211", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

