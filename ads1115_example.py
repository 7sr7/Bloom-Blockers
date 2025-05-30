import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import smbus2

print('board.SCL: ', board.SCL)
print('board.SDA: ', board.SDA)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

print('I2C devices found:', [hex(i) for i in i2c.scan()])

bus = smbus2.SMBus(1)

print(bus)

if False:
    exit(1)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

if True:
    exit(1)


# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

print("{:>5}\t{:>5}".format("raw", "v"))

try:
    while True:
        print("cahn0: {:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
        print("cahn1: {:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
        print("cahn2: {:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
        print("cahn3: {:>5}\t{:>5.3f}".format(chan3.value, chan3.voltage))
        print("")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass


