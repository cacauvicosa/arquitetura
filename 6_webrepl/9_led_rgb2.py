from machine import Pin, PWM

import time

pwm0 = PWM(Pin(0))  
pwm0.freq(1000)         # set frequency
pwm0.duty(512)          # set duty cycle
time.sleep_ms(1000)
pwm0.deinit()           # turn off PWM on the pin

pwm1 = PWM(Pin(5), freq=500, duty=200) # 
time.sleep_ms(10000)
pwm1.deinit() 
