# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time

	
def fade():
	pin = Pin(0, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
	np = NeoPixel(pin, 144)   # create NeoPixel driver on GPIO0 for 300 pixels
	l = [4,8,10,12,14,16,20,30,40,60,80,100,140,180,220,255]
	for j in l:
		for i in range(144):
			np[i] = (j,j,0)
			np.write()
	l.reverse()
	for j in l:
		for i in range(144):
			np[i] = (j,j,0)
		np.write()




