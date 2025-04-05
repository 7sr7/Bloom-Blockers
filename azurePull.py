"""
for testing how to read data from azure iot to python....
"""

from azure.iot.device import IoTHubDeviceClient, Message # pip install azure-iot-device
import random
import time
import json
import math

from datetime import datetime
from azure.eventhub import EventHubConsumerClient # pip install azure.eventhub
from azurePush import getCurrentTime

# from "Insertion endpoint" --> "Event Hub interchangeable endpoint" 
    # (or should be a tab that translates roughly to this... my azure hub is in jp so im doing my best to translate to what i think it would be in en...)

#「組み込みのエンドポイント」から --> 「イベントハブ互換エンドポイント」
CONNECTION_STR = "Endpoint=sb://iothub-ns-bloomblock-64710761-f3cd7291df.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=ybZ2iX4zPlE2pjtXKReWlLV4fycc/L+CWAIoTLXWQzg=;EntityPath=bloomblockershub"




# from "Shared access policy" --> "Consumer group"
    # (or should be a tab that translates roughly to this... my azure hub is in jp so im doing my best to translate to what i think it would be in en...)

#「共有アクセスポリシー」から 「コンシューマー グループ」 
EVENTHUB_NAME = "bloomblockershub"


global messageReceived
messageReceived = False


global file 

# clear the file...
file = open("azureData.txt","w")
file.write("")

if True:
    file.write("Phosphate" + ' ' * 7 + '|' + ' ' * 16 + "Time\n")
    file.write("Measurements" + ' ' * 4 + '|' + ' ' * 15 + "Taken\n") 
    file.write('-' * 16 + '|' + '-' * 20 + "\n")

else:
    file.write("Phosphate Measurements |             Time Taken\n")
    file.write("-----------------------------------------------\n")

file.close()

if False:
    exit(1)

year, month, day, hr, min, sec = getCurrentTime()

if False:
    file.write(f'The following is all the unread Azure IoT cloud data as of {str(year).rjust(2,"0")}/{str(month).rjust(2,"0")}/{str(day).rjust(2,"0")} @ {str(hr).rjust(2, "0")}:{str(min).rjust(2, "0")}:{str(sec).rjust(2, "0")}...\n')


if False:
    file.write("assasdfasd\n")
    exit(1)


def getNumDigits(targetNum):
    ret = 0
    while (int(targetNum) > 0):
        ret += 1
        targetNum //= 10

    return ret

def on_event(partition_context, event):

    if False:
        print(f"Received message: {event.body_as_str()}")
        partition_context.update_checkpoint()

    else:
        if event and event.body:

            if True:
                print("Message received from Azure IoT Hub...")

            # Print raw message as string
            if True:
                print("Message body:", event.body_as_str())

            msgBody = event.body_as_str()    

            try: 
                msgBody = json.loads(msgBody)
                phosphateData = msgBody.get("phosphateData")
                timestamp = msgBody.get("timestamp")

                phosphateData = float(phosphateData)

                phosphateData = math.ceil(phosphateData * 1000) / 1000

                file = open("azureData.txt","a")

                year, month, day, hr, min, sec = timestamp


                if (float(phosphateData) <= 0 or float(phosphateData) >= 1000000000):
                    phosphateString = ' ' * 6
                    phosphateString += "NaN"
                    phosphateString += ' ' * 7
                    phosphateString += '| '

                else:
                    numDigits = getNumDigits(float(phosphateData))
                    phosphateString = ' ' * (6 - numDigits // 2)
                    phosphateString += f'{phosphateData:.3f}'
                    phosphateString += ' ' * (6 - numDigits // 2 - numDigits % 2 - (numDigits == 0))
                    phosphateString += '| '

                file.write(phosphateString)
                file.write(f'{str(year).rjust(2,"0")}/{str(month).rjust(2,"0")}/{str(day).rjust(2,"0")} {str(hr).rjust(2, "0")}:{str(min).rjust(2, "0")}:{str(sec).rjust(2, "0")}\n')

                file.close()

            except Exception as e:
                pass


            
            
            
            
            # file.write()

            # file.write("\n\n")

            messageReceived = True


            if False:
                # Optional: Print any system properties (like timestamps, device ID)
                print("Enqueued time:", event.enqueued_time)
                print("System properties:", event.system_properties)
                print("Application properties:", event.properties)

            # Mark this message as read
            partition_context.update_checkpoint()

        # elif not event:
        #     print("No event...")
        #     exit(1)



# Create the consumer client
client = EventHubConsumerClient.from_connection_string(
    conn_str=CONNECTION_STR,
    consumer_group="bloomblockershub",
    eventhub_name=EVENTHUB_NAME,
)






def timeout_receive():

    iniTime = time.time()

    with client:
        client.receive(
            on_event=on_event,
            starting_position="@latest", 

            # starting_position="-1", // this means that you read from the beginning of the cloud storage (anything from last 7 days i think) 
            max_wait_time=3  # Wait up to 10 seconds for a message

        )

    elapsedTime = time.time() - iniTime

    if not messageReceived:
        print("no message received...")
        exit(1)
    else:
        print("a")

    messageReceived = False

timeout_receive()

if False:
    # Start receiving
    print("Listening for incoming messages from Azure IoT Hub...")
    with client:
        client.receive(
            on_event=on_event,
            starting_position="-1",  # "-1" = read from beginning
        )
if False:
    print("Reading all messages from today...")
    with client:
        client.receive(
            on_event=on_event,
            starting_position="-1"  # "-1" = from the beginning of the stream
        )