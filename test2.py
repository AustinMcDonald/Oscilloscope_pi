import time
import numpy as np
import matplotlib.pyplot as plt
#import numpy
from drawnow import *
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()
adc = Adafruit_ADS1x15.ADS1015()


def Trigger(vals, threshold):
	Triggered = False
	half_buffer = len(vals)/2
	Condition1 = any(x >  threshold for x in vals)
	Condition2 = any(x >  threshold for x in vals)
	if Condition1==True and Condition2==True:
		for x in range(0,len(vals)):
			if vals[x]>threshold and half_buffer-2<x<half_buffer+2:
				Triggered = True
	return Triggered

def makeFig():
    plt.ylim(-1500,1500)
    #plt.ylim(-30e3,30e3)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')
    plt.axvline(cnt)
    
GAIN = 2/3
val = [ ]
cnt = 0
bufferlen = 100
half_buffer = bufferlen/2
val = np.zeros(bufferlen)
trg = np.zeros(bufferlen, dtype=bool)
# Start continuous ADC conversions on channel 0 using the previous gain value.
#adc.start_adc(0, gain=GAIN,data_rate=3300)
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')

while (True):
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    val[cnt] = value
    if value>500:
	trg[cnt] = True
    else:
	trg[cnt] = False
	
    print('Channel 0: {0}'.format(value))
    
    testcon = any(x <  500 for x in val[0:half_buffer])
    testcon2= val[cnt-1]<val[cnt]
    
    #if value>500 and half_buffer==cnt and testcon==True and testcon2==True:
    if value>500 and testcon==True and testcon2==True:
        print('Triggered')
	print(val)
	drawnow(makeFig)
	
    cnt = cnt+1
    if(cnt == bufferlen):
        #val.pop(0)
	cnt=0
    #print((t1-t0)*1e3)
    # Sleep for half a second.
    time.sleep(0.01)
