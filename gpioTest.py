from gpiozero import LED, DigitalOutputDevice
import time


if False:
    # Use GPIO pin 17 (Pin 11 on the board)
    led = LED(17)

    print("Blinking LED on GPIO 17...")

    while True:
        led.on()
        print("LED ON")
        sleep(1)
        led.off()
        print("LED OFF")
        sleep(1)

pin = DigitalOutputDevice(27)  # GPIO 27 (pin 13)


while True:

    if False:
        pin.on()   # Set HIGH
        sleep(2)

        pin.off()  # Set LOW
    else:
        pin.toggle()
        time.sleep(2)





if False:
    motorPin = 9

    def setup():
        pinMode(motorPin, OUTPUT)
        digitalWrite(motorPin, LOW)   # Ensure MOSFET is off at power‑up


    def loop():
        time.sleep(5)
        digitalWrite(motorPin, HIGH);  # Turn the motor ON (via MOSFET)
        time.sleep(5)

        digitalWrite(motorPin, LOW);   # Turn the motor OFF
        while (1) {}                   # Stop the program from restarting the cycle
