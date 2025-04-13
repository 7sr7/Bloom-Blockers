import ADS1x15

# initialize ADS1115 on I2C bus 1 with default address 0x48
ADS = ADS1x15.ADS1115(1)

# read ADC in pin 0
ADS.readADC(0)

