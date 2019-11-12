# Create Led Strip in D3,300 leds....yellow dot 0 to 299...
from machine import Pin
from neopixel import NeoPixel
import time

	

pin = Pin(0, Pin.OUT)   # set GPIO0 or D3 in NodeMCU to output to drive NeoPixels
fita = NeoPixel(pin, 300)   # create NeoPixel driver on GPIO0 for 300 pixels

def setor(fita,inicio,fim,r,g,b):
	for i in range(fim-inicio):
		fita[i+inicio] = (r,g,b)
	fita.write()

def fadesetor(fita,inicio,fim,r,g,b,t):  
  stepr = r/255
  stepg = g/255
  stepb = b/255
  
  for j in range(255):
        r = int(j*stepr)
        g = int(j*stepg)
        b = int(j*stepb)
	setor(fita,inicio,fim,r,g,b)
	time.sleep_ms(t)
  for j in range(255,0,-1):
        r = int(j*stepr)
        g = int(j*stepg)
        b = int(j*stepb)
	setor(fita,inicio,fim,r,g,b)
	time.sleep_ms(t)

def repita(fita,inicio,fim,r,g,b,t,v):
   for i in range(v):
	fadesetor(fita,inicio,fim,r,g,b,t)


def fadesetorfast(fita,inicio,fim,r,g,b,t):  
  stepr = r/255
  stepg = g/255
  stepb = b/255
  
  for j in range(0,255,5):
        r = int(j*stepr)
        g = int(j*stepg)
        b = int(j*stepb)
	setor(fita,inicio,fim,r,g,b)
	time.sleep_ms(t)
  for j in range(255,0,-5):
        r = int(j*stepr)
        g = int(j*stepg)
        b = int(j*stepb)
	setor(fita,inicio,fim,r,g,b)
	time.sleep_ms(t)

def fadesetorstep(fita,inicio,fim,r,g,b,step):  
  stepr = r/255
  stepg = g/255
  stepb = b/255
  
  for j in range(0,255,step):
        r = int(j*stepr)
        g = int(j*stepg)
        b = int(j*stepb)
	setor(fita,inicio,fim,r,g,b)
  for j in range(255,0,-step):
        r = int(j*stepr)
        g = int(j*stepg)
        b = int(j*stepb)
	setor(fita,inicio,fim,r,g,b)


for i in range(3):
	fadesetorstep(fita,10,30,0,50,50,10)


