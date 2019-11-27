/*  
 * ____                     _      ______ _____    _____
  / __ \                   | |    |  ____|  __ \  |  __ \               
 | |  | |_ __   ___ _ __   | |    | |__  | |  | | | |__) |__ _  ___ ___ 
 | |  | | '_ \ / _ \ '_ \  | |    |  __| | |  | | |  _  // _` |/ __/ _ \
 | |__| | |_) |  __/ | | | | |____| |____| |__| | | | \ \ (_| | (_|  __/
  \____/| .__/ \___|_| |_| |______|______|_____/  |_|  \_\__,_|\___\___|
        | |                                                             
        |_|          
 Open LED Race
 An minimalist cars race for LED strip  
  
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 3 of the License, or
 (at your option) any later version.

 by gbarbarov@singulardevices.com  for Arduino day Seville 2019 

 Code made dirty and fast, next improvements in: 
 https://github.com/gbarbarov/led-race
 https://www.hackster.io/gbarbarov/open-led-race-a0331a
 https://twitter.com/openledrace
*/


#include <ESP8266WiFi.h>
#include <PubSubClient.h>
const char* ssid = "sua rede WIFI";
const char* password = "sua senha";

const char* mqtt_server = "broker.mqtt-dashboard.com";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("fita", "hello world");
      // ... and resubscribe
      client.subscribe("fita/carroverde");
      client.subscribe("fita/carrovermelho");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


                                                            
#include <Adafruit_NeoPixel.h>
#define MAXLED         300 // MAX LEDs actives on strip

#define PIN_LED        D3  // R 500 ohms to DI pin for WS2812 and WS2813, for WS2813 BI pin of first LED to GND  ,  CAP 1000 uF to VCC 5v/GND,power supplie 5V 2A  

int PIN_P1=0;   // switch player 1 to PIN and GND
int PIN_P2=0;           // switch player 2 to PIN and GND 


int NPIXELS=MAXLED; // leds on track

#define COLOR1    track.Color(255,0,0)
#define COLOR2    track.Color(0,255,0)

      
byte  gravity_map[MAXLED];     

int TBEEP=3; 

float speed1=0;
float speed2=0;
float dist1=0;
float dist2=0;

byte loop1=0;
byte loop2=0;

byte leader=0;
byte loop_max=5; //total laps race


float ACEL=0.2;
float kf=0.015; //friction constant
float kg=0.003; //gravity constant

byte flag_sw1=0;
byte flag_sw2=0;
byte draworder=0;
 
unsigned long timestamp=0;

Adafruit_NeoPixel track = Adafruit_NeoPixel(MAXLED, PIN_LED, NEO_GRB + NEO_KHZ800);

int tdelay = 5; 

void set_ramp(byte H,byte a,byte b,byte c)
{for(int i=0;i<(b-a);i++){gravity_map[a+i]=127-i*((float)H/(b-a));};
 gravity_map[b]=127; 
 for(int i=0;i<(c-b);i++){gravity_map[b+i+1]=127+H-i*((float)H/(c-b));};
}

void set_loop(byte H,byte a,byte b,byte c)
{for(int i=0;i<(b-a);i++){gravity_map[a+i]=127-i*((float)H/(b-a));};
 gravity_map[b]=255; 
 for(int i=0;i<(c-b);i++){gravity_map[b+i+1]=127+H-i*((float)H/(c-b));};
}


void setup() {
  for(int i=0;i<NPIXELS;i++){gravity_map[i]=127;};
  track.begin(); 

 // if ((digitalRead(PIN_P1)==0)) //push switch 1 on reset for activate physic
  {
    set_ramp(20,180,195,215);    // ramp centred in LED 100 with 10 led fordward and 10 backguard 
    for(int i=0;i<NPIXELS;i++){track.setPixelColor(i, track.Color(0,0,(127-gravity_map[i])/8) );};
    track.show();
  };
  start_race();    
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  String Topic(topic);
  Serial.print(Topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  if ( Topic.equals("fita/carroverde") ) {
    PIN_P1 = !PIN_P1;
  }
  if ( Topic.equals("fita/carrovermelho") ) {
    PIN_P2 = !PIN_P2;
  }

}

void start_race(){for(int i=0;i<NPIXELS;i++){track.setPixelColor(i, track.Color(0,0,0));};
                  track.show();
                  delay(2000);
                  track.setPixelColor(12, track.Color(0,255,0));
                  track.setPixelColor(11, track.Color(0,255,0));
                  track.show();
                  track.setPixelColor(12, track.Color(0,0,0));
                  track.setPixelColor(11, track.Color(0,0,0));
                  track.setPixelColor(10, track.Color(255,255,0));
                  track.setPixelColor(9, track.Color(255,255,0));
                  track.show();
                  track.setPixelColor(9, track.Color(0,0,0));
                  track.setPixelColor(10, track.Color(0,0,0));
                  track.setPixelColor(8, track.Color(255,0,0));
                  track.setPixelColor(7, track.Color(255,0,0));
                  track.show();
                  timestamp=0;              
                 };

void winner_fx() {
           

                                               
              };

void burning1(){
//to do
 }

void burning2(){
//to do
 }

void track_rain_fx(){
//to do
 }

void track_oil_fx(){
//to do
 }

void track_snow_fx(){
//to do
 }


void fuel_empty(){
//to do
 }

void fill_fuel_fx(){
//to do
 }

void in_track_boxs_fx(){
//to do
 }

void pause_track_boxs_fx(){
//to do
 }
 
void flag_boxs_stop(){
//to do
 }

void flag_boxs_ready(){
//to do
 }

void draw_safety_car(){
//to do
 }

void telemetry_rx(){
  //to do
 }
 
void telemetry_tx(){
  //to do
 }

void telemetry_lap_time_car1(){
//to do
 }

void telemetry_lap_time_car2(){
//to do
 }

void telemetry_record_lap(){
//to do
 }

void telemetry_total_time(){
//to do
 }

int read_sensor(byte player){
//to do
}

int calibration_sensor(byte player){
  //to do  
}

int display_lcd_laps(){
  //to do  
}

int display_lcd_time(){
  //to do  
}



void draw_car1(void){for(int i=0;i<=loop1;i++){track.setPixelColor(((word)dist1 % NPIXELS)+i, track.Color(0,255-i*20,0));};                   
  }

void draw_car2(void){for(int i=0;i<=loop2;i++){track.setPixelColor(((word)dist2 % NPIXELS)+i, track.Color(255-i*20,0,0));};            
 }
  
void loop() {
    for(int i=0;i<NPIXELS;i++){track.setPixelColor(i, track.Color(0,0,0));};
    if (!client.connected()) {
    reconnect();
    }
    client.loop();

    if ( (flag_sw1==1) && (PIN_P1==0) ) {flag_sw1=0;speed1+=ACEL;};
    if ( (flag_sw1==0) && (PIN_P1==1) ) {flag_sw1=1;};

    
    speed1-=speed1*kf; 
    
    if ( (flag_sw2==1) && (PIN_P2==0) ) {flag_sw2=0;speed2+=ACEL;};
    if ( (flag_sw2==0) && (PIN_P2==1) ) {flag_sw2=1;};

        
    speed2-=speed2*kf; 
        
    dist1+=speed1;
    dist2+=speed2;

    if (dist1>dist2) {leader=1;} 
    if (dist2>dist1) {leader=2;};
      
    if (dist1>NPIXELS*loop1) {loop1++;};
    if (dist2>NPIXELS*loop2) {loop2++;};

    if (loop1>loop_max) {for(int i=0;i<NPIXELS;i++){track.setPixelColor(i, track.Color(0,255,0));}; track.show();
                                                    winner_fx();loop1=0;loop2=0;dist1=0;dist2=0;speed1=0;speed2=0;timestamp=0;
                                                    start_race();
                                                   }
    if (loop2>loop_max) {for(int i=0;i<NPIXELS;i++){track.setPixelColor(i, track.Color(255,0,0));}; track.show();
                                                    winner_fx();loop1=0;loop2=0;dist1=0;dist2=0;speed1=0;speed2=0;timestamp=0;
                                                    start_race();
                                                   }
    if ((millis() & 512)==(512*draworder)) {if (draworder==0) {draworder=1;}
                          else {draworder=0;}   
                         }; 

    if (draworder==0) {draw_car1();draw_car2();}
        else {draw_car2();draw_car1();}   
                 
    track.show(); 
    delay(tdelay);
    
    
}
