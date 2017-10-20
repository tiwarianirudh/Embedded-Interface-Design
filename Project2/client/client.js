// Reference: https://os.mbed.com/cookbook/Websockets-Server#code
// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

$(document).ready(function () {
  $("div#message_details").hide()
    var ws;
  $("#open").click(function(evt) {
    evt.preventDefault();
    // var host = $("#host").val();
    // var port = $("#port").val();
    // var uri = $("#uri").val();

    // create websocket instance
    ws = new WebSocket("ws://10.0.0.224:8888/ws");

    $("#get_current_temp").click(function(evt){
      ws.send("currentTemp");
    });

    $("#get_current_hum").click(function(evt) {
      ws.send("currentHum");
    });

    $("#get_avg_temp").click(function(evt) {
      ws.send("avgTemp");
    });

    $("#get_avg_hum").click(function(evt) {
      ws.send("avgHum");
    });

    $("#get_min_temp").click(function(evt) {
      ws.send("minTemp");
    });

    $("#get_min_hum").click(function(evt) {
      ws.send("minHum");
    });

    $("#get_max_temp").click(function(evt) {
      ws.send("maxTemp");
    });

    $("#get_max_hum").click(function(evt) {
      ws.send("maxHum");
    });

    ws.onmessage = function(evt) {
      var buffer = evt.data.split("-")

      if()
    };
)};
