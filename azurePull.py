"""
for testing how to read data from azure iot to python....
"""

from azure.iot.device import IoTHubDeviceClient, Message # pip install azure-iot-device
import random
import time
import json
from datetime import datetime
from azure.eventhub import EventHubConsumerClient # pip install azure.eventhub

# taken from 「組み込みのエンドポイント」 --> 「イベントハブ互換エンドポイント」
CONNECTION_STR = "Endpoint=sb://iothub-ns-bloomblock-64710761-f3cd7291df.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=ybZ2iX4zPlE2pjtXKReWlLV4fycc/L+CWAIoTLXWQzg=;EntityPath=bloomblockershub"

# taken from 「共有アクセスポリシー」 --> 「iothubowner」 --> 「プライマリ接続文字列」
EVENTHUB_NAME = "bloomblockershub"


global messageReceived
messageReceived = False

def on_event(partition_context, event):

    if False:
        print(f"Received message: {event.body_as_str()}")
        partition_context.update_checkpoint()

    else:
        if event and event.body:
            print("Message received from Azure IoT Hub...")

            # Print raw message as string
            print("Message body:", event.body_as_str())

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