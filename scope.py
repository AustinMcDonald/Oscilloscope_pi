import time
import matplotlib.pyplot as plt
#import numpy
from drawnow import *
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()
adc = Adafruit_ADS1x15.ADS1015()

GAIN = 2/3
val = [ ]
cnt = 0
plt.ion()
# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN,data_rate=3300)
print('Reading ADS1x15 channel 0')
plt.figure(figsize=(8,8))
#create the figure function
def makeFig():
    plt.ylim(-2000,2000)
    #plt.ylim(-30e3,30e3)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')
while (True):
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    # Sleep for half a second.
    #time.sleep(0.5)
    val.append(int(value))
    drawnow(makeFig)
    #plt.pause(.000001)
    cnt = cnt+1
    if(cnt>50):
        val.pop(0)
