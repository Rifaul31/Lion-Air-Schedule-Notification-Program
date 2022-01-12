# Import libraries
import paho.mqtt.client as mqtt
import os
import datetime
import json

# -------------------- MQTT Setup --------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" ----- Client Connected ----- ")
    else:
        print("Error connect code : " + str(rc))

# The callback for when a PUBLISH message is received from the server.

# When receiving message payload from the publisher, the message will be decoded
# from json type string into it's original type (in this case, it's a dictionary)

# Schedule that is received will be shown on the terminal and the data will be saved
# into a text file, any time format will be saved in boarding.txt and any transit
# location will be saved in lokasi.txt
def on_message(client, userdata, msg):
    jsonData = msg.payload.decode("utf-8") 
    sched = json.loads(jsonData) # Decode data from JSON type string
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