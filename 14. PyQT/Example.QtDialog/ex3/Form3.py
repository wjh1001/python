# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form3.ui'
#
# Created: Mon Aug 24 16:21:30 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(720, 775)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(481, 415, 147, 22))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(481, 443, 231, 22))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(481, 471, 134, 22))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(481, 387, 133, 22))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(481, 359, 125, 22))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(481, 331, 182, 22))
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_9 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(481, 499, 173, 22))
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_10.setEnabled(True)
        self.checkBox_10.setGeometry(QtCore.QRect(481, 275, 115, 22))
        self.checkBox_10.setAcceptDrops(False)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 670, 671, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(480, 30, 151, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 560, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox_11 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(481, 303, 163, 22))
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 441, 611))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(481, 221, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 240, 122, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox_12 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(481, 527, 185, 22))
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 110, 157, 95))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinBox_2 = QtGui.QSpinBox(self.widget)
        self.spinBox_2.setMinimum(35)
        self.spinBox_2.setMaximum(70)
        self.spinBox_2.setProperty("value", 40)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBox_2)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.spinBox = QtGui.QSpinBox(self.widget)
        self.spinBox.setProperty("value", 7)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.spinBox_3 = QtGui.QSpinBox(self.widget)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setProperty("value", 3)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.checkBox.setText(_translate("MainWindow", "Generate XLS file", None))
        self.checkBox_3.setText(_translate("MainWindow", "Launching Time measurement", None))
        self.checkBox_4.setText(_translate("MainWindow", "Benchmark FPS", None))
        self.checkBox_5.setText(_translate("MainWindow", "Screen Capture", None))
        self.checkBox_6.setText(_translate("MainWindow", "File debug log", None))
        self.checkBox_7.setText(_translate("MainWindow", "Memory measurement", None))
        self.checkBox_9.setText(_translate("MainWindow", "HWUI PathCache Info", None))
        self.checkBox_10.setText(_translate("MainWindow", "Graph ouput", None))
        self.pushButton.setText(_translate("MainWindow", "RUN", None))
        self.checkBox_11.setText(_translate("MainWindow", "Copy files to Device", None))
        self.label_3.setText(_translate("MainWindow", "Config file", None))
        self.pushButton_2.setText(_translate("MainWindow", "Load config file", None))
        self.checkBox_12.setText(_translate("MainWindow", "Enable Systrace output", None))
        self.label_2.setText(_translate("MainWindow", "Temperature", None))
        self.label.setText(_translate("MainWindow", "Waiting Time", None))
        self.label_4.setText(_translate("MainWindow", "Iterations", None))

