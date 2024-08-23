#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "DHT.h"
#include <RTClib.h>

// Define the LCD I2C address and dimensions (20 columns, 4 rows)
LiquidCrystal_I2C lcd(0x27, 20, 4);
RTC_DS3231 rtc;

// Photocell pin
#define PHOTOCELL_PIN A4
// DHT sensor settings
#define DHTPIN A5        // DHT sensor pin connected to A3
#define DHTTYPE DHT11    // DHT11 sensor type
DHT dht(DHTPIN, DHTTYPE);

float temp = 0;
float humidity = 0;
int lightLevel = 0;
String currentTime = "";

void setup() {
  Serial.begin(9600);
  setupDisplay();
  Wire.begin();
  dht.begin();
  rtc.begin();
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
}

void loop() {
  UpdateDisplay();
  delay(1000);
}

// Function to process time based on millis()
bool processTimeAndValidate() {
  DateTime now = rtc.now();  // Get the current time from the RTC
  String timeRead = (String(now.hour() < 10 ? "0" : "") + String(now.hour()) + ":" +
                     String(now.minute() < 10 ? "0" : "") + String(now.minute()) + ":" +
                     String(now.second() < 10 ? "0" : "") + String(now.second()) + " " +
                     String(now.day() < 10 ? "0" : "") + String(now.day()) + "/" +
                     String(now.month() < 10 ? "0" : "") + String(now.month()));
  if(timeRead != currentTime) {
    currentTime = timeRead;
    return true;
  }
  return false;
}

// Function to read photocell and return true if the value has changed
bool processPhotocellAndValidate() {
  int lightRead = analogRead(PHOTOCELL_PIN);
  if (lightRead != lightLevel) {
    lightLevel = lightRead;
    return true;
  }
  return false;
}

bool processTempAndValdiate(){
   float tempRead = dht.readTemperature();
  if(temp != tempRead){
    temp = tempRead;
    return true;
  }
  return false;
}

bool processHumidAndValdiate(){
  float humidityRead = dht.readHumidity();
  if(humidity != humidityRead){
    humidity = humidityRead;
    return true;
  }
  return false;
}

void setupDisplay(){
  // Initialize the LCD and start it
  lcd.begin();
  lcd.backlight();
  // Display initial message
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Initializing...");
  lcd.setCursor(0,1);
  lcd.print("Temp: ");
  lcd.setCursor(0,2);
  lcd.print("Humidity: ");
  lcd.setCursor(0,3);
  lcd.print("Irradiance: ");
}

void UpdateDisplay() {
  // Update time
  if (processTimeAndValidate()) {
    lcd.setCursor(0,0);
    lcd.print("                ");
    lcd.setCursor(0,0);
    lcd.print("Time: ");
    lcd.print(currentTime);
      // Update temperature
    if (processTempAndValdiate()) {
      lcd.setCursor(6,1);
      lcd.print("        ");
      lcd.setCursor(6,1);
      lcd.print(temp);
      lcd.print(" C");
    }
    // Update humidity
    if (processHumidAndValdiate()) {
      lcd.setCursor(10,2);
      lcd.print("      ");
      lcd.setCursor(10,2);
      lcd.print(humidity);
      lcd.print("%");
    }
    // Update irradiance
    if (processPhotocellAndValidate()) {
      lcd.setCursor(12,3);
      lcd.print("      ");
      lcd.setCursor(12,3);
      lcd.print(lightLevel);
      lcd.print(" ");
    }
    //for python scrip to get continuous values per each second
    Serial.print(currentTime);
    Serial.print(" T: ");
    Serial.println(temp);
    Serial.print(currentTime);
    Serial.print(" H: ");
    Serial.println(humidity);
  }
}
