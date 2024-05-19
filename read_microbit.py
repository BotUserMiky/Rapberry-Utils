from ntpath import join
import serial
import paho.mqtt.client as mqtt

ser = serial.Serial(port = "COM3", baudrate = 115200)
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("192.168.0.100",99)
mqttc.loop_start()

print("Connected to: " + ser.portstr)

seq = []
prev = None

while True:
    for c in ser.read():
        seq.append(chr(c) if chr(c) != "\n" else "")

        if chr(c) == '\n':
            joined_seq = ''.join(str(v) for v in seq)
            if prev != joined_seq:
                prev = joined_seq
                print(joined_seq)
                send = mqttc.publish("IOT/connection", joined_seq, qos=2)
                send.wait_for_publish()
            seq = []
            break

ser.close()