# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!


# GUI designed by Mukund Madhusudan Atre with help of Qt Creator
# References: Stack Overflow, Qt Documentation, ZetCode.com, YouTube,  Python.org examples

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import Adafruit_DHT as sense
import datetime
import matplotlib.pyplot as mplot
import numpy
import csv



class Ui_Sensors(object):
    #Initializing variables needed in computation of average
    def __init__(self):
        self.sum_humid = 0
        self.sum_temp = 0
        self.measure_count = 1

    def setupUi(self, Sensors):
        self.sum_humid = 0
        self.sum_temp = 0
        self.measure_count = 1
        #Main Window Object iniatialization
        Sensors.setObjectName("Sensors")
        Sensors.resize(742, 544)
        Sensors.setAnimated(True)
        Sensors.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(Sensors)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 100, 130, 27))
        font = QtGui.QFont()
        font.setPointSize(12)

        #Various text boxes and buttons needed in GUI
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 160, 130, 27))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(140, 105, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 165, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(140, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 370, 80, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 220, 130, 27))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 370, 80, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(610, 100, 31, 221))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar_2.setGeometry(QtCore.QRect(670, 100, 31, 221))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 460, 50, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("25")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 460, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(160, 460, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(250, 460, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 460, 50, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText("45")
        self.Message_label = QtWidgets.QLabel(self.centralWidget)
        self.Message_label.setGeometry(QtCore.QRect(420, 460, 281, 20))
        self.Message_label.setText("")
        self.Message_label.setObjectName("Message_label")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(620, 330, 16, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(680, 330, 16, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(270, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(390, 300, 130, 27))
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(255, 370, 130, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 300, 130, 27))
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(30, 300, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(310, 300, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        Sensors.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(Sensors)
        self.mainToolBar.setObjectName("mainToolBar")
        Sensors.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Sensors)
        self.statusBar.setObjectName("statusBar")
        Sensors.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(Sensors)
        self.toolBar.setObjectName("toolBar")
        Sensors.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(Sensors)
        self.toolBar_2.setObjectName("toolBar_2")
        Sensors.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(Sensors)
        self.toolBar_3.setObjectName("toolBar_3")
        Sensors.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)

        self.retranslateUi(Sensors)
        #Connecting User Actions to Functions that acquire and process data
        self.getCurrTime()
        self.queryData()
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        #self.pushButton.clicked.connect(self.queryData)
        self.timer = QTimer()
        self.timer.timeout.connect(self.getCurrTime)
        self.timer.timeout.connect(self.queryData)
        self.timer.start(5000)
        self.pushButton_3.clicked.connect(self.plotGraph)
        self.pushButton_2.clicked.connect(Sensors.close)
        QtCore.QMetaObject.connectSlotsByName(Sensors)

    def retranslateUi(self, Sensors):
        _translate = QtCore.QCoreApplication.translate
        Sensors.setWindowTitle(_translate("Sensors", "Weather"))
        self.label.setText(_translate("Sensors", "Temperature(T)"))
        self.label_2.setText(_translate("Sensors", "Humidity(H)"))
        self.label_3.setText(_translate("Sensors", "Date/Time"))
        self.pushButton.setText(_translate("Sensors", "Reset"))
        self.label_4.setText(_translate("Sensors", "Temperature and Humidity"))
        self.pushButton_2.setText(_translate("Sensors", "Exit"))
        self.label_5.setText(_translate("Sensors", "Threshold:"))
        self.label_6.setText(_translate("Sensors", "T"))
        self.label_7.setText(_translate("Sensors", "H"))
        self.label_8.setText(_translate("Sensors", "T"))
        self.label_9.setText(_translate("Sensors", "H"))
        self.label_10.setText(_translate("Sensors", "Average"))
        self.pushButton_3.setText(_translate("Sensors", "Plot Graph"))
        self.label_11.setText(_translate("Sensors", "Temperature"))
        self.label_12.setText(_translate("Sensors", "Humidity"))
        self.toolBar.setWindowTitle(_translate("Sensors", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("Sensors", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("Sensors", "toolBar_3"))

    #Function for querying data from sensors and storing data to .csv
    def queryData(self):
        threshold_temp = self.lineEdit_4.text()
        threshold_humid = self.lineEdit_5.text()
        #Function provided by Adafruit_DHT library for taking data from DHT22 sensor
        humidity, temperature = sense.read_retry(22,4)
        if humidity and temperature is not None:
            temp_data = '{0:.2f}'.format(temperature)
            humid_data = '{0:.2f}'.format(humidity)
            self.progressBar.setValue(float(temp_data))
            self.progressBar_2.setValue(float(humid_data))
            self.lineEdit.setText(temp_data)
            self.lineEdit_2.setText(humid_data)

            #Code for Alarm if values are greater than threshold
            if float(temp_data)>float(threshold_temp):
                self.progressBar.setStyleSheet("""QProgressBar::chunk {background-color: red;} """)
                self.Message_label.setText("Temperature Over Threshold!")
            else:
                self.progressBar.setStyleSheet("""QProgressBar::chunk {background-color: blue;} """)

            if float(humid_data)>float(threshold_humid):
                self.progressBar_2.setStyleSheet("""QProgressBar::chunk {background-color: red;} """)
                self.Message_label.setText("Humidity Over Threshold!")
            else:
                self.progressBar_2.setStyleSheet("""QProgressBar::chunk {background-color: blue;} """)

            self.Message_label.setText("Sensor Data Received")

            #Code for computing average of temperature and humidity values
            self.sum_humid += float(humid_data)
            self.sum_temp += float(temp_data)
            avg_humid = (self.sum_humid/float(self.measure_count))
            avg_temp = (self.sum_temp/float(self.measure_count))
            if self.measure_count==1:
                self.lineEdit_6.setText("")
                self.lineEdit_7.setText("")
            else:
                self.lineEdit_7.setText('{0:.2f}'.format(avg_temp))
                self.lineEdit_6.setText('{0:.2f}'.format(avg_humid))

            self.measure_count += 1

            #Writing acquired values to th_data.csv file
            with open('th_data.csv', 'a', newline = '') as comfile:
                file_write = csv.writer(comfile, delimiter = ',')
                file_write.writerow([humid_data, temp_data])
        #Error Checking if no data is Received
        else:
            self.Message_label.setText("No Data Received; Try Again")

    #Get current date and time from QTimer()
    def getCurrTime(self):
        current = datetime.datetime.now()
        self.lineEdit_3.setText(current.strftime("%m/%d/%Y %H:%M"))

    #Function for plotting graph by pulling values from .csv file
    def plotGraph(self):
        humid_data, temp_data = numpy.loadtxt('th_data.csv', delimiter = ',', unpack=True)
        i = range(0, len(temp_data))
        mplot.plot(i, temp_data)
        mplot.plot(i, humid_data)
        mplot.title("Temperature and Humidity Variation Graph")
        mplot.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sensors = QtWidgets.QMainWindow()
    ui = Ui_Sensors()
    ui.setupUi(Sensors)
    Sensors.show()
    sys.exit(app.exec_())
