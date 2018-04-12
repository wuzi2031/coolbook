import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.username_pw_set("rensanning", "123456")
client.on_connect = on_connect
client.on_message = on_message
client.connect("47.106.145.133", 1883)

while client.loop() == 0:
    msg = "from Publisher " + time.ctime()
    client.publish("test/rensanning/time", msg, 0, True)
    print("message published")
    time.sleep(1.5)