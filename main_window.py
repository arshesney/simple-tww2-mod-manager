# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modListTbl = QtWidgets.QTableWidget(self.centralwidget)
        self.modListTbl.setGeometry(QtCore.QRect(10, 10, 781, 501))
        self.modListTbl.setObjectName("modListTbl")
        self.modListTbl.setColumnCount(0)
        self.modListTbl.setRowCount(0)
        self.launchGameBtn = QtWidgets.QPushButton(self.centralwidget)
        self.launchGameBtn.setGeometry(QtCore.QRect(594, 520, 191, 41))
        self.launchGameBtn.setObjectName("launchGameBtn")
        self.selectAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectAllBtn.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.selectAllBtn.setObjectName("selectAllBtn")
        self.clearAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearAllBtn.setGeometry(QtCore.QRect(90, 530, 75, 23))
        self.clearAllBtn.setObjectName("clearAllBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.launchGameBtn.setText(_translate("MainWindow", "Launch Game"))
        self.selectAllBtn.setText(_translate("MainWindow", "Select All"))
        self.clearAllBtn.setText(_translate("MainWindow", "Clear All"))
