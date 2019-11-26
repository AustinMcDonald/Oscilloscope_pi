import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()
adc = Adafruit_ADS1x15.ADS1015()

GAIN = 2/3
val = [ ]
cnt = 0
# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN,data_rate=3300)
#adc.start_adc(0, gain=GAIN,data_rate=128)
print('Reading ADS1x15 channel 0')

while (True):
    # Read the last ADC conversion value and print it out.
    t0 = time.time()
    value = adc.get_last_result()
    t1 = time.time()
    print('Channel 0: {0}'.format(value))
    print((t1-t0)*1e3)
    # Sleep for half a second.
    #time.sleep(0.5)
