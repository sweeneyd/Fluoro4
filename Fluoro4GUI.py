# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fluoro4.ui'
#
# Created: Mon Jan 12 03:32:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 542)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 320, 411, 181))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 85, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 85, 18))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 120, 85, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 150, 85, 18))
        self.checkBox_5.setObjectName("checkBox_5")
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(50, 25, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 55, 104, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setEnabled(False)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 115, 104, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setEnabled(False)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 85, 104, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtGui.QComboBox(self.groupBox)
        self.comboBox_5.setEnabled(False)
        self.comboBox_5.setGeometry(QtCore.QRect(50, 145, 104, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_6.setEnabled(False)
        self.checkBox_6.setGeometry(QtCore.QRect(160, 30, 85, 18))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setGeometry(QtCore.QRect(250, 30, 85, 18))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_8.setEnabled(False)
        self.checkBox_8.setGeometry(QtCore.QRect(250, 60, 85, 18))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_9.setEnabled(False)
        self.checkBox_9.setGeometry(QtCore.QRect(160, 60, 85, 18))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_10.setEnabled(False)
        self.checkBox_10.setGeometry(QtCore.QRect(250, 90, 85, 18))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_11.setEnabled(False)
        self.checkBox_11.setGeometry(QtCore.QRect(160, 90, 85, 18))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_12.setEnabled(False)
        self.checkBox_12.setGeometry(QtCore.QRect(160, 120, 85, 18))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_13.setEnabled(False)
        self.checkBox_13.setGeometry(QtCore.QRect(250, 120, 85, 18))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_14.setEnabled(False)
        self.checkBox_14.setGeometry(QtCore.QRect(160, 150, 85, 18))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_15.setEnabled(False)
        self.checkBox_15.setGeometry(QtCore.QRect(250, 150, 85, 18))
        self.checkBox_15.setObjectName("checkBox_15")
        self.comboBox_6 = QtGui.QComboBox(self.groupBox)
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 25, 71, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtGui.QComboBox(self.groupBox)
        self.comboBox_7.setEnabled(False)
        self.comboBox_7.setGeometry(QtCore.QRect(330, 55, 71, 26))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtGui.QComboBox(self.groupBox)
        self.comboBox_8.setEnabled(False)
        self.comboBox_8.setGeometry(QtCore.QRect(330, 85, 71, 26))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtGui.QComboBox(self.groupBox)
        self.comboBox_9.setEnabled(False)
        self.comboBox_9.setGeometry(QtCore.QRect(330, 115, 71, 26))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtGui.QComboBox(self.groupBox)
        self.comboBox_10.setEnabled(False)
        self.comboBox_10.setGeometry(QtCore.QRect(330, 145, 71, 26))
        self.comboBox_10.setObjectName("comboBox_10")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 320, 331, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_11 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_11.setEnabled(False)
        self.comboBox_11.setGeometry(QtCore.QRect(50, 25, 71, 26))
        self.comboBox_11.setObjectName("comboBox_11")
        self.checkBox_20 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_20.setGeometry(QtCore.QRect(10, 90, 85, 18))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_17 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_17.setGeometry(QtCore.QRect(10, 60, 85, 18))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_18.setGeometry(QtCore.QRect(10, 120, 85, 18))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_19.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_16 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_16.setGeometry(QtCore.QRect(10, 150, 85, 18))
        self.checkBox_16.setObjectName("checkBox_16")
        self.comboBox_12 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_12.setEnabled(False)
        self.comboBox_12.setGeometry(QtCore.QRect(50, 55, 71, 26))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_13 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_13.setEnabled(False)
        self.comboBox_13.setGeometry(QtCore.QRect(50, 85, 71, 26))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_14 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_14.setEnabled(False)
        self.comboBox_14.setGeometry(QtCore.QRect(50, 115, 71, 26))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_15 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_15.setEnabled(False)
        self.comboBox_15.setGeometry(QtCore.QRect(50, 145, 71, 26))
        self.comboBox_15.setObjectName("comboBox_15")
        self.progressBar = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(130, 20, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_2.setEnabled(False)
        self.progressBar_2.setGeometry(QtCore.QRect(130, 50, 118, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_3.setEnabled(False)
        self.progressBar_3.setGeometry(QtCore.QRect(130, 80, 118, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_4.setEnabled(False)
        self.progressBar_4.setGeometry(QtCore.QRect(130, 110, 118, 23))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_5.setEnabled(False)
        self.progressBar_5.setGeometry(QtCore.QRect(130, 140, 118, 23))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.comboBox_16 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_16.setEnabled(False)
        self.comboBox_16.setGeometry(QtCore.QRect(260, 145, 71, 26))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_17 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_17.setEnabled(False)
        self.comboBox_17.setGeometry(QtCore.QRect(260, 85, 71, 26))
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_18 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_18.setEnabled(False)
        self.comboBox_18.setGeometry(QtCore.QRect(260, 55, 71, 26))
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_19 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_19.setEnabled(False)
        self.comboBox_19.setGeometry(QtCore.QRect(260, 25, 71, 26))
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_20 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_20.setEnabled(False)
        self.comboBox_20.setGeometry(QtCore.QRect(260, 115, 71, 26))
        self.comboBox_20.setObjectName("comboBox_20")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(160, 40, 56, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 56, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 56, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(160, 130, 56, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(160, 160, 56, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 10, 741, 311))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked(bool)"), self.comboBox.setEnabled)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked(bool)"), self.checkBox_6.setEnabled)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked(bool)"), self.checkBox_7.setEnabled)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked(bool)"), self.comboBox_6.setEnabled)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("clicked(bool)"), self.comboBox_2.setEnabled)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("clicked(bool)"), self.checkBox_9.setEnabled)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("clicked(bool)"), self.checkBox_8.setEnabled)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("clicked(bool)"), self.comboBox_7.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("clicked(bool)"), self.comboBox_4.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("clicked(bool)"), self.checkBox_11.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("clicked(bool)"), self.checkBox_10.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("clicked(bool)"), self.comboBox_8.setEnabled)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL("clicked(bool)"), self.comboBox_3.setEnabled)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL("clicked(bool)"), self.checkBox_12.setEnabled)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL("clicked(bool)"), self.checkBox_13.setEnabled)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL("clicked(bool)"), self.comboBox_9.setEnabled)
        QtCore.QObject.connect(self.checkBox_5, QtCore.SIGNAL("clicked(bool)"), self.comboBox_5.setEnabled)
        QtCore.QObject.connect(self.checkBox_5, QtCore.SIGNAL("clicked(bool)"), self.checkBox_14.setEnabled)
        QtCore.QObject.connect(self.checkBox_5, QtCore.SIGNAL("clicked(bool)"), self.checkBox_15.setEnabled)
        QtCore.QObject.connect(self.checkBox_5, QtCore.SIGNAL("clicked(bool)"), self.comboBox_10.setEnabled)
        QtCore.QObject.connect(self.checkBox_19, QtCore.SIGNAL("clicked(bool)"), self.comboBox_11.setEnabled)
        QtCore.QObject.connect(self.checkBox_19, QtCore.SIGNAL("clicked(bool)"), self.progressBar.setEnabled)
        QtCore.QObject.connect(self.checkBox_19, QtCore.SIGNAL("clicked(bool)"), self.label.setEnabled)
        QtCore.QObject.connect(self.checkBox_19, QtCore.SIGNAL("clicked(bool)"), self.comboBox_19.setEnabled)
        QtCore.QObject.connect(self.checkBox_17, QtCore.SIGNAL("clicked(bool)"), self.comboBox_18.setEnabled)
        QtCore.QObject.connect(self.checkBox_17, QtCore.SIGNAL("clicked(bool)"), self.progressBar_2.setEnabled)
        QtCore.QObject.connect(self.checkBox_17, QtCore.SIGNAL("clicked(bool)"), self.label_2.setEnabled)
        QtCore.QObject.connect(self.checkBox_17, QtCore.SIGNAL("clicked(bool)"), self.comboBox_12.setEnabled)
        QtCore.QObject.connect(self.checkBox_20, QtCore.SIGNAL("clicked(bool)"), self.comboBox_17.setEnabled)
        QtCore.QObject.connect(self.checkBox_20, QtCore.SIGNAL("clicked(bool)"), self.progressBar_3.setEnabled)
        QtCore.QObject.connect(self.checkBox_20, QtCore.SIGNAL("clicked(bool)"), self.label_3.setEnabled)
        QtCore.QObject.connect(self.checkBox_20, QtCore.SIGNAL("clicked(bool)"), self.comboBox_13.setEnabled)
        QtCore.QObject.connect(self.checkBox_18, QtCore.SIGNAL("clicked(bool)"), self.comboBox_20.setEnabled)
        QtCore.QObject.connect(self.checkBox_18, QtCore.SIGNAL("clicked(bool)"), self.progressBar_4.setEnabled)
        QtCore.QObject.connect(self.checkBox_18, QtCore.SIGNAL("clicked(bool)"), self.label_4.setEnabled)
        QtCore.QObject.connect(self.checkBox_18, QtCore.SIGNAL("clicked(bool)"), self.comboBox_14.setEnabled)
        QtCore.QObject.connect(self.checkBox_16, QtCore.SIGNAL("clicked(bool)"), self.comboBox_16.setEnabled)
        QtCore.QObject.connect(self.checkBox_16, QtCore.SIGNAL("clicked(bool)"), self.progressBar_5.setEnabled)
        QtCore.QObject.connect(self.checkBox_16, QtCore.SIGNAL("clicked(bool)"), self.label_5.setEnabled)
        QtCore.QObject.connect(self.checkBox_16, QtCore.SIGNAL("clicked(bool)"), self.comboBox_15.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Fluorophores", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("MainWindow", "5.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_6.setText(QtGui.QApplication.translate("MainWindow", "Excitation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setText(QtGui.QApplication.translate("MainWindow", "Emission", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_8.setText(QtGui.QApplication.translate("MainWindow", "Emission", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_9.setText(QtGui.QApplication.translate("MainWindow", "Excitation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_10.setText(QtGui.QApplication.translate("MainWindow", "Emission", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_11.setText(QtGui.QApplication.translate("MainWindow", "Excitation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_12.setText(QtGui.QApplication.translate("MainWindow", "Excitation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_13.setText(QtGui.QApplication.translate("MainWindow", "Emission", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_14.setText(QtGui.QApplication.translate("MainWindow", "Excitation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_15.setText(QtGui.QApplication.translate("MainWindow", "Emission", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_20.setText(QtGui.QApplication.translate("MainWindow", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_17.setText(QtGui.QApplication.translate("MainWindow", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_18.setText(QtGui.QApplication.translate("MainWindow", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_19.setText(QtGui.QApplication.translate("MainWindow", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_16.setText(QtGui.QApplication.translate("MainWindow", "5.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
