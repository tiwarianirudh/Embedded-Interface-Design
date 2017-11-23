/******************************************
# Project- 3
# AWS with Graphical Client
# Date: November 20, 2017
#Authors: Anirudh Tiwari || Mukund M Atre
******************************************/



// Initialize Sqs instance and necessary variables
var AWS = require('aws-sdk');
AWS.config.update({region: 'REGION'});
var sqs = new AWS.SQS();
var avg_temp = 0.00;
var avg_humid = 0.00;
var sum_temp = 0.00;
var sum_humid = 0.00;
var max_temp = 0.00;
var max_humid = 0.00;
var min_temp = 100.00;
var min_humid = 100.00;
var count = 1.0;

//  Handler that is called every time an event is detected
exports.handler = (event, context, callback) => {
    var eventText = JSON.stringify(event, null, 2);
    console.log("Received event:", eventText);
    // Taking values received from the IoT topic
    var curr_temp = parseFloat(event.Temperature);
    var curr_humid = parseFloat(event.Humidity);
    // Computing min, max and average
    max_temp = Math.max(max_temp, curr_temp);
    max_humid = Math.max(max_humid, curr_humid);
    min_temp = Math.min(min_temp, curr_temp);
    min_humid = Math.min(min_humid, curr_humid);
    sum_temp += curr_temp;
    sum_humid += curr_humid;
    avg_temp = (sum_temp/count);
    avg_humid = (sum_humid/count);
    avg_temp = avg_temp.toFixed(2);
    avg_humid = avg_humid.toFixed(2);
    max_temp = max_temp.toFixed(2);
    max_humid = max_humid.toFixed(2);
    min_temp = min_temp.toFixed(2);
    min_humid = min_humid.toFixed(2);

    // Message to be put on SQS queue in JSON format
    var params = {
     DelaySeconds: 0,
     MessageBody: "{ \"curr_temp\": " + curr_temp +", " + " \"avg_temp\": " + avg_temp + "," + "\"max_temp\": " + max_temp + "," + "\"min_temp\": " + min_temp + "," +"\"curr_humid\": " + curr_humid + "," + "\"avg_humid\": " + avg_humid + "," + "\"max_humid\": " + max_humid + "," + "\"min_humid\": " + min_humid + "}",
     QueueUrl: "https://sqs.us-east-2.amazonaws.com/354307652430/weather_queue"
    };

    // Sending message to SQS queue every time an event is generated
    sqs.sendMessage(params, function(err,data){
    if(err) {
      console.log('error:',"Fail Send Message" + err);
    }else{
      console.log('data:',data.MessageId);
    }
});
    //  Logging values that can be viewed in Cloudwatch
    console.log(max_temp, min_temp, max_humid, min_humid, avg_temp, avg_humid, count);
    count++;
    callback(null, curr_humid);
};
