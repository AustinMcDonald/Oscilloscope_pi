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

def makeFig():
    plt.ylim(-100,1500)
    #plt.xlim(min(times),max(times))
    #plt.xlim(-200,200)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.xlabel('Time [ms]')
    plt.plot(times,vals, 'ro-', label='Channel 0')
    #plt.plot(tim,val,'ro-',label='channel0')
    plt.legend(loc='upper right')
    
GAIN = 2/3

cnt = 0
bufferlen = 300
half_buffer = bufferlen/2
val = np.zeros(bufferlen)
tim = np.zeros(bufferlen)

def Trigger(vals, threshold):
	Triggered = False
	Tloc = np.where(val>threshold)
	if len(Tloc[0])>2:
	    Condition1 = 20<Tloc[0][0]<bufferlen-20
	    LOC = Tloc[0][0]
	else:
	    Condition1 = False
	    LOC = 0
	
	ConditionCheck = [Condition1 == True]
	if all(ConditionCheck):
	    Triggered = True
	    
	return Triggered, LOC

# Start continuous ADC conversions on channel 0 using the previous gain value.
#adc.start_adc(0, gain=GAIN,data_rate=3300)
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')

while (True):
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    val[cnt] = value
    tim[cnt] = time.time()
    #print('Channel 0: {0}'.format(value))
	
    cnt = cnt+1
    if(cnt == bufferlen):
	cnt=0
	Triggered,TriggerLoc = Trigger(val, 500)
	times = (tim - tim[TriggerLoc])*1e3
	vals  = val
	if Triggered == True:
	    drawnow(makeFig)
	
	    
    time.sleep(0.0001)
