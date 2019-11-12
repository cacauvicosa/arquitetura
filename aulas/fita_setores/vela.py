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


def Draw(fita):
	Clear(fita)
	for i in range(CNT):
  		AddColor(fita,i, fire_color)
		r = random.randrange(80)
  		diff_color = ( r, r/2, r/2)
  		SubstractColor(fita,i, diff_color)
	fita.write()

AddColor(uint8_t position, uint32_t color)
{
uint32_t blended_color = Blend(strip.getPixelColor(position), color);
strip.setPixelColor(position, blended_color);
}

///
/// Set color of LED
///
void NeoFire::SubstractColor(uint8_t position, uint32_t color)
{
uint32_t blended_color = Substract(strip.getPixelColor(position), color);
strip.setPixelColor(position, blended_color);
}

///
/// Color blending
///
uint32_t NeoFire::Blend(uint32_t color1, uint32_t color2)
{
uint8_t r1,g1,b1;
uint8_t r2,g2,b2;
uint8_t r3,g3,b3;

r1 = (uint8_t)(color1 >> 16),
g1 = (uint8_t)(color1 >>  8),
b1 = (uint8_t)(color1 >>  0);

r2 = (uint8_t)(color2 >> 16),
g2 = (uint8_t)(color2 >>  8),
b2 = (uint8_t)(color2 >>  0);

return strip.Color(constrain(r1+r2, 0, 255), constrain(g1+g2, 0, 255), constrain(b1+b2, 0, 255));
}

///
/// Color blending
///
uint32_t NeoFire::Substract(uint32_t color1, uint32_t color2)
{
uint8_t r1,g1,b1;
uint8_t r2,g2,b2;
uint8_t r3,g3,b3;
int16_t r,g,b;

r1 = (uint8_t)(color1 >> 16),
g1 = (uint8_t)(color1 >>  8),
b1 = (uint8_t)(color1 >>  0);

r2 = (uint8_t)(color2 >> 16),
g2 = (uint8_t)(color2 >>  8),
b2 = (uint8_t)(color2 >>  0);

r=(int16_t)r1-(int16_t)r2;
g=(int16_t)g1-(int16_t)g2;
b=(int16_t)b1-(int16_t)b2;
if(r<0) r=0;
if(g<0) g=0;
if(b<0) b=0;

return strip.Color(r, g, b);
}

///
/// Every LED to black
///
void NeoFire::Clear()
{
for(uint16_t i=0; i<strip.numPixels (); i++)
  strip.setPixelColor(i, off_color);
}

NeoFire fire(strip);

///
/// Setup
///
void setup()
{
strip.begin();
strip.setBrightness(50);
strip.show(); // Initialize all pixels to 'off'
}

///
/// Main loop
///
void loop()
{
fire.Draw();
delay(random(50,150));
}
