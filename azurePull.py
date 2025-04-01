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


# taken from 「組み込みのエンドポイント」 --> 「イベントハブ互換エンドポイント」
CONNECTION_STR = "Endpoint=sb://iothub-ns-bloomblock-64710761-f3cd7291df.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=ybZ2iX4zPlE2pjtXKReWlLV4fycc/L+CWAIoTLXWQzg=;EntityPath=bloomblockershub"

# taken from 「共有アクセスポリシー」 --> 「iothubowner」 --> 「プライマリ接続文字列」
EVENTHUB_NAME = "bloomblockershub"


global messageReceived
messageReceived = False


global file 

# clear the file...
file = open("azureData.txt","w")
file.write("")

if True:
    file.write("Phosphate       |                Time\n")
    file.write("Measurements    |               Taken\n")
    file.write("----------------|--------------------\n")

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
                print("here")
                msgBody = json.loads(msgBody)
                phosphateData = msgBody.get("phosphateData")
                timestamp = msgBody.get("timestamp")


                phosphateData = float(phosphateData)

                phosphateData = math.ceil(phosphateData * 1000) / 1000

                file = open("azureData.txt","a")

                year, month, day, hr, min, sec = timestamp
            
                file.write(f'     {phosphateData:.3f}      | ')
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
            starting_position="-1", # read from beginning

            # starting_position="@latest", 
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
    print("📡 Listening for incoming messages from Azure IoT Hub...")
    with client:
        client.receive(
            on_event=on_event,
            starting_position="-1",  # "-1" = read from beginning
        )
if False:
    print("📡 Reading all messages from today...")
    with client:
        client.receive(
            on_event=on_event,
            starting_position="-1"  # "-1" = from the beginning of the stream
        )