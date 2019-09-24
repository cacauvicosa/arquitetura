from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(14, Pin.OUT)   # output to drive NeoPixels
np = NeoPixel(pin, 64)   # create NeoPixel driver on GPIO0 for 8 pixels


def help():
   print ("name ")
   print ("scan (default pin 14), cyan color, 8x8")
   print ("fromXtoY(r,g,b,x,y) line from x->y, color rgb")
   print ("blink - scan 0-63 color 0,23,23 - 20ms")
   print ("blink pixel p in rgb blink_pixel(r,g,b,p)")

def name():
   print ("MicroPython-4fba3d")
   print ("Painel 8x8 Led WS2812 pino 14 Esp8266")
   
def scan():
	global np
	np[0] = (0, 255, 255) # set the first pixel to white
	np.write()              # write data to all pixels
	r, g, b = np[0]         # get first pixel colour
	for i in range(63):
		np[i] = (0,0,0)
		np[i+1] = (r,g,b) 
		np.write()
		time.sleep_ms(10)
	
	np[63] = (0,0,0)
	np.write()

def fromXtoY(r,g,b,x,y):
	global np
	for i in range(y-x):
		if ( i + x < 64 ):
			np[i] = (r,g,b)
	np.write()


def blink_pixel(r,g,b,p):
	global np
	np[p] = (r,g,b)
	np.write()
        time.sleep_ms(20)
	np[p] = (0,0,0)
	np.write()
	

def blink():
	for i in range(63):
		blink_pixel(0,23,23,i)
	

def zigzag(t):
	for i in range(t):
		for i in range(63):
			blink_pixel(50,50,0,i)
		for i in range(64):
			blink_pixel(50,50,0,63-i)

