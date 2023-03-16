#Mobile app (MyMQTT)to Respberrypi
#mobile publisher pi subscriber                                                                                                                                   import paho.mqtt.client as mqttclient
import time
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("client is connected")
        global connected
        connected = True
    else:
            print("client is not connected")
def on_message(client, userdata, message):
    Messagereceived=True
    print("Message received" ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    
Messagereceived = False         
connected = False
broker_address = "192.168.43.165"
port = 1883
#user = "     "
#password = "      "
client = mqttclient.Client("MQTT")
#client.username_pw_set(user, password=password)
client.on_message=on_message
client.connect(broker_address, port=port)
client.on_connect = on_connect
client.subscribe("mqtt/secondcode")
client.loop_start()
while connected!=True:
    time.sleep(0.1)
while Messagereceived!=True:
    time.sleep(0.1)
    
client.loop_stop()