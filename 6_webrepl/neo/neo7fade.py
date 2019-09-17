# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time


def RGBLoop():
	global np
	for j in range(3):
    		for k in range(16): 
      			if j==0:
				setAll(16*k,0,0)
			elif j==1:
				setAll(0,16*k,0)
			else:
				setAll(0,0,16*k)	
      			np.write()
			time.sleep_ms(10)
    		for k in range(16): 
      			if j==0:
				setAll(256-16*k,0,0)
			elif j==1:
				setAll(0,256-16*k,0)
			else:
				setAll(0,0,256-16*k)	
	      		np.write()
			time.sleep_ms(10)

def setAll(r,g,b):
	global np
	for i in range(32):
		np[i] = (r,g,b)
	

pin = Pin(14, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
np = NeoPixel(pin, 32)   # create NeoPixel driver on GPIO0 for 300 pixels
while True:
	RGBLoop()


