const mqtt = require("mqtt");
const mqttclient = mqtt.connect('mqtt://35.176.164.225:1883/', {username: "admin", password: "admin@123"});

var topic = "test";
var msg = "Hello";

mqttclient.on('connect', ()=>{
    setInterval(() => {
        mqttclient.publish(topic, msg);
        console.log('Message sent', msg);
    }, 1000);
})