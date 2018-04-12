import time
import paho.mqtt.client as mqtt
import datetime


def on_publish(msg, rc):  # 成功发布消息的操作
    if rc == 0:
        print("publish success, msg = " + msg)


def on_connect(client, userdata, flags, rc):  # 连接后的操作 0为成功
    print("Connection returned " + str(rc))


client = mqtt.Client(
    client_id="PID_test0001",
    clean_session=True,
    userdata=None,
    protocol='MQTTv311'
)

user = "user0001"
pwd = "user0001password"
mqtt_svr = "mqtt-test.cn-qingdao.aliyuncs.com"
port = 1883
topic = "testtopic"

client.username_pw_set(user, pwd)
client.connect(mqtt_svr, port, 60)
client.on_connect = on_connect
client.loop_start()
time.sleep(2)
count = 0
while count < 1:
    count = count + 1
    msg = str(datetime.datetime.now())
    rc, mid = client.publish(topic, payload=msg, qos=0)
    on_publish(msg, rc)
    time.sleep(1)