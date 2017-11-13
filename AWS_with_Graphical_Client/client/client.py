# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 377)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.RequestData = QtWidgets.QPushButton(self.centralWidget)
        self.RequestData.setGeometry(QtCore.QRect(310, 150, 141, 81))
        self.RequestData.setAutoFillBackground(False)
        self.RequestData.setObjectName("RequestData")
        self.FahrenheitToCelcius = QtWidgets.QRadioButton(self.centralWidget)
        self.FahrenheitToCelcius.setGeometry(QtCore.QRect(60, 160, 70, 27))
        self.FahrenheitToCelcius.setObjectName("FahrenheitToCelcius")
        self.CtoFlabel = QtWidgets.QLabel(self.centralWidget)
        self.CtoFlabel.setGeometry(QtCore.QRect(0, 240, 194, 21))
        self.CtoFlabel.setObjectName("CtoFlabel")
        self.CelciusToFahrenhite = QtWidgets.QRadioButton(self.centralWidget)
        self.CelciusToFahrenhite.setGeometry(QtCore.QRect(60, 270, 66, 27))
        self.CelciusToFahrenhite.setObjectName("CelciusToFahrenhite")
        self.FtoClabel = QtWidgets.QLabel(self.centralWidget)
        self.FtoClabel.setGeometry(QtCore.QRect(10, 130, 170, 21))
        self.FtoClabel.setObjectName("FtoClabel")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 201, 71))
        self.label.setAutoFillBackground(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setIndent(35)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 491, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RequestData.setText(_translate("MainWindow", "Request Data"))
        self.FahrenheitToCelcius.setText(_translate("MainWindow", "F to  C"))
        self.CtoFlabel.setText(_translate("MainWindow", "Change Scale to Fahrenhite"))
        self.CelciusToFahrenhite.setText(_translate("MainWindow", "C to F"))
        self.FtoClabel.setText(_translate("MainWindow", "Change Scale to Celcius"))
        self.label.setText(_translate("MainWindow", "Weather Statistics"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

