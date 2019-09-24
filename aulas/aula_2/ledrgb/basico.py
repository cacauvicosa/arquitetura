from machine import Pin, PWM
import time

red = PWM(Pin(0))  
blue = PWM(Pin(4))  
green = PWM(Pin(5))  

def name():
   print ("MicroPython-1c376d")
   print ("Led RGB GPIO 0,4,5 (D...)")

def help():
   print ("name ")
   print ("scan blink once R 1s G 1s B 1s")

def scan():
   global red,green,blue
   red = PWM(Pin(0), freq=1000, duty=512)  
   time.sleep(1) 
   red.deinit()
   green = PWM(Pin(5), freq=1000, duty=512)  
   time.sleep(1) 
   green.deinit()
   blue = PWM(Pin(4), freq=1000, duty=512)  
   time.sleep(1) 
   blue.deinit()

def fade(pin):
    led = PWM(Pin(pin), freq=1000, duty=10)  
    for i in range(100):
	led.duty(i)
        time.sleep_ms(10)
    for i in range(90):
	led.duty(10*i+100)
        time.sleep_ms(20)
    for i in range(90):
	led.duty(1000-(10*i))
        time.sleep_ms(20)
    for i in range(100):
	led.duty(100-i)
        time.sleep_ms(10)
    

def off(pin):
    led = PWM(Pin(pin))
    led.deinit()
 
