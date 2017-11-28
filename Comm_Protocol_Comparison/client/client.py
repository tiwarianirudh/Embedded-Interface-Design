# -*- coding: utf-8 -*-
# Client Side for AWS with graphical Client Project
# Made by Mukund Madhusudan Atre and Anirudh Tiwari
from PyQt5 import QtCore, QtGui, QtWidgets
from websocket import create_connection
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
from aiocoap import *
import matplotlib
import threading
import datetime
import asyncio
import boto3
import json
import time
import sys
import ast
import sys



class Ui_MainWindow(object):

    def __init__(self):
        self.sqs = boto3.resource('sqs')
        # Call the queue by name
        self.queue = self.sqs.get_queue_by_name(QueueName='weather_queue')
        self.max_temp_list=[]
        self.min_temp_list=[]
        self.curr_temp_list=[]
        self.avg_temp_list=[]
        self.max_humid_list=[]
        self.min_humid_list=[]
        self.curr_humid_list=[]
        self.avg_humid_list=[]
        self.num_readings = 0
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.unit = " C\n"
        self.final_mesg = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1316, 671)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.RequestData = QtWidgets.QPushButton(self.centralWidget)
        self.RequestData.setGeometry(QtCore.QRect(330, 200, 181, 121))
        self.RequestData.setAutoFillBackground(False)
        self.RequestData.setObjectName("RequestData")
        self.FahrenheitToCelcius = QtWidgets.QRadioButton(self.centralWidget)
        self.FahrenheitToCelcius.setGeometry(QtCore.QRect(60, 210, 70, 27))
        self.FahrenheitToCelcius.setObjectName("FahrenheitToCelcius")
        self.CtoFlabel = QtWidgets.QLabel(self.centralWidget)
        self.CtoFlabel.setGeometry(QtCore.QRect(30, 310, 210, 21))
        self.CtoFlabel.setObjectName("CtoFlabel")
        self.CelciusToFahrenhite = QtWidgets.QRadioButton(self.centralWidget)
        self.CelciusToFahrenhite.setGeometry(QtCore.QRect(60, 350, 75, 27))
        self.CelciusToFahrenhite.setObjectName("CelsiusToFahrenheit")
        self.FtoClabel = QtWidgets.QLabel(self.centralWidget)
        self.FtoClabel.setGeometry(QtCore.QRect(30, 180, 210, 21))
        self.FtoClabel.setObjectName("FtoClabel")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 211, 131))
        self.label.setAutoFillBackground(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setIndent(35)
        self.label.setObjectName("label")
        # Message Box for displaying data/error messages
        self.MessageBox = QtWidgets.QTextEdit(self.centralWidget)
        self.MessageBox.setGeometry(QtCore.QRect(760, 0, 531, 601))
        self.MessageBox.setObjectName("MessageBox")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(630, 260, 67, 21))
        self.label_2.setObjectName("label_2")
        self.ClearMessage = QtWidgets.QPushButton(self.centralWidget)
        self.ClearMessage.setGeometry(QtCore.QRect(600, 520, 151, 29))
        self.ClearMessage.setObjectName("ClearMessage")
        self.Close = QtWidgets.QPushButton(self.centralWidget)
        self.Close.setGeometry(QtCore.QRect(210, 520, 121, 31))
        self.Close.setObjectName("Close")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1316, 26))
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
        # Calling appropriate functions on different button clicks
        self.Close.clicked.connect(MainWindow.close)
        self.ClearMessage.clicked.connect(self.MessageBox.clear)
        self.RequestData.clicked.connect(self.fetch_data)
        self.FahrenheitToCelcius.clicked.connect(self.fah_to_cel)
        self.CelciusToFahrenhite.clicked.connect(self.cel_to_fah)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RequestData.setText(_translate("MainWindow", "Request Data"))
        self.FahrenheitToCelcius.setText(_translate("MainWindow", "F to  C"))
        self.CtoFlabel.setText(_translate("MainWindow", "Change Scale to Fahrenheit"))
        self.CelciusToFahrenhite.setText(_translate("MainWindow", "C to F"))
        self.FtoClabel.setText(_translate("MainWindow", "Change Scale to Celsius"))
        self.label.setText(_translate("MainWindow", "Weather Statistics"))
        self.label_2.setText(_translate("MainWindow", "Message"))
        self.ClearMessage.setText(_translate("MainWindow", "Clear Message"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))



    def fetch_data(self):
        # Receive message from SQS queue
        queuelist = []
        for i in range(3):
            offload_list = self.queue.receive_messages(MaxNumberOfMessages=10)
            if not offload_list:
                break
        # Process messages by printing out body
            for msg in offload_list:
                msgbody = ast.literal_eval(msg.body)
                queuelist.append(msgbody)
        # delete the msg
                msg.delete()
                self.num_readings += 1

        # Take out data from individual messages and classify them based on key
        if queuelist:
            for mesg in queuelist:
                self.curr_temp_list.append(mesg["curr_temp"])
                self.curr_humid_list.append(mesg["curr_humid"])
                self.max_temp_list.append(mesg["max_temp"])
                self.max_humid_list.append(mesg["max_humid"])
                self.min_temp_list.append(mesg["min_temp"])
                self.min_humid_list.append(mesg["min_humid"])
                self.avg_temp_list.append(mesg["avg_temp"])
                self.avg_humid_list.append(mesg["avg_humid"])

            # generate message to be printed in Message Box
            self.final_mesg=""
            for max_t,min_t,curr_t,avg_t,max_h,min_h,curr_h,avg_h in zip(self.max_temp_list,\
                self.min_temp_list,self.curr_temp_list, self.avg_temp_list, self.max_humid_list,\
                self.min_humid_list, self.curr_humid_list, self.avg_humid_list):


                self.final_mesg +=   "Max Temp: {0:.2f}".format((max_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Min Temp: {0:.2f}".format((min_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Last Temp: {0:.2f}".format((curr_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Avg Temp: {0:.2f}".format((avg_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Max Hum: "+ str(max_h) + " %\n" + \
                                "Min Hum: "+ str(min_h) + " %\n" + \
                                "Last Hum: "+ str(curr_h) + " %\n" + \
                                "Avg Hum: "+ str(avg_h) + " %\n\n"


            self.MessageBox.setText("Fetched Data:\n"  + self.final_mesg + "\nTimestamp: " + str(datetime.datetime.now()))
            self.plotGraph()
            print("\nCoAP Data:\n")
            coapthread = threading.Thread(target=self.CoAPhandler)
            coap_t1 = time.time()
            coapthread.start()
            coapthread.join()
            coap_t2 = time.time()
            coap_exec_time = (coap_t2 - coap_t1)
            print('\nCoAP Protocol data exchange time: %s'% coap_exec_time)
            print("\n\nMQTT Data:\n")
            mqtt_t1 = time.time()
            client.publish(up_topic, self.final_mesg)
            msg_event.wait()
            mqtt_t2 = time.time()
            mqtt_exec_time = (mqtt_t2 - mqtt_t1)
            print('\nMQTT Protocol data exchange time: %s seconds'% mqtt_exec_time)
            msg_event.clear()
            web_t1 = time.time()
            self.websocket_client()
            web_t2 = time.time()
            web_exec_time = web_t2 - web_t1
            print('WebSocket Protocol data exchange time: %s'% web_exec_time)
        # Error Handling
        else:
            self.MessageBox.setText("Error Fetching Data \n")


    # Function for plotting graph of humidity and temperature separately
    def plotGraph(self):
        plt.plot(range(self.num_readings), self.max_temp_list, 'b-', label='Max Temp')
        plt.plot(range(self.num_readings), self.min_temp_list, 'r-', label='Min Temp')
        plt.plot(range(self.num_readings), self.curr_temp_list, 'y-', label='Last Temp')
        plt.plot(range(self.num_readings), self.avg_temp_list, 'g-', label='Avg Temp')
        plt.legend(loc='best')
        plt.title('Temperature Analysis')
        plt.ylabel('Temperature C')
        plt.xlabel('num_readings')
        plt.show()

        plt.plot(range(self.num_readings), self.max_humid_list, 'b-', label='Max Hum')
        plt.plot(range(self.num_readings), self.min_humid_list, 'r-', label='Min Hum')
        plt.plot(range(self.num_readings), self.curr_humid_list, 'y-', label='Last Hum')
        plt.plot(range(self.num_readings), self.avg_humid_list, 'g-', label='Avg Hum')
        plt.legend(loc='best')
        plt.title('Humidity Analysis')
        plt.ylabel('Humidity %')
        plt.xlabel('Number of readings')
        plt.show()

    # Unit conversion
    def cel_to_fah(self):
        self.mult_factor = 1.8
        self.add_factor = 32.0
        self.unit = " F\n"


    def fah_to_cel(self):
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.unit = " C\n"

    async def coapPUT(self, data):
        context = await Context.create_client_context()

        await asyncio.sleep(2)

        request = Message(code=PUT, payload=bytes(data, 'utf-8'))

        request.opt.uri_host = '10.0.0.224'
        request.opt.uri_path = ("other", "block")

        response = await context.request(request).response

        print('Result: %s\n%r'%(response.code, response.payload))

    def CoAPhandler(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.coapPUT(self.final_mesg))
        return 0


    def websocket_client(self):
        ws.send(self.final_mesg)
        result =  ws.recv()
        print("\nWebSocket Data:\n")
        print(result)



def mqtt_server():
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(down_topic)

def on_message(client, userdata, msg):
    print(str(msg.payload))
    msg_event.set()




if __name__ == "__main__":
    msg_event = threading.Event()
    up_topic = 'mqtt_upstream'
    down_topic = 'mqtt_downstream'
    client = mqtt.Client()
    client.connect("10.0.0.224",1883,60)

    ws = create_connection("ws://10.0.0.224:8888/ws")

    threads = []
    mqtt_thread = threading.Thread(target=mqtt_server)
    threads.append(mqtt_thread)
    mqtt_thread.daemon = True
    mqtt_thread.start()


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
