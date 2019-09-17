# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time
PIN_P1 = Pin(4,Pin.IN,Pin.PULL_UP) # d2 botao para acelerar o carro 1

Color = [1,2,3,6, 10,15,20,25, 30,35,40,60, 80,100,120,140]

def RGBLoop():
	global np,PIN_P1,Color
    	for k in range(16): 
      		setAll(Color[k],0,0)
      		np.write()
		if PIN_P1.value() == 0:
			return
    	for k in range(16): 
		setAll(Color[15-k],0,0)	
	      	np.write()
		if PIN_P1.value() == 0:
			return

def setAll(r,g,b):
	global np
	for i in range(64):
		np[i] = (r,g,b)
	

pin = Pin(14, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
np = NeoPixel(pin, 64)   # create NeoPixel driver on GPIO0 for 300 pixels
while True:
	RGBLoop()


