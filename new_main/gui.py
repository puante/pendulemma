# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledZmYhIc.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(439, 586)
        self.actionopen = QAction(mainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TitleLabel1 = QLabel(self.centralwidget)
        self.TitleLabel1.setObjectName(u"TitleLabel1")
        self.TitleLabel1.setGeometry(QRect(0, 0, 391, 41))
        font = QFont()
        font.setFamilies([u"\uad81\uc11c\uccb4"])
        font.setPointSize(28)
        self.TitleLabel1.setFont(font)
        self.p1_mass = QSpinBox(self.centralwidget)
        self.p1_mass.setObjectName(u"p1_mass")
        self.p1_mass.setGeometry(QRect(70, 100, 79, 26))
        self.p1_length = QSpinBox(self.centralwidget)
        self.p1_length.setObjectName(u"p1_length")
        self.p1_length.setGeometry(QRect(240, 100, 79, 26))
        self.p1_theta0 = QSpinBox(self.centralwidget)
        self.p1_theta0.setObjectName(u"p1_theta0")
        self.p1_theta0.setGeometry(QRect(70, 160, 79, 26))
        self.p1_theta0.setMinimum(-7)
        self.p1_theta0.setMaximum(7)
        self.p1_omega0 = QSpinBox(self.centralwidget)
        self.p1_omega0.setObjectName(u"p1_omega0")
        self.p1_omega0.setGeometry(QRect(240, 160, 79, 26))
        self.p1_omega0.setMinimum(-99)
        self.Pendulum1Label = QLabel(self.centralwidget)
        self.Pendulum1Label.setObjectName(u"Pendulum1Label")
        self.Pendulum1Label.setGeometry(QRect(0, 60, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"\uad81\uc11c\uccb4"])
        font1.setPointSize(14)
        self.Pendulum1Label.setFont(font1)
        self.Pendulum1Label.setMargin(3)
        self.LabelP1_1 = QLabel(self.centralwidget)
        self.LabelP1_1.setObjectName(u"LabelP1_1")
        self.LabelP1_1.setGeometry(QRect(40, 110, 31, 16))
        font2 = QFont()
        font2.setFamilies([u"\uad81\uc11c\uccb4"])
        self.LabelP1_1.setFont(font2)
        self.LabelP1_2 = QLabel(self.centralwidget)
        self.LabelP1_2.setObjectName(u"LabelP1_2")
        self.LabelP1_2.setGeometry(QRect(200, 110, 41, 16))
        self.LabelP1_2.setFont(font2)
        self.LabelP1_3 = QLabel(self.centralwidget)
        self.LabelP1_3.setObjectName(u"LabelP1_3")
        self.LabelP1_3.setGeometry(QRect(30, 170, 51, 16))
        self.LabelP1_3.setFont(font2)
        self.LabelP1_4 = QLabel(self.centralwidget)
        self.LabelP1_4.setObjectName(u"LabelP1_4")
        self.LabelP1_4.setGeometry(QRect(200, 170, 41, 16))
        self.LabelP1_4.setFont(font2)
        self.Pendulum2Label = QLabel(self.centralwidget)
        self.Pendulum2Label.setObjectName(u"Pendulum2Label")
        self.Pendulum2Label.setGeometry(QRect(10, 210, 71, 31))
        self.Pendulum2Label.setFont(font1)
        self.Pendulum2Label.setMargin(3)
        self.p2_mass = QSpinBox(self.centralwidget)
        self.p2_mass.setObjectName(u"p2_mass")
        self.p2_mass.setGeometry(QRect(70, 270, 79, 26))
        self.LabelP2_1 = QLabel(self.centralwidget)
        self.LabelP2_1.setObjectName(u"LabelP2_1")
        self.LabelP2_1.setGeometry(QRect(40, 280, 31, 16))
        self.LabelP2_1.setFont(font2)
        self.LabelP2_2 = QLabel(self.centralwidget)
        self.LabelP2_2.setObjectName(u"LabelP2_2")
        self.LabelP2_2.setGeometry(QRect(200, 280, 41, 16))
        self.LabelP2_2.setFont(font2)
        self.p2_length = QSpinBox(self.centralwidget)
        self.p2_length.setObjectName(u"p2_length")
        self.p2_length.setGeometry(QRect(240, 270, 79, 26))
        self.LabelP2_3 = QLabel(self.centralwidget)
        self.LabelP2_3.setObjectName(u"LabelP2_3")
        self.LabelP2_3.setGeometry(QRect(30, 340, 41, 16))
        self.LabelP2_3.setFont(font2)
        self.p2_theta0 = QSpinBox(self.centralwidget)
        self.p2_theta0.setObjectName(u"p2_theta0")
        self.p2_theta0.setGeometry(QRect(70, 330, 79, 26))
        self.p2_theta0.setMinimum(-7)
        self.p2_theta0.setMaximum(7)
        self.LabelP2_4 = QLabel(self.centralwidget)
        self.LabelP2_4.setObjectName(u"LabelP2_4")
        self.LabelP2_4.setGeometry(QRect(200, 340, 41, 16))
        self.LabelP2_4.setFont(font2)
        self.p2_omega0 = QSpinBox(self.centralwidget)
        self.p2_omega0.setObjectName(u"p2_omega0")
        self.p2_omega0.setGeometry(QRect(240, 330, 79, 26))
        self.p2_omega0.setMinimum(-99)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 470, 431, 71))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.notice = QLabel(self.centralwidget)
        self.notice.setObjectName(u"notice")
        self.notice.setGeometry(QRect(10, 380, 50, 16))
        self.notice.setFont(font2)
        self.notice_2 = QLabel(self.centralwidget)
        self.notice_2.setObjectName(u"notice_2")
        self.notice_2.setGeometry(QRect(20, 400, 311, 16))
        self.notice_2.setFont(font2)
        self.notice_3 = QLabel(self.centralwidget)
        self.notice_3.setObjectName(u"notice_3")
        self.notice_3.setGeometry(QRect(20, 420, 401, 16))
        self.notice_3.setFont(font2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 439, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionopen)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Double Pendulum Simulator", None))
        self.actionopen.setText(QCoreApplication.translate("mainWindow", u"\uc5f4\uae30", None))
        self.TitleLabel1.setText(QCoreApplication.translate("mainWindow", u"\uc774\uc911\uc9c4\uc790\u3161 \uc2dc\ubbac\ub808\uc774\uc200", None))
        self.Pendulum1Label.setText(QCoreApplication.translate("mainWindow", u"\uc9c4\uc790 1", None))
        self.LabelP1_1.setText(QCoreApplication.translate("mainWindow", u"\uc9c8\ub7c9", None))
        self.LabelP1_2.setText(QCoreApplication.translate("mainWindow", u"\uc904 \uae38\uc774", None))
        self.LabelP1_3.setText(QCoreApplication.translate("mainWindow", u"\ucd08\uae30\uac01", None))
        self.LabelP1_4.setText(QCoreApplication.translate("mainWindow", u"\uac01\uc18d\ub3c4", None))
        self.Pendulum2Label.setText(QCoreApplication.translate("mainWindow", u"\uc9c4\uc790 2", None))
        self.LabelP2_1.setText(QCoreApplication.translate("mainWindow", u"\uc9c8\ub7c9", None))
        self.LabelP2_2.setText(QCoreApplication.translate("mainWindow", u"\uc904 \uae38\uc774", None))
        self.LabelP2_3.setText(QCoreApplication.translate("mainWindow", u"\ucd08\uae30\uac01", None))
        self.LabelP2_4.setText(QCoreApplication.translate("mainWindow", u"\uac01\uc18d\ub3c4", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\ud601\uba85\uc801 \uc2dc\ubbac\ub808\uc774\uc200 \uc9d1\ud589", None))
        self.notice.setText(QCoreApplication.translate("mainWindow", u"\ucc38\uace0)", None))
        self.notice_2.setText(QCoreApplication.translate("mainWindow", u"\ubcf8 \uc2dc\ubbac\ub808\uc774\uc200\uc740 SI \ub2e8\uc704\uacc4\ub97c \uc0ac\uc6a9\ud558\uace0 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.notice_3.setText(QCoreApplication.translate("mainWindow", u"\uac01\ub3c4\ub294 Rad\uc774\uba70, \uae30\uc900\uc120 \uae30\uc900 \uc624\ub978\ucabd\uc774 \uc591, \uc67c\ucabd\uc774 \uc74c\uc5d0 \ud574\ub2f9\ub429\ub2c8\ub2e4.", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\ud30c\uc77c", None))
    # retranslateUi