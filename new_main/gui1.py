# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy,
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
        font.setFamilies([u"궁서체"])
        font.setPointSize(28)
        self.TitleLabel1.setFont(font)

        # ---- 진자 1 ----
        self.p1_mass = QDoubleSpinBox(self.centralwidget)
        self.p1_mass.setObjectName(u"p1_mass")
        self.p1_mass.setGeometry(QRect(70, 100, 79, 26))
        self.p1_mass.setMinimum(0.01)
        self.p1_mass.setMaximum(999.0)
        self.p1_mass.setDecimals(3)
        self.p1_mass.setSingleStep(0.1)
        self.p1_mass.setValue(1.0)

        self.p1_length = QDoubleSpinBox(self.centralwidget)
        self.p1_length.setObjectName(u"p1_length")
        self.p1_length.setGeometry(QRect(240, 100, 79, 26))
        self.p1_length.setMinimum(0.01)
        self.p1_length.setMaximum(999.0)
        self.p1_length.setDecimals(3)
        self.p1_length.setSingleStep(0.1)
        self.p1_length.setValue(1.0)

        self.p1_theta0 = QDoubleSpinBox(self.centralwidget)
        self.p1_theta0.setObjectName(u"p1_theta0")
        self.p1_theta0.setGeometry(QRect(70, 160, 79, 26))
        self.p1_theta0.setMinimum(-7.0)
        self.p1_theta0.setMaximum(7.0)
        self.p1_theta0.setDecimals(3)
        self.p1_theta0.setSingleStep(0.1)

        self.p1_omega0 = QDoubleSpinBox(self.centralwidget)
        self.p1_omega0.setObjectName(u"p1_omega0")
        self.p1_omega0.setGeometry(QRect(240, 160, 79, 26))
        self.p1_omega0.setMinimum(-99.0)
        self.p1_omega0.setMaximum(99.0)
        self.p1_omega0.setDecimals(3)
        self.p1_omega0.setSingleStep(0.1)

        self.Pendulum1Label = QLabel(self.centralwidget)
        self.Pendulum1Label.setObjectName(u"Pendulum1Label")
        self.Pendulum1Label.setGeometry(QRect(0, 60, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"궁서체"])
        font1.setPointSize(14)
        self.Pendulum1Label.setFont(font1)
        self.Pendulum1Label.setMargin(3)

        self.LabelP1_1 = QLabel(self.centralwidget)
        self.LabelP1_1.setObjectName(u"LabelP1_1")
        self.LabelP1_1.setGeometry(QRect(40, 110, 31, 16))
        font2 = QFont()
        font2.setFamilies([u"궁서체"])
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

        # ---- 진자 2 ----
        self.p2_mass = QDoubleSpinBox(self.centralwidget)
        self.p2_mass.setObjectName(u"p2_mass")
        self.p2_mass.setGeometry(QRect(70, 270, 79, 26))
        self.p2_mass.setMinimum(0.01)
        self.p2_mass.setMaximum(999.0)
        self.p2_mass.setDecimals(3)
        self.p2_mass.setSingleStep(0.1)
        self.p2_mass.setValue(1.0)

        self.LabelP2_1 = QLabel(self.centralwidget)
        self.LabelP2_1.setObjectName(u"LabelP2_1")
        self.LabelP2_1.setGeometry(QRect(40, 280, 31, 16))
        self.LabelP2_1.setFont(font2)

        self.LabelP2_2 = QLabel(self.centralwidget)
        self.LabelP2_2.setObjectName(u"LabelP2_2")
        self.LabelP2_2.setGeometry(QRect(200, 280, 41, 16))
        self.LabelP2_2.setFont(font2)

        self.p2_length = QDoubleSpinBox(self.centralwidget)
        self.p2_length.setObjectName(u"p2_length")
        self.p2_length.setGeometry(QRect(240, 270, 79, 26))
        self.p2_length.setMinimum(0.01)
        self.p2_length.setMaximum(999.0)
        self.p2_length.setDecimals(3)
        self.p2_length.setSingleStep(0.1)
        self.p2_length.setValue(1.0)

        self.LabelP2_3 = QLabel(self.centralwidget)
        self.LabelP2_3.setObjectName(u"LabelP2_3")
        self.LabelP2_3.setGeometry(QRect(30, 340, 41, 16))
        self.LabelP2_3.setFont(font2)

        self.p2_theta0 = QDoubleSpinBox(self.centralwidget)
        self.p2_theta0.setObjectName(u"p2_theta0")
        self.p2_theta0.setGeometry(QRect(70, 330, 79, 26))
        self.p2_theta0.setMinimum(-7.0)
        self.p2_theta0.setMaximum(7.0)
        self.p2_theta0.setDecimals(3)
        self.p2_theta0.setSingleStep(0.1)

        self.LabelP2_4 = QLabel(self.centralwidget)
        self.LabelP2_4.setObjectName(u"LabelP2_4")
        self.LabelP2_4.setGeometry(QRect(200, 340, 41, 16))
        self.LabelP2_4.setFont(font2)

        self.p2_omega0 = QDoubleSpinBox(self.centralwidget)
        self.p2_omega0.setObjectName(u"p2_omega0")
        self.p2_omega0.setGeometry(QRect(240, 330, 79, 26))
        self.p2_omega0.setMinimum(-99.0)
        self.p2_omega0.setMaximum(99.0)
        self.p2_omega0.setDecimals(3)
        self.p2_omega0.setSingleStep(0.1)

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

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Double Pendulum Simulator", None))
        self.actionopen.setText(QCoreApplication.translate("mainWindow", u"열기", None))
        self.TitleLabel1.setText(QCoreApplication.translate("mainWindow", u"이중진자ㅡ 시뮬레이션", None))
        self.Pendulum1Label.setText(QCoreApplication.translate("mainWindow", u"진자 1", None))
        self.LabelP1_1.setText(QCoreApplication.translate("mainWindow", u"질량", None))
        self.LabelP1_2.setText(QCoreApplication.translate("mainWindow", u"줄 길이", None))
        self.LabelP1_3.setText(QCoreApplication.translate("mainWindow", u"초기각", None))
        self.LabelP1_4.setText(QCoreApplication.translate("mainWindow", u"각속도", None))
        self.Pendulum2Label.setText(QCoreApplication.translate("mainWindow", u"진자 2", None))
        self.LabelP2_1.setText(QCoreApplication.translate("mainWindow", u"질량", None))
        self.LabelP2_2.setText(QCoreApplication.translate("mainWindow", u"줄 길이", None))
        self.LabelP2_3.setText(QCoreApplication.translate("mainWindow", u"초기각", None))
        self.LabelP2_4.setText(QCoreApplication.translate("mainWindow", u"각속도", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"혁명적 시뮬레이션 집행", None))
        self.notice.setText(QCoreApplication.translate("mainWindow", u"참고)", None))
        self.notice_2.setText(QCoreApplication.translate("mainWindow", u"본 시뮬레이션은 SI 단위계를 사용하고 있습니다.", None))
        self.notice_3.setText(QCoreApplication.translate("mainWindow", u"각도는 Rad이며, 기준선 기준 오른쪽이 양, 왼쪽이 음에 해당합니다.", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"파일", None))