from machine import Pin, PWM

import time

pwm0 = PWM(Pin(14))  
pwm0.freq(1000)         # set frequency
pwm0.duty(200)          # set duty cycle
time.sleep_ms(1000)
pwm0.deinit()           # turn off PWM on the pin

pwm1 = PWM(Pin(14), freq=500, duty=512) # 
time.sleep_ms(10000)
 
