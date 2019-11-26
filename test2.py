import time

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

GAIN = 2/3
val = [ ]
cnt = 0
# Start continuous ADC conversions on channel 0 using the previous gain value.
#adc.start_adc(0, gain=GAIN,data_rate=3300)
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')

while (True):
    # Read the last ADC conversion value and print it out.
    t0 = time.time()
    value = adc.get_last_result()
    val.append(int(value))
    t1 = time.time()
    print('Channel 0: {0}'.format(value))
    if Trigger(val,10)==True:
        print('Triggered')
    cnt = cnt+1
    if(cnt>50):
        val.pop(0)
    #print((t1-t0)*1e3)
    # Sleep for half a second.
    time.sleep(0.1)
