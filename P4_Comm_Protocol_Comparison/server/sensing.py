# Qt Based application meant to be run on RPI3
# Gets data from DHT22 Sensor and displays it in Qt GUI
# Author: Mukund Madhusudan Atre and Anirudh Tiwari

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient as aws
from PyQt5 import QtCore, QtGui, QtWidgets
import aiocoap.resource as resource
import paho.mqtt.client as mqtt
import matplotlib.pyplot as mplot
from PyQt5.QtCore import QTimer
import Adafruit_DHT as sense
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import threading
import datetime
import aiocoap
import socket
import logging
import asyncio
import json
import numpy
import time
import pika
import csv
import sys
import ssl
import os



class Ui_Sensors(object):
# Initializing necessary parameters
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
        #self.timer.timeout.connect(self.plotGraph)
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
            pydict = {'Temperature': temp_data, 'Humidity': humid_data}
            jsondict = json.dumps(pydict)
            # Publishing data to aws topic
            mqttaws_client.publish(topic, jsondict, 1)
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
            with open('th_data.csv', 'a', newline = '') as comfile:
                file_write = csv.writer(comfile, delimiter = ',')
                file_write.writerow([0, 0, 0, 0, 0, 0, 0, 0, self.getCurrTime()])
            print ("No Data Received; Try Again")


    #Get current date and time from QTimer()
    def getCurrTime(self):
        current = datetime.datetime.now()
        self.datetime_box.setText(current.strftime("%m/%d/%Y %H:%M"))
        return current.strftime("%m/%d/%Y %H:%M")

    # Functions for temperature unit conversion
    def cel_to_fah(self):
        self.mult_factor = 1.8
        self.add_factor = 32.0
        self.temp_unit = ' \u00b0' + 'F'

    def fah_to_cel(self):
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.temp_unit = ' \u00b0' + 'C'

    #Function for plotting graph by pulling values from .csv file
    def plotGraph(self):
        x = []
        y = []
        with open('th_data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(float(row[0]))
                y.append(float(row[1]))
        i = range(0,len(x))
        fig1 = mplot.figure(1)
        mplot.plot(i,x,'b')
        mplot.title('Humidity Variation Graph')
        fig1.savefig('humid_plot.jpg')

        fig2 = mplot.figure(2)
        mplot.plot(i,y,'r')
        mplot.title('Temperature Variation Graph')
        fig2.savefig('temp_plot.jpg')


# Blocking connection for CoAP Server
class BlockResource(resource.Resource):

    def set_content(self, content):
        self.content = content

    async def render_put(self, request):
        self.set_content(request.payload)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)

# Handler for QT
def UIhandler():
    app = QtWidgets.QApplication(sys.argv)
    Sensors = QtWidgets.QMainWindow()
    ui = Ui_Sensors()
    ui.setupUi(Sensors)
    Sensors.show()
    sys.exit(app.exec_())

# Handler for CoAp server
def CoAPserver():
    # Resource tree creation
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    root = resource.Site()

    root.add_resource(('.well-known', 'core'),
            resource.WKCResource(root.get_resources_as_linkheader))

    root.add_resource(('other', 'block'), BlockResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))

    loop = asyncio.get_event_loop()
    loop.run_forever()

# Handler for MQTT server
def mqtt_server():
    client = mqtt.Client()
    client.connect("localhost",1883,60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(up_topic)

def on_message(client, userdata, msg):
    client.publish(down_topic, msg.payload);

# Handler for websocket
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new websocket connection')

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print ('websocket connection closed')

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler)])

def websock_server():
    http_server = tornado.httpserver.HTTPServer(application)
    myIP = '127.0.0.1'
    port = 8888
    http_server.listen(8888, address='10.0.0.224')
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()


# Handler for Rabbit AMQP
def rabbitmq_server():
    channel.queue_declare(queue='up_queue')

    channel.basic_consume(callback,queue='up_queue', no_ack=True)

    channel.start_consuming()

def callback(ch, method, properties, body):
    channel.queue_declare(queue='down_queue')
    channel.basic_publish(exchange='', routing_key='down_queue', body= body )


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    mqttaws_client = None
    client_name = 'sensor_rpi'
    host = 'a1qcmx85kdext1.iot.us-east-2.amazonaws.com'
    rootCAPath = './certificates/root-CA.crt'
    privateKeyPath = './certificates/rpi-mma.private.key'
    certificatePath = './certificates/rpi-mma.cert.pem'
    topic = 'aws_eidp3'
    up_topic = 'mqtt_upstream'
    down_topic = 'mqtt_downstream'
    mqttaws_client = aws(client_name)
    mqttaws_client.configureEndpoint(host, 8883)
    mqttaws_client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
    mqttaws_client.connect()

# Thread declarations for UI and communication protocols
    threads = []
    uithread = threading.Thread(target=UIhandler)
    threads.append(uithread)
    uithread.start()

    coapthread = threading.Thread(target=CoAPserver)
    threads.append(coapthread)
    coapthread.daemon = True
    coapthread.start()

    mqtt_thread = threading.Thread(target=mqtt_server)
    threads.append(mqtt_thread)
    mqtt_thread.daemon = True
    mqtt_thread.start()

    websocket_thread = threading.Thread(target=websock_server)
    threads.append(websocket_thread)
    websocket_thread.daemon = True
    websocket_thread.start()

    rabbitmq_thread = threading.Thread(target=rabbitmq_server)
    threads.append(rabbitmq_thread)
    rabbitmq_thread.daemon = True
    rabbitmq_thread.start()
