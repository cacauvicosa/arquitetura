 # Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time
import random
	
CNT = 30 # leds
pin = Pin(0, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
fita = NeoPixel(pin, CNT)   # create NeoPixel driver on GPIO0 for 300 pixels


fire_color  = ( 80,  35,  00)
off_color    =  (  0,  0,  0)


def Draw(fita,CNT,fire_color,off_color):
        L = [23,56,12,89,20,78,30,2,35,50,23,76,2,9,60,18,30,2,35,50,23,46,72,89,60,38,80,20,5,52]
	Clear(fita,CNT)
	for i in range(CNT):
  		AddColor(fita,i, fire_color)
		r = L[i]
  		diff_color = ( r, r/2, r/2)
  		SubstractColor(fita,i, diff_color)
	fita.write()

def AddColor(fita, position, color):
	fita[position] = Blend(fita[position], color)

def SubstractColor(fita, position, color):
	fita[position] = Substract(fita[position], color)

def Blend(color1, color2):
	r1 = color1[0]
	g1 = color1[1]
	b1 = color1[2]
	r2 = color2[0]
	g2 = color2[1]
	b2 = color2[2]
	if (r1+r2>255):
		r1 = 255
	else: 
		r1=r1+r2
	if (g1+g2>255):
		g1 = 255
	else: 
		g1=g1+g2
	if (b1+b2>255):
		b1 = 255
	else: 
		b1=b1+b2

	return (r1,g1,b1)

def Substract(color1, color2):
	r1 = color1[0]
	g1 = color1[1]
	b1 = color1[2]
	r2 = color2[0]
	g2 = color2[1]
	b2 = color2[2]
	r=r1-r2
	g=g1-g2
	b=b1-b2
	if(r<0):
		 r=0
	if(g<0):
		 g=0
	if(b<0):
		 b=0
	return (r, g, b)

def Clear(fita,CNT):
	for i in range(CNT):
		fita[i] = (0,0,0)	
	fita.write()


for i in range(10):
	Draw(fita,CNT,fire_color,off_color)
	time.sleep_ms(70)

