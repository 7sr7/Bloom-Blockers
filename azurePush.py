"""
for testing how to write data from python to azure iot....
"""

from azure.iot.device import IoTHubDeviceClient, Message # pip install azure-iot-device
import random
import time
import json
from datetime import datetime


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

    if False:    
        print(f'Current date is: {currYr.rjust(2,"0")}/{currMon.rjust(2,"0")}/{currDay.rjust(2,"0")} @ {currHr.rjust(2, "0")}:{currMin.rjust(2, "0")}:{currSec.rjust(2, "0")}')



    return dateArr


# creating Azure IoT client...
def initializeClient():
    # my connection string (primary key of registered device on Azure IoT)
    CONNECTION_STRING = "HostName=BloomBlockersHub.azure-devices.net;DeviceId=RaspberryPiPython;SharedAccessKey=fNZ1n6dxy+B46X1UqHNkKSxvjBM8w1Ct06YXgo6yusk="

    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    return client


# sending data to Azure IoT...
def send_data(client):
    # time stall... (maybe if i have multiple messages to send)
    if False:
        time.sleep(5)  


    if False:
        for i in range(5):
            message = Message(i)
            client.send_message(message)

    else:
        for i in range(5):
            # simulated data for right now...
            measuredPhosphateLevel = random.uniform(0, 10)


            # creating message in desired format...
            allData = {
                "phosphateData": measuredPhosphateLevel,
                "timestamp": getCurrentTime()
            }

            message = Message(json.dumps(allData))
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
    if True:
        # sending data...
        print("Sending data to Azure IoT Hub...")
        client = initializeClient()
        
        send_data(client)
        print("Sent data to Azure IoT Hub successfully...")
        client.shutdown()

    if False:
        print(time.time())

    if False:
        print(getCurrentTime())


if __name__ == "__main__":
    main()    

