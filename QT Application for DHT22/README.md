# Embedded Interface Design
### Project 1: Application for Sensor Data
### Author: *Anirudh Tiwari*
### University of Colorado Boulder  



**Project Description and Implementation**  
>1. Interface DHT22 Sensor with Raspberry Pi3
>2. The GUI is created to show values values for temperature, humidity, date and time, average values, alarm indications, progress-bar indications and graphs.
>3. The temperature and humidity values are refreshed for every "Refresh" button click.
>4. The average values until the last event of data capture are shown for humidity and temperature sensor values.
>5. A .csv file is created for storing the obtained values from the sensor.
>6. Graph for Temperature and Humidity values can be plotted until the last event of data capture by pressing the Generate Graph button.
>7. User can set optimum values for temperature and humidity to activate the visual-alarm.
>8. Visual alarm in the form of color change is implemented for the alarm-activation values entered by the user or the default values set.
>9. The alarm activations is shown by RED color, while GREEN indicates the safe-value.
>10. The alarm color is set to BLACK if no data is sensed by the sensor indicating the error.
>11. The progress bar indicates the %value for obtained humidity and temperature data on a scale of 100.
>12. The close button terminates the Sensor Data Application.





**Instructions Followed**  
>1. Raspberry Pi is flashed with Raspbian Stretch OS.  
>2. To support remote development and demonstration, VNC viewer is setup.
>3. PyQt5 library is installed on the Raspberry Pi.
>4. Pin Connections: PIN1:VCC | PIN6:GROUND | PIN7:DATA.
>5. The following command is used to generate the python code from the .ui file from GUI created in QtCreator: pyuic5 -x mainwindow.ui -o project1.py
>6. The following command is used to run the python-code: python3 project1.py





**Project Features for Extra-Credits**  
>1. Display of Average values for all values captured until the last "Refresh" event.
>2. Graph is generated for Temperature values captured over time, until the "Generate Graph" is clicked.
>3. Graph is generated for Humidity values captured over time, until the "Generate Graph" is clicked.  
>4. User sets an alarm for Temperature values being obtained.
>5. User sets an alarm for Humidity Values being obtained.
>6. Alarm Activation(Red) if the temperature value exceeds the user set value,else is Green.
>7. Alarm Activation(Red) if the humidity value exceeds the user set value, else is Green.
>8. Alarm is Black and a message is displayed if no data is acquired by the sensor or the sensor malfunctions.






**Supporting Execution-Pictures**  

![alt text](https://github.com/tiwarianirudh/eid-fall2017/blob/master/Project1/untitled/0_No_Data_Recieved.png "When No Data is Captured")    


![alt text](https://github.com/tiwarianirudh/eid-fall2017/blob/master/Project1/untitled/1_With_No_Alarm.png "With No Alarm")  


![alt text](https://github.com/tiwarianirudh/eid-fall2017/blob/master/Project1/untitled/2_With_Temp_Alarm.png "With Temperature Alarm")


![alt text](https://github.com/tiwarianirudh/eid-fall2017/blob/master/Project1/untitled/3_With_Humidity_Alarm.png "With Humidity Alarm")


![alt text](https://github.com/tiwarianirudh/eid-fall2017/blob/master/Project1/untitled/Humidity.png "Humidity Graph")


![alt text](https://github.com/tiwarianirudh/eid-fall2017/blob/master/Project1/untitled/Temperature.png "With Temperature Graph")






**References:**  
..* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

..* References Mentioned in Code as required

..* https://www.raspberrypi.org/documentation/remote-access/vnc/

..* https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

..* https://cdn-learn.adafruit.com/downloads/pdf/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.pdf

