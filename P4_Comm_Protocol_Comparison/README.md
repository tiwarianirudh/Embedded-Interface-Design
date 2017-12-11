# Embedded Interface Design
### Project 4: Communication Protocols Comparison
### Author: *Anirudh Tiwari*  |  *Mukund M Atre*
### University of Colorado Boulder  

**Project Implementation**  
>a. **Features Included from Project 3**
>1. Interface DHT22 Sensor with Raspberry Pi3
>2. The server is interfaced with implementation in QT
>3. The client is interfaced with implementation in QT
>4. The server uses ADAfruit Library for interfacing the DHT22-Sensor with the RPi.
>5. AWS_IOT-Python_SDK is used to send data to the AWS in JSON format.
>6. AWS Lambda then puts the data on a SQS queue and in the Dynamo DB.
>7. The client QT fetches the required data from the SQS queue and display the most recent obtained data and its time-stamp.  
>8. The client can form the graph for the obtained 30 values(or less) for Humidity and Temperatures in 8 categories.

>b. **New Feature**
>1. The data obtained from the SQS Queue is now exchanged with the server using FOUR protocols namely:
>> Co-AP Protocol.
>> MQTT Protocol - Using a Broker at the server.
>> WebSocket Protocol.
>> Rabbit AMQP protocol - Using a queue.


**Project Features for Extra-Credits**  
>1. Rabbit AMQP protocol - Using a queue.


**Instructions to Run Project**
>1. At client, run the client.py file by the command: python3 client.py
>2. At server, run the sensing.py file by the command: sensing.py
>3. Once the client QT GUI is up, click fetch data to get the data from the SQS queue and display it in the text box.
>4. Click the plot graph button to plot graphs for the fetched data.
>5. Click the test protocols button to send the data using all four protocols.


**References:**  
> https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

> www.stackoverflow.com

> https://aws.amazon.com/documentation/lambda/?icmpid=docs_menu_internal

> https://aws.amazon.com/documentation/dynamodb/?icmpid=docs_menu_internal

> https://www.tutorialspoint.com/nodejs/

> http://aiocoap.readthedocs.io/en/latest/examples.html

> https://pypi.python.org/pypi/paho-mqtt

> https://www.rabbitmq.com/tutorials/tutorial-one-python.html
