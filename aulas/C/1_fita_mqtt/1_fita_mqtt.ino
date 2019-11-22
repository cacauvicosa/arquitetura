#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.

#include <Adafruit_NeoPixel.h>
#define LED_PIN    D3
#define LED_COUNT 300
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

int inicio, fim;
uint32_t cor;
boolean grava=false;


//const char* ssid = "3gCacau";
//const char* password = "arduino351";
const char* ssid = "dlink-602C";
const char* password = "gitgt24651";

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


int number(byte *text, unsigned int length) {
  int x=0;
  int d;
  for (int i = 0; i < length; i++) {
    d = ((char)text[i]-48);
    x = x*10 + d; 
  }
  return x;
}


uint32_t text2color(byte *text, unsigned int length) {
  uint32_t x=0;
  int d;
  for (int i = 1; i < length; i++) {
    if ( (char)text[i] < 58) d = ((char)text[i]-48);
    else d = ((char)text[i]-97)+10;
    x = x*16 + d; 
  }
  return x;
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
      client.subscribe("fita/inicio");
      client.subscribe("fita/fim");
      client.subscribe("fita/cor");
      client.subscribe("fita/grava");
      client.subscribe("fita/apaga");
      client.subscribe("fita/fire"); 
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  pinMode(2, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(150); // Set BRIGHTNESS to about 1/5 (max = 255)

}


void colorWipe(uint32_t color, int wait) {
  for(int i=inicio; i<fim; i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
    strip.show();                          //  Update strip to match
    delay(wait);                           //  Pause for a moment
  }
}



void apaga() {
  for(int i=inicio; i<fim; i++) { // For each pixel in strip...
    strip.setPixelColor(i, 0);         //  Set pixel's color (in RAM)
                              //  Update strip to match                          //  Pause for a moment
  }
  strip.show();
}


///
/// Fire simulator
///
class NeoFire
{
  Adafruit_NeoPixel &strip;
 public:

  NeoFire(Adafruit_NeoPixel&);
  void Draw();
  void Clear();
  void AddColor(uint8_t position, uint32_t color);
  void SubstractColor(uint8_t position, uint32_t color);
  uint32_t Blend(uint32_t color1, uint32_t color2);
  uint32_t Substract(uint32_t color1, uint32_t color2);
};

///
/// Constructor
///
NeoFire::NeoFire(Adafruit_NeoPixel& n_strip)
: strip (n_strip)
{
}
uint32_t fire_color   = strip.Color ( 80,  35,  00);
uint32_t off_color    = strip.Color (  0,  0,  0);

///
/// Set all colors
///
void NeoFire::Draw()
{
Clear();

for(int i=inicio;i<fim;i++)
  {
  AddColor(i, fire_color);
  int r = random(80);
  uint32_t diff_color = strip.Color ( r, r/2, r/2);
  SubstractColor(i, diff_color);
  }
  
strip.show();
}

///
/// Set color of LED
///
void NeoFire::AddColor(uint8_t position, uint32_t color)
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

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

 /* long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    //snprintf (msg, 20, "%f", t);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("fita", msg);
  }
  */
  
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

  if ( Topic.equals("fita/inicio") ) {
    inicio = number(payload,length); // converter caracteres em um numero inteiro 
    Serial.println(inicio);
  }
  if ( Topic.equals("fita/fim") ) {
    fim = number(payload,length); // converter caracteres em um numero inteiro 
    Serial.println(fim);
  }
  if ( Topic.equals("fita/cor") ) {
    cor = text2color(payload,length); // converter caracteres em um numero inteiro 
    Serial.println(cor);
  }
  if ( Topic.equals("fita/grava") ) {
    if ( (char) payload[0] == '1') grava = true; // converter caracteres em um numero inteiro 
    Serial.println("grava");
    colorWipe(cor,10);
  }
  if ( Topic.equals("fita/apaga") ) {
    Serial.println("apaga");
    apaga();
  }

  if ( Topic.equals("fita/fire") ) {
    Serial.println("fire");
    fogo(5); // time in seconds
  }

}

void fogo(int t) {
  for (int i=0; i < t*10; i++){
    fire.Draw();
    delay(random(20,90));
  }
}  
  
