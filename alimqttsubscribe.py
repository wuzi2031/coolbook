import paho.mqtt.client as mqtt

user = "user0001"
pwd = "user0001password"
mqtt_svr = "mqtt-test.cn-qingdao.aliyuncs.com"
port = 1883  # endpoint端口
topic = "testtopic"  # 订阅的主题内容


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic, qos=0)


def on_message(client, userdata, msg):
    print("topic:" + msg.topic + " Message:" + str(msg.payload))


client = mqtt.Client(
    client_id="CID_test0001",
    clean_session=True,
    userdata=None,
    protocol='MQTTv31'
)

client.username_pw_set(user, pwd)
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_svr, port, 60)
client.loop_forever()