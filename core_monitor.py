from mqttWrapper.mqttWrapper import MqttWrapper as mqtt
import conf

monitor_one = mqtt(client_id='monitor_one', host=conf.host, port=conf.port)

monitor_one.subscribe("monitors/monitor_one")
monitor_one.loop_forever()
