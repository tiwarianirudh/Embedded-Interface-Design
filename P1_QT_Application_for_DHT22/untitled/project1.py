# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
#
# Author : Anirudh Tiwari
#
# Institution: University of Colorado Boulder

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import datetime
import Adafruit_DHT
import sys
import csv
import numpy
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def __init__(self):
        self.read_count=1
        self.total_temp=0
        self.total_humid=0
        self.temp_avg=0
        self.humid_avg=0
        self.opt_temp=0
        self.opt_humid=0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 592)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 121, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 110, 121, 31))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 67, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 111, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 510, 91, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 510, 91, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 510, 141, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 170, 291, 29))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 161, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 260, 81, 29))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(550, 260, 81, 29))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(390, 260, 141, 21))
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(430, 40, 121, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar_2.setGeometry(QtCore.QRect(430, 110, 118, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 400, 191, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 400, 81, 29))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText("20")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(360, 400, 171, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(550, 400, 81, 29))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText("50")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(680, 40, 201, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(680, 270, 201, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(686, 10, 191, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(680, 240, 191, 21))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTemp_Hum_Sensor = QtWidgets.QMenu(self.menuBar)
        self.menuTemp_Hum_Sensor.setTitle("")
        self.menuTemp_Hum_Sensor.setObjectName("menuTemp_Hum_Sensor")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuTemp_Hum_Sensor.menuAction())

        self.retranslateUi(MainWindow)
        self.getPresentTime()
        self.sensorData()
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.progressBar.reset)
        self.pushButton.clicked.connect(self.progressBar_2.reset)
        self.clock=QTimer()
        self.clock.timeout.connect(self.getPresentTime)
        self.clock.start(5000)
        self.pushButton.clicked.connect(self.sensorData)
        self.pushButton_3.clicked.connect(self.graph_temp)
        self.pushButton_3.clicked.connect(self.graph_hum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensor Data"))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.label_3.setText(_translate("MainWindow", "Date and Time"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Graph"))
        self.label_4.setText(_translate("MainWindow", "Average Temperature: "))
        self.label_5.setText(_translate("MainWindow", "Average Humidity"))
        self.label_6.setText(_translate("MainWindow", "Set Optimum Temperature"))
        self.label_7.setText(_translate("MainWindow", "Set Optimum Humidity"))
        self.label_8.setText(_translate("MainWindow", "      Temperature Alarm"))
        self.label_9.setText(_translate("MainWindow", "           Humidity Alarm "))

    def sensorData(self):
        # Reading Sensor Data
        humidity, temperature = Adafruit_DHT.read_retry(22,4)

        # Check for no data captured - Condition if data is successfully captured
        if humidity is not None and temperature is not None:
            temperature_data = '{0:.4f}'.format(temperature)
            humidity_data  = '{0:.4f}'.format(humidity)

            # Progress bar for sensor data values
            self.progressBar.setValue(float(temperature_data))
            self.progressBar_2.setValue(float(humidity_data))

            # Creating CSV file for storing the sensed data for Humidity and Temperature
            # Reference: https://docs.python.org/3.3/library/csv.html
            with open('sensor_data.csv', 'a', newline='') as csv_file:
                csvWriter = csv.writer(csv_file, delimiter=',')
                csvWriter.writerow([temperature_data, humidity_data])

            # Average/ Mean value calculations
            self.total_temp += float(temperature_data)
            self.total_humid += float(humidity_data)
            self.temp_avg = self.total_temp/self.read_count
            self.humid_avg = self.total_humid/self.read_count
            self.read_count += 1;

            # Alarm(Video) creation for optimum values input by the user
            opt_temp = self.lineEdit_6.text()
            opt_humid = self.lineEdit_7.text()
            # Reference: https://wiki.qt.io/How_to_Change_the_Background_Color_of_QWidget
            if float(temperature_data) > float(opt_temp) :
                self.graphicsView.setStyleSheet("background: red")
            else:
                self.graphicsView.setStyleSheet("background: green")

            if float(humidity_data) > float(opt_humid) :
                self.graphicsView_2.setStyleSheet("background: red")
            else:
                self.graphicsView_2.setStyleSheet("background: green")

        # Check for no data captured - Condition if data is not captured
        else:
            temperature_data = 'Failed. Retry!'
            humidity_data = 'Failed. Retry!'
            self.graphicsView.setStyleSheet("background: black")
            self.graphicsView_2.setStyleSheet("background: black")

        # Displaying the obtained data values
        self.lineEdit.setText(temperature_data)
        self.lineEdit_2.setText(humidity_data)
        self.lineEdit_4.setText('{0:.4f}'.format(self.temp_avg))
        self.lineEdit_5.setText('{0:.4f}'.format(self.humid_avg))

    # Graph Plotting for the obtained Temperature values
    # Refernce: https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
    def graph_temp(self):
        temperature_data, humidity_data = numpy.loadtxt('sensor_data.csv', delimiter=',', unpack=True)
        i = range(0, len(temperature_data))
        plt.plot(i, temperature_data)
        plt.xlabel('Reading Number')
        plt.ylabel('Temperature in Celcius')
        plt.show()

    # Graph Plotting for the obtained Humidity values
    # Refernce: https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
    def graph_hum(self):
        temperature_data, humidity_data = numpy.loadtxt('sensor_data.csv', delimiter=',', unpack=True)
        j = range(0, len(humidity_data))
        plt.plot(j, humidity_data)
        plt.xlabel('Reading Number')
        plt.ylabel('Humidity Value')
        plt.show()

    # Display the current time at data capture.
    # Reference: https://docs.python.org/2/library/datetime.html
    def getPresentTime(self):
        presentdateTime = datetime.datetime.now()
        self.lineEdit_3.setText(presentdateTime.strftime("%m/%d/%Y %H:%M"))

# Main Function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
