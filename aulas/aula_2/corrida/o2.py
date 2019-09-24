NPIXELS=300  # numero de pixels da Fita

def draw_p1():
	global track, dist1, old_dist1
	j = int(old_dist1)
	for i in range(loop1+1):
		if j % NPIXELS+i < NPIXELS:
			track[j % NPIXELS+i] = (0,0,0)
	j = int(dist1)
	for i in range(loop1+1):
		if j % NPIXELS+i < NPIXELS:
			track[j % NPIXELS+i] = (0,255,0)
                    
def draw_p2():
	global track,dist2,old_dist2
	j = int(old_dist2)
	for i in range(loop2+1):
		if j % NPIXELS+i < NPIXELS:
			track[j % NPIXELS+i] = (0,0,0)
	j = int(dist2)
	for i in range(loop2+1):
		if j % NPIXELS+i < NPIXELS:
			track[j % NPIXELS+i] = (255,0,0)



from machine import Pin
from neopixel import NeoPixel
import time

speed1=0      # velocidade carro 1
speed2=0   # velocidade carro 2 (inicial)
dist1=0       # distancia percorrida pelo carro 1
dist2=0       # carro 2
old_dist1=0
old_dist2=0

loop1=0       # numero de voltas do carro 1 
loop2=0       # carro 2 

loop_max=5    # Maximo de voltas da corrida

ACEL=0.2    # aceleracao base 
FRICTION=0.01  # friccao (reducao da aceleracao)
kf=1.5         # constante de reducao da fricçao 

flag_sw1=0    # Flag para saber se o acel do Carro 1 foi apertado
flag_sw2=0    # carro 2


pinoFita = Pin(0, Pin.OUT)   # Pino 0 - D3 NodeMCU para conectar os leds NeoPixels
track = NeoPixel(pinoFita, NPIXELS)   # Cria a fita de led com 300 pixels
PIN_P1 = Pin(4,Pin.IN,Pin.PULL_UP) # d2 botao para acelerar o carro 1
PIN_P2 = Pin(5,Pin.IN,Pin.PULL_UP) # d1 botao para acelerar o carro 2
pin = Pin(2,Pin.OUT)

while True:
	if flag_sw1==1 and  PIN_P1.value()==0:
		flag_sw1=0  # para contar pressionou tem que mudar de 1 para 0
		speed1 = speed1 + ACEL # se vc pressionou, aumenta a velocidade

	if flag_sw1==0 and PIN_P1.value()==1: 
		flag_sw1=1  # Prepara o botao, agora esta desapertado

	speed1 = speed1 - FRICTION*speed1*kf 
	if speed1<0: 
		speed1=0

	if flag_sw2==1 and  PIN_P2.value()==0:
		flag_sw2=0  # para contar pressionou tem que mudar de 1 para 0
		speed2 = speed2 + ACEL # se vc pressionou, aumenta a velocidade

	if flag_sw2==0 and PIN_P2.value()==1: 
		flag_sw2=1  # Prepara o botao, agora esta desapertado
  	
	speed2 = speed2 - FRICTION*speed2*kf 
	if speed2<0: 
		speed2=0

	old_dist1= dist1
	old_dist2= dist2
	dist1=dist1+speed1
	dist2=dist2+speed2

    	if dist1>NPIXELS*loop1: 
		loop1 +=1
    	if dist2>NPIXELS*loop2: 
		loop2 +=1

	draw_p1()
	draw_p2()

	if loop1>loop_max:
		for i in range(NPIXELS):
			track[i] = (0,255,0)
		track.write()	                                                 	
		loop1=0
		time.sleep(1)
		for i in range(NPIXELS):
			track[i] = (0,0,0)
		loop2=0
		dist1=0
		dist2=0
		speed1=0


	if loop2>loop_max:
		for i in range(NPIXELS):
			track[i] = (255,0,0)
		track.write()	                                                 	
		loop1=0
		time.sleep(1)
		for i in range(NPIXELS):
			track[i] = (0,0,0)
		loop2=0
		dist1=0
		dist2=0
		speed2=0


	track.write()
