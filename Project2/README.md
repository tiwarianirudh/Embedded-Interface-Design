# Embedded Interface Design
### Project 2: Remote Websocket/Web Page UI
### Authors: *Anirudh Tiwari*
###        : *Mukund M Atre*
### University of Colorado Boulder  



**Project Description and Implementation**  
>1. Interface DHT22 Sensor with Raspberry Pi3
>2. The GUI is created on QT to show values values for temperature, humidity, date and time, average values, alarm indications, progress-bar indications and graphs.
>3. The temperature and humidity values are refreshed automatically after every five seconds.
>4. The average values until the last event of data capture are shown for humidity and temperature sensor values.
>5. A .csv file is created as a database for storing the obtained values from the sensor.
>6. The HTML page for the client displays all the mandatory 8 buttons for requesting the sensor data and a few additional ones as well.
>7. The server is implemented using Tornado and is used to connect the client with the sensor RPi.
>8. The webpage is styled with CSS and the interaction is done with the help of Javascript which uses JQuery library.
>9. The webpage handles error in connecting to the socket and prompts the user to retry by refreshing.
>10. This error can be tested by starting the client interaction before starting the server.



**Instructions to run the code:**  
>1. Before running the server, run sensing.py which interacts with the sensors and stores the data in the database(a csv). Command: python3 sensing.py
>2. Start the server by running the following command: python3 server.py
>3. Open the Weather Statistics webpage by clicking on the client.html.
>4. The page is then self-explanatory for its functioning.  





**Project Features for Probable Extra-Credits**  
>1. Graph Plot for Temperature data from the database at the sensor Rpi.
>2. Graph Plot for Temperature data from the database at the sensor Rpi.
>3. Additional Button to graph-plot temperature data.
>4. Additional Button to graph-plot humidity data.
>5. Additional Button for changing the temperature unit from Celsius to Fahrenheit (For already obtained and for the next new data).
>6. Additional Button for clearing the data currently being displayed on the webpage.


**References:**  
..* https://www.w3schools.com/html/default.asp
..* https://www.w3schools.com/css/default.asp
..* https://www.w3schools.com/jquery/default.asp
..* https://www.w3schools.com/js/default.asp
..* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
..* https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

..* https://cdn-learn.adafruit.com/downloads/pdf/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.pdf
