// Reference: https://os.mbed.com/cookbook/Websockets-Server#code
// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

$(document).ready(function () {
  $("div#message_details").hide()
  var ws;
  var if_farh= 0;
  var temp = 0;
  var switch_current_data;
  var switch_avg_data;
  var switch_min_data;
  var switch_max_data;
  var error;
  // $("#open").click(function(evt) {
  //   evt.preventDefault();
    // var host = $("#host").val();
    // var port = $("#port").val();
    // var uri = $("#uri").val();

    // create websocket instance
    ws = new WebSocket("ws://10.0.0.224:8888/ws");
    ws.onmessage = function(evt) {
      var buffer = evt.data.split("-")

      if(buffer[0] == "current_temp"){
        if(if_farh){
          // https://stackoverflow.com/questions/12839567/converting-string-to-number-in-javascript-jquery
          var temp = parseFloat(buffer[1])
          temp = ((temp * 9.0)/5.0)+32
          $("#out_current_temp").val(temp.toFixed(2)+ "\u00b0F");
        }
        else{
        $("#out_current_temp").val(buffer[1] + "\u00b0C");
        }
      }

      if(buffer[0] == "current_hum"){
        $("#out_current_hum").val(buffer[1] + "%");
      }
      if(buffer[0] == "avg_temp"){
        if(if_farh){
          // https://stackoverflow.com/questions/12839567/converting-string-to-number-in-javascript-jquery
          var temp = parseFloat(buffer[1])
          temp = ((temp * 9.0)/5.0)+32
          $("#out_avg_temp").val(temp.toFixed(2)+ "\u00b0F");
        }
        else{
        $("#out_avg_temp").val(buffer[1] + "\u00b0C");
        }
      }
      if(buffer[0] == "avg_hum"){
        $("#out_avg_hum").val(buffer[1] + "%");
      }

      if(buffer[0] == "min_temp"){
        if(if_farh){
          // https://stackoverflow.com/questions/12839567/converting-string-to-number-in-javascript-jquery
          var temp = parseFloat(buffer[1])
          temp = ((temp * 9.0)/5.0)+32
          $("#out_min_temp").val(temp.toFixed(2)+ "\u00b0F");
        }
        else{
        $("#out_min_temp").val(buffer[1] + "\u00b0C");
        }
      }
      if(buffer[0] == "min_hum"){
        $("#out_min_hum").val(buffer[1] + "%");
      }
      if(buffer[0] == "max_temp"){
        if(if_farh){
          // https://stackoverflow.com/questions/12839567/converting-string-to-number-in-javascript-jquery
          var temp = parseFloat(buffer[1])
          temp = ((temp * 9.0)/5.0)+32
          $("#out_max_temp").val(temp.toFixed(2)+ "\u00b0F");
        }
        else{
        $("#out_max_temp").val(buffer[1] + "\u00b0C");
        }
      }
      if(buffer[0] == "max_hum"){
        $("#out_max_hum").val(buffer[1] + "%");
      }
    };

    $("#get_current_temp").click(function(evt){
      ws.send("current_temp");
    });

    $("#get_current_hum").click(function(evt) {
      ws.send("current_hum");
    });

    $("#get_avg_temp").click(function(evt) {
      ws.send("avg_temp");
    });

    $("#get_avg_hum").click(function(evt) {
      ws.send("avg_hum");
    });

    $("#get_min_temp").click(function(evt) {
      ws.send("min_temp");
    });

    $("#get_min_hum").click(function(evt) {
      ws.send("min_hum");
    });

    $("#get_max_temp").click(function(evt) {
      ws.send("max_temp");
    });

    $("#get_max_hum").click(function(evt) {
      ws.send("max_hum");
    });

    $("#scale_switch").click(function(evt){
      var buffer1;
      //switch_current_data = $("#out_current_temp").val()

      if(if_farh){
        switch_current_data = $("#out_current_temp").val()
        var buffer1 = switch_current_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp-32)*5.0)/9.0
        // Reference:
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_current_temp").val(temp.toFixed(2)+"\u00b0C");
        }
        else{
          $("#out_current_temp").val("Error in Conversion");
        }

        switch_avg_data = $("#out_avg_temp").val()
        var buffer1 = switch_avg_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp-32)*5.0)/9.0
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_avg_temp").val(temp.toFixed(2)+"\u00b0C");
        }
        else{
          $("#out_avg_temp").val(temp);
        }

        switch_min_data = $("#out_min_temp").val()
        var buffer1 = switch_min_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp-32)*5.0)/9.0
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_min_temp").val(temp.toFixed(2)+"\u00b0C");
        }
        else{
          $("#out_min_temp").val("Error in Conversion");
        }

        switch_max_data = $("#out_max_temp").val()
        var buffer1 = switch_max_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp-32)*5.0)/9.0
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_max_temp").val(temp.toFixed(2)+"\u00b0C");
        }
        else{
          $("#out_max_temp").val("Error in Conversion");
        }
        if_farh = 0;
        $("#scale_switch").fadeOut(200).val("Switch Scale: C to F").fadeIn(200)
      }


      else{
        switch_current_data = $("#out_current_temp").val()
        var buffer1 = switch_current_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp*9.0)/5.0)+32
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_current_temp").val(temp.toFixed(2)+"\u00b0F");
        }
        else{
          $("#out_current_temp").val("Error in Conversion");
        }

        switch_avg_data = $("#out_avg_temp").val()
        var buffer1 = switch_avg_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp*9.0)/5.0)+32
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_avg_temp").val(temp.toFixed(2)+"\u00b0F");
        }
        else{
          $("#out_avg_temp").val("Error in Conversion");
        }

        switch_min_data = $("#out_min_temp").val()
        var buffer1 = switch_min_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp*9.0)/5.0)+32
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_min_temp").val(temp.toFixed(2)+"\u00b0F");
        }
        else{
          $("#out_min_temp").val("Error in Conversion");
        }

        switch_max_data = $("#out_max_temp").val()
        var buffer1 = switch_max_data.split("\u00b0")
        var temp = parseFloat(buffer1[0])
        temp = ((temp*9.0)/5.0)+32
        // https://www.w3schools.com/jsref/jsref_isnan_number.asp
        if(Number.isNaN(temp) == false){
          $("#out_max_temp").val(temp.toFixed(2)+"\u00b0F");
        }
        else{
          $("#out_max_temp").val("Error in Conversion");
        }
        if_farh = 1;
        $("#scale_switch").fadeOut(200).val("Switch Scale: F to C").fadeIn(200)
      }
    });
});
