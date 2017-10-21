import matplotlib.pyplot as mplot
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import datetime
import numpy
import csv

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes.
'''

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')

    def on_message(self, message):
        print ('message received:  %s' % message)
        # Reverse Message and send it back
        print ('sending back message: %s' % message)
        self.write_message(message + '-' + str(data_query(message)))

    def on_close(self):
        print ('connection closed')

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

def data_query(message):
    csv_file = open('th_data.csv', 'r')
    lastline = csv_file.readlines()[-1]
    temp = lastline.split(",")
    if (message == 'current_hum'):
        return temp[0] + '-' + temp[8]
    elif (message == 'current_temp'):
        return temp[1] + '-' + temp[8]
    elif (message == 'avg_hum'):
        return temp[2] + '-' + temp[8]
    elif (message == 'avg_temp'):
        return temp[3] + '-' + temp[8]
    elif (message == 'max_hum'):
        return temp[4] + '-' + temp[8]
    elif (message == 'max_temp'):
        return temp[5] + '-' + temp[8]
    elif (message == 'min_hum'):
        return temp[6] + '-' + temp[8]
    elif (message == 'min_temp'):
        return temp[7] + '-' + temp[8]
    else:
        return 'Invalid input'

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
