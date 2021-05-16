from flask import Flask, jsonify, render_template, request, Response
from flask_mqtt import Mqtt
from datetime import datetime
import webbrowser
import time
import json

temp = 0
hum = 0
pre = 0

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'aws_IP' # replace your AWS IP_adress
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'mqtt_username' # replace your mqtt user_name
app.config['MQTT_PASSWORD'] = 'mqtt_passwd' # replace your mqtt Passwd
app.config['MQTT_REFRESH_TIME'] = 1.0
mqtt = Mqtt(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('sensor')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):

    global temp, hum, pre

    topic = message.topic
    if topic == 'sensor':
        sensor = message.payload.decode()
        sensor_data = json.loads(sensor)

        temp = sensor_data["temp"]
        hum = sensor_data["hum"]
        pre = sensor_data["pre"]
        print(sensor_data)

# @app.route('/_stuff', methods = ['GET'])
# def stuff():
#     global temp, hum, pre
#     return jsonify( temp=temp, hum=hum, pre=pre)

# @app.route('/cool_form', methods=['GET', 'POST'])
# def cool_form():
#     return render_template('cool_form.html')

# @app.route('/')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)