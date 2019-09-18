import machine
import time

def toggle(p):
	p.value(not p.value())


pin = machine.Pin(2, machine.Pin.OUT)
for j in range(10):
	for i in range(100):
		pin.off()
		time.sleep_ms(1)
		pin.on()
		time.sleep_ms(8)

# pwm  pulse wave modulation



