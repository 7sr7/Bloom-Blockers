"""
for testing how to send data from python to azure iot....
"""

from azure.iot.device import IoTHubDeviceClient, Message # pip install azure-iot-device
import random
import time

# Azure IoT Hub connection string
CONNECTION_STRING = "HostName=BloomBlockersHub.azure-devices.net;DeviceId=RaspberryPiPython;SharedAccessKey=fNZ1n6dxy+B46X1UqHNkKSxvjBM8w1Ct06YXgo6yusk="

# Create client instance
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Simulate sensor data
def send_data():
    for i in range(2):
        time.sleep(5)  # Send data every 5 seconds

        nitrate_level = random.uniform(0, 10)  # Simulated sensor data
        phosphate_level = random.uniform(0, 10)

        message = Message(f'{{"nitrate": {nitrate_level}, "phosphate": {phosphate_level}}}')
        print("Sending message:", message)

        try:
            client.send_message(message)
            print("Message sent successfully...")
        except Exception as e:
            print("Error:", e)
            client.shutdown()
            exit(1)


# Start sending data
print("Sending data to Azure IoT Hub...")
send_data()
print("Sent data to Azure IoT Hub successfully...")
client.shutdown()
