# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time

def blink_pixel(r,g,b,p):
	np[p] = (r,g,b)
	np.write()
	np[p] = (0,0,0)
	np.write()
	

pin = Pin(14, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
np = NeoPixel(pin, 64)   # create NeoPixel driver on GPIO0 for 300 pixels
while True:
	for i in range(31):
		np[2*i] = (50,50,0)
		np[63-2*i]= (0,50,50)
		np.write()		
		np[2*i] = (0,0,0)
		np[63-2*i]= (0,0,0)
		np.write()		
	for i in range(31):
		np[63-2*i] = (50,50,0)
		np[2*i]= (0,50,50)
		np.write()		
		np[2*i] = (0,0,0)
		np[63-2*i]= (0,0,0)
		np.write()		





