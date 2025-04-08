from gpiozero import LED
from time import sleep

# Use GPIO pin 17 (Pin 11 on the board)
led = LED(17)

print("🔁 Blinking LED on GPIO 17...")

while True:
    led.on()
    print("LED ON")
    sleep(1)
    led.off()
    print("LED OFF")
    sleep(1)

