const mqtt = require("mqtt");
const mqttclient = mqtt.connect('mqtt://35.176.164.225:1883/', {username: "admin", password: "admin@123"});

const topic = 'test';

try {
  mqttclient.on('connect', function () { // When connected
    console.log('Client connected');
    //subscribe to a topic
    mqttclient.subscribe([topic], function () {
      mqttclient.on('message', function (topic, message, packet) {
        console.log(message.toString());
        console.log(topic.toString());
      });
    });
  });
} catch (err) {
  console.log(err);
}