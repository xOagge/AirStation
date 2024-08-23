# Arduino Sensor Display and Data Logging

This project involves an Arduino system that reads temperature, humidity, and light intensity from sensors, displays the information on an I2C LCD, and logs the data to the serial output. The system also uses a real-time clock (RTC) to timestamp the data.

## Components Required

- Arduino Uno (or similar)
- DHT11 Sensor (for temperature and humidity)
- Photocell (for light intensity measurement)
- RTC Module (e.g., DS3231)
- I2C LCD Display (20x4 or similar)
- Connecting wires and breadboard

## Code Overview

### Arduino Code

- **Serial Communication:** Sends sensor data over the serial port for logging.
- **Sensors:**
  - **Temperature & Humidity:** Read from the DHT11 sensor.
  - **Light Intensity:** Read from a photocell.
  - **Time:** Managed by the RTC module (DS3231).
- **Display:**
  - **LCD Display:** Shows real-time data including temperature, humidity, and light intensity.
- **Functions:**
  - **`processTimeAndValidate()`:** Updates and validates the time display on the LCD.
  - **`processPhotocellAndValidate()`:** Reads and validates the light intensity value.
  - **`processTempAndValidate()`:** Reads and validates the temperature value.
  - **`processHumidAndValidate()`:** Reads and validates the humidity value.
  - **`UpdateDisplay()`:** Updates the LCD with the latest sensor readings and logs data to the serial output.

### Libraries Used

- **`Wire.h`:** For I2C communication with the LCD and RTC.
- **`LiquidCrystal_I2C.h`:** For controlling the I2C LCD display.
- **`DHT.h`:** For reading temperature and humidity from the DHT11 sensor.
- **`RTClib.h`:** For interfacing with the RTC module.

## Setup

1. **Connect Components:** 
   - Connect the DHT11 sensor to the defined pin.
   - Attach the photocell to the analog input pin.
   - Wire the RTC module and LCD display to the I2C bus.
2. **Upload Arduino Code:** Use the Arduino IDE to upload the provided code to your Arduino board.
3. **Open Serial Monitor:** Ensure the serial monitor is set to 9600 baud to view logged data.

## Data Logging

- **Format:**
  - **Time:** Current timestamp from the RTC.
  - **Temperature:** Value from the DHT11 sensor in Celsius.
  - **Humidity:** Value from the DHT11 sensor in percentage.
  - **Light Intensity:** Value from the photocell (analog reading).
- **Logging Frequency:** Data is logged every second.

## Display

- **LCD Screen:**
  - **Line 1:** Displays the current time.
  - **Line 2:** Shows the temperature in Celsius.
  - **Line 3:** Shows the humidity percentage.
  - **Line 4:** Shows the light intensity.

## Troubleshooting

- **Incorrect Display:** Ensure all sensor connections are secure and check for proper library installation.
- **No Data on Serial Monitor:** Verify that the Arduino board is correctly connected and the serial monitor is set to the correct baud rate.
- **LCD Issues:** Confirm the I2C address and wiring are correct for the LCD display.

## License

This project is open-source and licensed under the [MIT License](https://opensource.org/licenses/MIT).
