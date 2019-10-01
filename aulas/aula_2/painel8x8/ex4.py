from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(14, Pin.OUT)   # output to drive NeoPixels
np = NeoPixel(pin, 64)   # create NeoPixel driver on GPIO0 for 8 pixels

def blink_pixel(r,g,b,p):
	global np
	np[p] = (r,g,b)
	np.write()
        time.sleep_ms(20)
	np[p] = (0,0,0)
	np.write()
	

def blink(r,g,b):
	global np
	for i in range(63):
		blink_pixel(r,g,b,i)

