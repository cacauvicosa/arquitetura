# Create Led Strip in 14, white 8 leds.... 
from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
np = NeoPixel(pin, 32)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (0, 15, 15) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
for i in range(32):
	np[i] = (r,g,b) 
np.write()

