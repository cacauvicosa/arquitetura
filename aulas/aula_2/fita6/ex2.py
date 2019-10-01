# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time

	

pin = Pin(14, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
fita = NeoPixel(pin, 6)   # create NeoPixel driver on GPIO0 for 300 pixels
def zigzag():
	global fita
	for i in range(5):
		fita[i] = (150,150,0)
		fita[5-i]= (0,150,150)
		fita.write()	
		time.sleep_ms(20)	
		fita[i] = (0,0,0)
		fita[5-i]= (0,0,0)
		fita.write()		
		time.sleep_ms(20)	

	for i in range(5):
		fita[5-i] = (150,150,0)
		fita[i]= (0,150,150)
		fita.write()	
		time.sleep_ms(50)	
		fita[i] = (0,0,0)
		fita[5-i]= (0,0,0)
		fita.write()		
		time.sleep_ms(50)	





