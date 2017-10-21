# Qt Based application meant to be run on RPI3
# Gets data from DHT22 Sensor and displays it in Qt GUI
# Author: Mukund Madhusudan Atre and Anirudh Tiwari

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import Adafruit_DHT as sense
import datetime
import matplotlib.pyplot as mplot
import numpy
import csv

class Ui_Sensors(object):

    def __init__(self):
        self.sum_humid = 0
        self.sum_temp = 0
        self.measure_count = 1
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.temp_unit = ' \u00b0' + 'C'
        self.max_temp = 0.0
        self.max_humid = 0.0
        self.min_temp = 50.0
        self.min_humid = 100.0

    def setupUi(self, Sensors):
        Sensors.setObjectName("Sensors")
        Sensors.resize(580, 589)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sensors.sizePolicy().hasHeightForWidth())
        Sensors.setSizePolicy(sizePolicy)
        Sensors.setAnimated(True)
        Sensors.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(Sensors)
        self.centralWidget.setObjectName("centralWidget")
        self.curr_temp_box = QtWidgets.QLineEdit(self.centralWidget)
        self.curr_temp_box.setGeometry(QtCore.QRect(340, 80, 130, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_temp_box.setFont(font)
        self.curr_temp_box.setFrame(False)
        self.curr_temp_box.setReadOnly(True)
        self.curr_temp_box.setObjectName("curr_temp_box")
        self.curr_humid_box = QtWidgets.QLineEdit(self.centralWidget)
        self.curr_humid_box.setGeometry(QtCore.QRect(340, 140, 130, 27))
        self.curr_humid_box.setFrame(False)
        self.curr_humid_box.setReadOnly(True)
        self.curr_humid_box.setObjectName("curr_humid_box")
        self.curr_temp_label = QtWidgets.QLabel(self.centralWidget)
        self.curr_temp_label.setGeometry(QtCore.QRect(90, 85, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_temp_label.setFont(font)
        self.curr_temp_label.setObjectName("curr_temp_label")
        self.curr_humid_label = QtWidgets.QLabel(self.centralWidget)
        self.curr_humid_label.setGeometry(QtCore.QRect(90, 145, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_humid_label.setFont(font)
        self.curr_humid_label.setObjectName("curr_humid_label")
        self.timestamp_label = QtWidgets.QLabel(self.centralWidget)
        self.timestamp_label.setGeometry(QtCore.QRect(90, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timestamp_label.setFont(font)
        self.timestamp_label.setObjectName("timestamp_label")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(140, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.datetime_box = QtWidgets.QLineEdit(self.centralWidget)
        self.datetime_box.setGeometry(QtCore.QRect(340, 200, 130, 27))
        self.datetime_box.setFrame(False)
        self.datetime_box.setReadOnly(True)
        self.datetime_box.setObjectName("datetime_box")
        self.avg_label = QtWidgets.QLabel(self.centralWidget)
        self.avg_label.setGeometry(QtCore.QRect(220, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avg_label.setFont(font)
        self.avg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avg_label.setObjectName("avg_label")
        self.avg_humid_box = QtWidgets.QLineEdit(self.centralWidget)
        self.avg_humid_box.setGeometry(QtCore.QRect(390, 290, 130, 27))
        self.avg_humid_box.setFrame(False)
        self.avg_humid_box.setReadOnly(True)
        self.avg_humid_box.setObjectName("avg_humid_box")
        self.avg_temp_box = QtWidgets.QLineEdit(self.centralWidget)
        self.avg_temp_box.setGeometry(QtCore.QRect(140, 290, 130, 27))
        self.avg_temp_box.setFrame(False)
        self.avg_temp_box.setReadOnly(True)
        self.avg_temp_box.setObjectName("avg_temp_box")
        self.avg_temp_label = QtWidgets.QLabel(self.centralWidget)
        self.avg_temp_label.setGeometry(QtCore.QRect(20, 290, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avg_temp_label.setFont(font)
        self.avg_temp_label.setObjectName("avg_temp_label")
        self.avg_humid_label = QtWidgets.QLabel(self.centralWidget)
        self.avg_humid_label.setGeometry(QtCore.QRect(300, 290, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avg_humid_label.setFont(font)
        self.avg_humid_label.setObjectName("avg_humid_label")
        self.max_label = QtWidgets.QLabel(self.centralWidget)
        self.max_label.setGeometry(QtCore.QRect(220, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_label.setFont(font)
        self.max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.max_label.setObjectName("max_label")
        self.max_temp_box = QtWidgets.QLineEdit(self.centralWidget)
        self.max_temp_box.setGeometry(QtCore.QRect(140, 370, 130, 27))
        self.max_temp_box.setFrame(False)
        self.max_temp_box.setReadOnly(True)
        self.max_temp_box.setObjectName("max_temp_box")
        self.max_temp_label = QtWidgets.QLabel(self.centralWidget)
        self.max_temp_label.setGeometry(QtCore.QRect(20, 370, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_temp_label.setFont(font)
        self.max_temp_label.setObjectName("max_temp_label")
        self.max_humid_label = QtWidgets.QLabel(self.centralWidget)
        self.max_humid_label.setGeometry(QtCore.QRect(300, 370, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_humid_label.setFont(font)
        self.max_humid_label.setObjectName("max_humid_label")
        self.max_humid_box = QtWidgets.QLineEdit(self.centralWidget)
        self.max_humid_box.setGeometry(QtCore.QRect(390, 370, 130, 27))
        self.max_humid_box.setFrame(False)
        self.max_humid_box.setReadOnly(True)
        self.max_humid_box.setObjectName("max_humid_box")
        self.min_label = QtWidgets.QLabel(self.centralWidget)
        self.min_label.setGeometry(QtCore.QRect(220, 410, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_label.setFont(font)
        self.min_label.setAlignment(QtCore.Qt.AlignCenter)
        self.min_label.setObjectName("min_label")
        self.min_temp_box = QtWidgets.QLineEdit(self.centralWidget)
        self.min_temp_box.setGeometry(QtCore.QRect(140, 450, 130, 27))
        self.min_temp_box.setFrame(False)
        self.min_temp_box.setReadOnly(True)
        self.min_temp_box.setObjectName("min_temp_box")
        self.min_humid_label = QtWidgets.QLabel(self.centralWidget)
        self.min_humid_label.setGeometry(QtCore.QRect(300, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_humid_label.setFont(font)
        self.min_humid_label.setObjectName("min_humid_label")
        self.min_temp_label = QtWidgets.QLabel(self.centralWidget)
        self.min_temp_label.setGeometry(QtCore.QRect(20, 450, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_temp_label.setFont(font)
        self.min_temp_label.setObjectName("min_temp_label")
        self.min_humid_box = QtWidgets.QLineEdit(self.centralWidget)
        self.min_humid_box.setGeometry(QtCore.QRect(390, 450, 130, 27))
        self.min_humid_box.setFrame(False)
        self.min_humid_box.setReadOnly(True)
        self.min_humid_box.setObjectName("min_humid_box")
        self.celsius_radio = QtWidgets.QRadioButton(self.centralWidget)
        self.celsius_radio.setGeometry(QtCore.QRect(150, 510, 117, 22))
        self.celsius_radio.setObjectName("celsius_radio")
        self.fahren_radio = QtWidgets.QRadioButton(self.centralWidget)
        self.fahren_radio.setGeometry(QtCore.QRect(300, 510, 117, 22))
        self.fahren_radio.setObjectName("fahren_radio")
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
        self.getCurrTime()
        self.celsius_radio.click()
        self.fahren_radio.clicked.connect(self.cel_to_fah)
        self.celsius_radio.clicked.connect(self.fah_to_cel)
        self.queryData()
        self.timer = QTimer()
        #self.timer.timeout.connect(self.getCurrTime)
        self.timer.timeout.connect(self.queryData)
        self.timer.start(5000)
        QtCore.QMetaObject.connectSlotsByName(Sensors)

    def retranslateUi(self, Sensors):
        _translate = QtCore.QCoreApplication.translate
        Sensors.setWindowTitle(_translate("Sensors", "Weather"))
        self.curr_temp_label.setText(_translate("Sensors", "Temperature(T)"))
        self.curr_humid_label.setText(_translate("Sensors", "Humidity(H)"))
        self.timestamp_label.setText(_translate("Sensors", "Date/Time"))
        self.label_4.setText(_translate("Sensors", "Temperature and Humidity"))
        self.avg_label.setText(_translate("Sensors", "Average"))
        self.avg_temp_label.setText(_translate("Sensors", "Temperature"))
        self.avg_humid_label.setText(_translate("Sensors", "Humidity"))
        self.max_label.setText(_translate("Sensors", "Maximum"))
        self.max_temp_label.setText(_translate("Sensors", "Temperature"))
        self.max_humid_label.setText(_translate("Sensors", "Humidity"))
        self.min_label.setText(_translate("Sensors", "Minimum"))
        self.min_humid_label.setText(_translate("Sensors", "Humidity"))
        self.min_temp_label.setText(_translate("Sensors", "Temperature"))
        self.celsius_radio.setText(_translate("Sensors", "Celsius"))
        self.fahren_radio.setText(_translate("Sensors", "Fahrenheit"))
        self.toolBar.setWindowTitle(_translate("Sensors", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("Sensors", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("Sensors", "toolBar_3"))


    #Function for querying data from sensors and storing data to .csv
    def queryData(self):
        #Function provided by Adafruit_DHT library for taking data from DHT22 sensor
        humidity, temperature = sense.read_retry(22,4)
        if humidity and temperature is not None:
            temp_data = '{0:.2f}'.format(temperature)
            humid_data = '{0:.2f}'.format(humidity)
            self.curr_temp_box.setText('{0:.2f}'.format((temperature*self.mult_factor)+ self.add_factor) + self.temp_unit)
            self.curr_humid_box.setText(humid_data  + '%')

            #Code for computing average of temperature and humidity values
            self.sum_humid += float(humidity)
            self.sum_temp += float(temperature)
            avg_humid = (self.sum_humid/float(self.measure_count))
            avg_temp = (self.sum_temp/float(self.measure_count))
            avg_temp_data = '{0:.2f}'.format(avg_temp)
            avg_humid_data = '{0:.2f}'.format(avg_humid)

            if self.measure_count==1:
                self.avg_temp_box.setText("")
                self.avg_humid_box.setText("")
            else:
                self.avg_temp_box.setText('{0:.2f}'.format((avg_temp*self.mult_factor)+self.add_factor)+self.temp_unit)
                self.avg_humid_box.setText('{0:.2f}'.format(avg_humid) + '%')

            self.measure_count += 1

            #Maximum and Minimum value computation
            if (temperature > self.max_temp):
                self.max_temp = temperature

            if (humidity > self.max_humid):
                self.max_humid = humidity

            if (temperature < self.min_temp):
                self.min_temp = temperature

            if (humidity < self.min_humid):
                self.min_humid = humidity

            max_temp_data = '{0:.2f}'.format(self.max_temp)
            min_temp_data = '{0:.2f}'.format(self.min_temp)
            max_humid_data = '{0:.2f}'.format(self.max_humid)
            min_humid_data = '{0:.2f}'.format(self.min_humid)
            self.max_temp_box.setText('{0:.2f}'.format((self.max_temp*self.mult_factor)+self.add_factor)+self.temp_unit)
            self.max_humid_box.setText('{0:.2f}'.format(self.max_humid)+'%')

            self.min_temp_box.setText('{0:.2f}'.format((self.min_temp*self.mult_factor)+self.add_factor)+self.temp_unit)
            self.min_humid_box.setText('{0:.2f}'.format(self.min_humid)+'%')

            #Writing acquired values to th_data.csv file
            with open('th_data.csv', 'a', newline = '') as comfile:
                file_write = csv.writer(comfile, delimiter = ',')
                file_write.writerow([humid_data, temp_data, avg_humid_data, avg_temp_data, max_humid_data, max_temp_data, min_humid_data, min_temp_data, self.getCurrTime()])


        #Error Checking if no data is Received
        else:
            print ("No Data Received; Try Again")

    #Get current date and time from QTimer()
    def getCurrTime(self):
        current = datetime.datetime.now()
        self.datetime_box.setText(current.strftime("%m/%d/%Y %H:%M"))
        return current.strftime("%m/%d/%Y %H:%M")

    def cel_to_fah(self):
        self.mult_factor = 1.8
        self.add_factor = 32.0
        self.temp_unit = ' \u00b0' + 'F'

    def fah_to_cel(self):
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.temp_unit = ' \u00b0' + 'C'


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sensors = QtWidgets.QMainWindow()
    ui = Ui_Sensors()
    ui.setupUi(Sensors)
    Sensors.show()
    sys.exit(app.exec_())
