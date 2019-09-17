from machine import Pin
from neopixel import NeoPixel

pin = Pin(15, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
for i in range(8):
np[i] = (255, 255, 255) 
np.write()
import time

time.sleep(1)           # sleep for 1 second
time.sleep_ms(500)      # sleep for 500 milliseconds
time.sleep_us(10)       # sleep for 10 microseconds

def fita(r,g,b):
for i in range(8):
np[i] = (r,g,b)
np.write()

def yellow():
for i in range(255):
fita(i,i,0)
time.sleep_ms(100)


def yellow():
for i in range(255):
fita(i,i,0)
print(i)
time.sleep_ms(100)


def fitan(r,g,b,n):
for i in range(n):
np[i] = (r,g,b)
np.write()


np = NeoPixel(pin, 300)  

#fire
palette = [(0, 0, 0), (128, 0, 0), (255, 0, 0),  (139, 0, 0), (255, 165, 0), (255, 140, 0), (255, 215, 0),(255, 255, 0)]
for i in range(8):
np[i] = palette[i]

import random

for j in range(100):
for i in range(8):
np[i] = palette[random.randrange(8)]
np.write()
time.sleep_ms(30)


np = NeoPixel(pin, 60) 
for j in range(100):
for i in range(60):
np[i] = palette[random.randrange(8)]
np.write()


