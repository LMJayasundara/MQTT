import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPERATURE")

# while True:
client.on_message = on_message
time.sleep(30)
# client.loop_end()
client.loop_forever()

# # Import package
# import paho.mqtt.client as mqtt

# # Define Variables
# MQTT_HOST = "mqtt.eclipseprojects.io"
# MQTT_PORT = 1883
# MQTT_KEEPALIVE_INTERVAL = 45
# MQTT_TOPIC = "helloTopic"
# MQTT_MSG = "hello MQTT"

# # Define on connect event function
# # We shall subscribe to our Topic in this function
# def on_connect(mosq, obj, rc):
#     mqttc.subscribe(MQTT_TOPIC, 0)

# # Define on_message event function. 
# # This function will be invoked every time,
# # a new message arrives for the subscribed topic 
# def on_message(mosq, obj, msg):
# 	print ("Topic: " + str(msg.topic))
# 	print ("QoS: " + str(msg.qos))
# 	print ("Payload: " + str(msg.payload))

# def on_subscribe(mosq, obj, mid, granted_qos):
#     print("Subscribed to Topic: " + 
# 	MQTT_MSG + " with QoS: " + str(granted_qos))

# # Initiate MQTT Client
# mqttc = mqtt.Client()

# # Assign event callbacks
# mqttc.on_message = on_message
# mqttc.on_connect = on_connect
# mqttc.on_subscribe = on_subscribe

# # Connect with MQTT Broker
# mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# # Continue monitoring the incoming messages for subscribed topic
# mqttc.loop_forever()