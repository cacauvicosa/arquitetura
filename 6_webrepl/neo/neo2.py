from machine import Pin
from neopixel import NeoPixel
import time

def fitan(r,g,b,n):
	for i in range(n):
		np[i] = (r,g,b)
	np.write()

pin = Pin(14, Pin.OUT)   # set GPIO14  in NodeMCU to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
for i in range(8):
	np[i] = (r,g,b) 
np.write()

time.sleep(1) 
fitan(255,0,0,8) # red
time.sleep(1) 
fitan(0,255,0,8) # green
time.sleep(1) 
fitan(0,0,255,8) # blue
time.sleep(1) 
fitan(255,255,0,8) # yellow
time.sleep(1) 
fitan(0,255,255,8) # cyan
time.sleep(1) 
fitan(255,0,255,8) # purple
time.sleep(1) 
fitan(0,0,0,8) # purple




