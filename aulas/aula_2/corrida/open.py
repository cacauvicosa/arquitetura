NPIXELS=300  # numero de pixels da Fita

def draw_p1():
	global track
	for i in range(loop1+1):
		track[dist1 % NPIXELS+i] = (0,255,0)
                    
def draw_p2():
	global track
	for i in range(loop2+1):
		track[dist2 % NPIXELS+i] = (255,0,0)



from machine import Pin
from neopixel import NeoPixel

speed1=0      # velocidade carro 1
speed2=1.25   # velocidade carro 2 (inicial)
dist1=0       # distancia percorrida pelo carro 1
dist2=0       # carro 2

loop1=0       # numero de voltas do carro 1 
loop2=0       # carro 2 

loop_max=5    # Maximo de voltas da corrida

ACEL=0.2     # aceleracao base 
FRICTION=0.01  # friccao (reducao da aceleracao)
kf=1.5         # constante de reducao da fricçao 

flag_sw1=0    # Flag para saber se o acel do Carro 1 foi apertado
flag_sw2=0    # carro 2

tdelay = 5   # atraso de 5ms para atualizar a fita com os carros
  

pinoFita = Pin(0, Pin.OUT)   # Pino 0 - D3 NodeMCU para conectar os leds NeoPixels
track = NeoPixel(pinoFita, NPIXELS)   # Cria a fita de led com 300 pixels
PIN_P1 = Pin(5,Pin.IN,Pin.PULL_UP) # d2 botao para acelerar o carro 1
PIN_P2 = Pin(4,Pin.IN,Pin.PULL_UP) # d1 botao para acelerar o carro 2


while True:
	for i in range(NPIXELS):
		track[i] = (0,0,0)  # apaga a pista

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

	dist1=dist1+speed1
	dist2=dist2+speed2
    	if dist1>NPIXELS*loop1: 
		loop1++
	if dist2>NPIXELS*loop2:
		loop2++

	draw_p1()
	draw_p2()
	track.write() 
 


