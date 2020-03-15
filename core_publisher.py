from mqttWrapper.mqttWrapper import MqttWrapper as mqtt
import conf

publisher = mqtt(client_id=conf.publisher_id, host=conf.host, port=conf.port)

while True:
    if message := input('Enter message\n'):
        publisher.publish('monitors/monitor_one', message)
