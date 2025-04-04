"""
for testing how to write data from python to azure iot....
"""

from azure.iot.device import IoTHubDeviceClient, Message # pip install azure-iot-device
import random
import time
import json
from datetime import datetime
import math


# get current date and time...
def getCurrentTime():
    currFullTime = str(datetime.now())
    currFullTime = currFullTime.split(" ")

    if False:
        print(currFullTime)
        exit(1)    


    currDate = currFullTime[0]
    currTime = currFullTime[1]

    # usable data for year / month / day format...
    currYr = str(currDate[0:4])
    currMon = str(currDate[5:7])
    currDay = str(currDate[8:10])

    currHr = str(currTime[0:2])
    currMin = str(currTime[3:5])
    currSec = str(currTime[6:8])


    dateArr = []
    dateArr.append(int(currYr))
    dateArr.append(int(currMon))
    dateArr.append(int(currDay))
    dateArr.append(int(currHr))
    dateArr.append(int(currMin))
    dateArr.append(int(currSec))


    date = f'Current date is: {currYr.rjust(2,"0")}/{currMon.rjust(2,"0")}/{currDay.rjust(2,"0")} @ {currHr.rjust(2, "0")}:{currMin.rjust(2, "0")}:{currSec.rjust(2, "0")}'
    if False:    
        print(date)



    return date


# creating Azure IoT client...
def initializeClient():
    # my connection string (primary key of registered device on Azure IoT)
    CONNECTION_STRING = "HostName=BloomBlockersHub.azure-devices.net;DeviceId=RaspberryPiPython;SharedAccessKey=fNZ1n6dxy+B46X1UqHNkKSxvjBM8w1Ct06YXgo6yusk="

    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    return client


# sending data to Azure IoT...
def send_data(client, phosphateData, dateStr):
    # time stall... (maybe if i have multiple messages to send)
    if False:
        time.sleep(5)  


    if True:
        message = "Phosphate level is " + str(phosphateData) + ". " + dateStr + "."

        print("Sending message:", message)

        # pushing this message to Azure IoT...
        if True:
            try:
                client.send_message(message)
                print("Message sent successfully...")
            except Exception as e:
                print("ERROR:", e)
                client.shutdown()
                exit(1)



def main():
    print("Sending data to Azure IoT Hub...")
    client = initializeClient()

    phosphateData = random.uniform(0,20)

    phosphateData = math.ceil(phosphateData * 1000) / 1000
    dateStr = getCurrentTime()

    print(dateStr)

    if True:
        try:
            send_data(client, phosphateData, dateStr)
        except:
            print("Error...\n")
            client.shutdown()
            exit(1)

    print("Sent data to Azure IoT Hub successfully...\n")

    client.shutdown()

    print("Exiting program...")
        

# this alternative is for "Phosphate level is _______ and date is _________"
if __name__ == "__main__":
    for i in range(10):
        main()    

    # st = "Phosphate level is 4.745. Current date is: 2025/04/03 @ 20:30:23."

    # phosphateData = st[19:24]

    # print(a)

    # date = st[43:53]
    # time = st[56:64]
    # print(date)
    # print(time)

