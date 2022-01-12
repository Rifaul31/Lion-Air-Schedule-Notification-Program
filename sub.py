# Import libraries
import paho.mqtt.client as mqtt
import os
import time
import datetime
import json
from threading import Thread

# -------------------- MQTT Setup --------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" ----- Client Connected ----- ")
    else:
        print("Error connect code : " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    jsonData = msg.payload.decode("utf-8")
    sched = json.loads(jsonData)
    if sched['id'] in sessCode:
        print("\n##### Received Previously Notified Schedule #####")
    else:
        print("\n>>>>> Notifikasi Baru Dari LionAIR pada Topic : " + msg.topic)
        print('-------------- Flight', sched['id'], 'Schedule --------------')
        print('Flight ID    : ', sched['id'])
        print('Origin       : ', sched['Origin'])
        print('Destination  : ', sched['Destination'])
        print('Departure    : ', sched['Departure'])
        print('Arrival      : ', sched['Arrival'])
        print('Date         : ', sched['Date'])
        sessCode.append(sched['id'])
        
        timeRecv = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open('boarding.txt', 'a') as f:
            f.write("Flight ID : " + sched['id'] + " | Departure: " + sched['Departure'] +
                    " | Arrival : " + sched['Arrival'] + " | Received at : " + timeRecv + "\n")
        
        with open('lokasi.txt', 'a') as f:
            f.write("Flight ID : " + sched['id'] + " | Origin: " + sched['Origin'] +
                    " | Destination : " + sched['Destination'] + " | Received at : " + timeRecv + "\n")
            
        print("The file boarding.txt and lokasi.txt has been updated")
    
    
# create client
client = mqtt.Client('Subscriber', clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

# connecting to broker emqx on port 1883
# client.connect('broker.emqx.io', port = 1883)
client.connect('broker.hivemq.com', port = 1883)

client.subscribe("/LionAirSchedule", 1)

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def header():
    print('------------------------- Lion Air Schedule Notification -------------------------')
def footer():
    print('----------------------------------------------------------------------------------')

# -------------------- Main Function --------------------
sessCode = []
sessTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
with open('boarding.txt', 'a') as f:
    f.write("--------------- Session start at " + sessTime + " ---------------" + "\n")

with open('lokasi.txt', 'a') as f:
    f.write("--------------- Session start at " + sessTime + " ---------------" + "\n")
clear()
header()

while client.loop() == 0:
    pass