# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(0, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
np = NeoPixel(pin, 144)   # create NeoPixel driver on GPIO0 for 300 pixels

p = [ [1,1,1],
      [1,0,1],
      [1,1,0],	
      [1,0,0],
      [1,0,0] ]

y = [ [1,0,0,1],
      [1,0,0,1],
      [0,1,1,1],	
      [0,0,0,1],
      [0,1,1,0] ]
t = [ [1,1,1],
      [0,1,0],
      [0,1,0],
      [0,1,0],
      [0,1,0] ]


h = [ [1,0,1],
      [1,0,1],
      [1,1,1],	
      [1,0,1],
      [1,0,1] ]

o = [ [1,1,1],
      [1,0,1],
      [1,0,1],	
      [1,0,1],
      [1,1,1] ]

n = [ [1,0,0,1],
      [1,1,0,1],
      [1,0,1,1],	
      [1,0,0,1],
      [1,0,0,1] ]



def table(i,j):
	if i%2==0:
		return 12*i+j
	else:
		return 12*i+11-j

def draw(r,g,b,char,i,j):
	global np
	sl = 0
	for Line in char:
		sc = 0
		for Col in Line: 
			if Col==1:
				np[table(i+sl,j+sc)] = (r,g,b)
			sc +=1
		sl+=1

l = [4,8,10,12,14,16,20,30,40,60,80,100,140,180,220,255]
for j in l:
	for i in range(24):
		np[i] = (j,j,0)
	for i in range(24):
		np[i+24] = (j,0,0)
	for i in range(24):
		np[i+48] = (j,0,j)
	for i in range(24):
		np[i+72] = (0,j,j)
	np.write()
l.reverse()
for j in l:
	for i in range(24):
		np[i] = (j,j,0)
	for i in range(24):
		np[i+24] = (j,0,0)
	for i in range(24):
		np[i+48] = (j,0,j)
	for i in range(24):
		np[i+72] = (0,j,j)
	np.write()

draw(0,200,0,p,0,0)
draw(0,0,200,y,0,4)
draw(200,0,0,t,0,9)
draw(200,200,0,h,6,0)
draw(0,200,200,o,6,4)
draw(200,0,200,n,6,8)

np.write()

time.sleep(10)

import urandom
for i in range(300):
	n = urandom.getrandbits(8)
	r = urandom.getrandbits(7)
	g = urandom.getrandbits(7)
	b = urandom.getrandbits(7)
	np[n%144] = (r,g,b)
	np[(n+1)%144] = (r,g,b)
	np[(n+12)%144] = (r,g,b)
	np[(n-12)%144] = (r,g,b)
	time.sleep_ms(30)
	np.write()

for i in range(144):
	np[i] =(0,0,0)
	np.write()

	
