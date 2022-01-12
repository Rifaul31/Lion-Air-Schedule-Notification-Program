# Import Libraries
import paho.mqtt.client as mqtt
import os
import json
import flight

# -------------------- MQTT Setup --------------------
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" ----- Client Connected ----- ")
    else:
        print("Error connect code : " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create client
client = mqtt.Client('Publisher')
client.on_connect = on_connect
client.on_message = on_message

# connecting to broker emqx or broker hivemq on port 1883
# client.connect('broker.emqx.io', port = 1883)
client.connect('broker.hivemq.com', port = 1883)

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # Function for Clearing the terminal screen
def header():
    print('------------------------- Lion Air Schedule Notification -------------------------')
def footer():
    print('----------------------------------------------------------------------------------')
    
def menu():
    clear()
    header()
    print(' (1). Look at Available Schedule')
    print(' (2). Send Schedule Notification')
    print(' (3). About Us')
    print(' (0). Exit')
    footer()

def showSched():
    clear()
    header()
    print("Available Flights: ")
    flight.showAllSchedule()
    footer()
    input("\nPress Enter to continue...")

# The function to send selected schedule to the subscriber

# Schedule that has already been sent will not be able to be announced again

# The schedule will be encoded into json type string to be able to be sent through
# using mqtt
def sendMenu():
    clear()
    header()
    id = int(input("Please input schedule ID: "))
    if id in sessCode:
        clear()
        print('##### This flight schedule has already been notified #####')
        input("\nPress Enter to continue...")
        return
    sched = flight.returnSchedule(id)
    if isinstance(sched, dict):
        clear()
        header()
        print("Is this the flight schedule you want to sent?")
        flight.showSchedule(id)
        conf = input("Input (Y) or press Enter to confirm, or (N) to cancel : ")
        if conf == "N":
            return
        else: 
            sessCode.append(id)
            send_data = json.dumps(sched)
            client.publish("/LionAirSchedule", send_data, 1)
            clear()
            print('##### Schedule Notification Delivered #####')
            input("\nPress Enter to continue...")
    else:
        print(flight.returnSchedule(id))
        input("Please try again...")
        menuSwitch(2)
        return

def aboutMenu():
    clear()
    header()
    print("This Lion Air Schedule Notification Program is made by:"
          "\n\nPERNANDA ARYA BHAGASKARA S.M (1301190184)"
          "\nNAUFAL XEELA PANDITYATAMA (1301194177)"
          "\nAULIA RAHMAN ARIF WAHYUDI (1301194195)"
          "\n\nIn order to fulfill the final task assignment for Distributed and Parallel System Course")
    footer()
    input("\nPress Enter to continue...")
    
def menuSwitch(numInput):
    if numInput == 1:
        showSched()
    elif numInput == 2:
        sendMenu()
    elif numInput == 3:
        aboutMenu()
    else:
        print('\n!!!INVALID COMMAND!!!')
        input("Please try again...")
    

# -------------------- Main Function --------------------
sessCode = []
menu()
menuInput = int(input("Please choose a command : "))
while menuInput != 0:
    footer()
    menuSwitch(menuInput)
    menu()
    menuInput = int(input("Please choose a command : "))
print("\n. . . Program Exit")
