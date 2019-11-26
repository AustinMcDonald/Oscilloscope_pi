#import time

def Trigger(vals, threshold):
	Triggered = False
	half_buffer = int(len(vals)/2)
	Condition1 = any(x >  threshold for x in vals)
	Condition2 = any(x >  threshold for x in vals)
	if Condition1==True and Condition2==True:
		for x in range(0,len(vals)):
			#if vals[x]>threshold and half_buffer-2<x<half_buffer+2:
			if vals[x]>threshold and x==half_buffer:
				Triggered = True
	return Triggered
				
