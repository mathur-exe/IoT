Rapberrypi to Mobile app (MyMQTT)                                                                                                                            import paho.mqtt.client as mqttclient
import time
def on_connect(client, usedata, flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected=True
    else:
        print("connection failed")
connected=False
broker_address="192.168.43.165"
port = 1883
#user = "                    "
#password = "
client=mqttclient.Client("MQTT")
#client.username_pw_set(user, password=password)
client.on_connect=on_connect
client.connect(broker_address, port = port)
client.loop_start()

while connected!=True:
    time.sleep(0.2)
client.publish("mqtt/firstcode", "Hello MQTT")
client.loop_stop()