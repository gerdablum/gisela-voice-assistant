import paho.mqtt.client as mqtt 

TOPIC_SEND_RF_COMMAND = "cmnd/tasmota_bridge/rfraw"
TOPIC_RECEIVE_MUSIC_COMMAND = "topic/music_control"

class MQTTClient:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set("licht", "alina")
        self.client.connect("localhost", 1883, 60) 
        self.client.loop_start()
        self.subscribers = []

    
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe(TOPIC_RECEIVE_MUSIC_COMMAND)

    def on_message(self, client, userdata, msg):
        print(f"{msg.topic} {msg.payload}")
        if (msg.topic == TOPIC_RECEIVE_MUSIC_COMMAND):
            for subscriber in self.subscribers:
                subscriber.onMusicCommandReceived(msg.payload)

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def sendMessage(self, payload):
        self.client.publish(TOPIC_SEND_RF_COMMAND, payload)
        print("published {payload} to {TOPIC_SEND_RF_COMMAND}")


   