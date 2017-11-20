# Embedded Interface Design
### Project 3: AWS with graphical client
### Author: *Anirudh Tiwari*  |  *Mukund M Atre*
### University of Colorado Boulder  



**Project Description and Implementation**  
>1. Interface DHT22 Sensor with Raspberry Pi3
>2. The server is interfaced with implementation in QT
>3. The client is interfaced with implementation in QT
>4. The server uses ADAfruit Library for interfacing the DHT22-Sensor with the RPi.
>5. AWS_IOT-Python_SDK is used to send data to the AWS in JSON format.
>6. AWS Lambda then puts the data on a SQS queue and in the Dynamo DB
>7. The client QT fetches the required data from the SQS queue and display the most recent obtained data and its time-stamp.  
>8. The client can form the graph for the obtained 30 values(or less) for Humidity and Temperatures in 8 categories.



**Project Features for Extra-Credits**  
>1. Cloudwatch for Data Monitoring
>2. Used DynamoDB to store data being received by the AWS.



**Instructions to Run Project**
>1. On client, run the client.py file by the command: python3 client.py
>2. On server, run the sensing.py file by the command: sensing.py


**References:**  
> https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
> www.stackoverflow.com
> https://aws.amazon.com/documentation/lambda/?icmpid=docs_menu_internal
> https://aws.amazon.com/documentation/dynamodb/?icmpid=docs_menu_internal
> https://www.tutorialspoint.com/nodejs/
