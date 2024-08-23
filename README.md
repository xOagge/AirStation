Arduino Sensor Display and Data Logging

This project involves an Arduino system that reads temperature, humidity, and light intensity using various sensors, displays the information on an I2C LCD, and logs the data to a text file for external processing. The system also includes a real-time clock (RTC) to timestamp the data.
Components Required

    Arduino Board (e.g., Arduino Uno)
    DHT11 Sensor: For temperature and humidity measurement
    Photocell: For light intensity measurement
    RTC Module (e.g., DS3231): For real-time clock functionality
    I2C LCD Display (20x4 or similar)
    Connecting Wires and Breadboard

Code Overview
Arduino Code
Libraries

    Wire.h: Provides I2C communication functionality.
    LiquidCrystal_I2C.h: Controls the LCD display over I2C.
    DHT.h: Manages interactions with the DHT11 sensor.
    RTClib.h: Handles real-time clock operations.

Functionality

    Initialization: Sets up serial communication, LCD display, sensors, and RTC module.
    Data Reading: Collects temperature, humidity, and light level from the sensors.
    Display Update: Updates the LCD with current time, temperature, humidity, and light level.
    Serial Output: Sends sensor data to the serial port for logging.

Key Functions

    setup(): Initializes the system components and sets up the display.
    loop(): Continuously updates the display and sends sensor data to the serial port every second.
    processTimeAndValidate(): Retrieves and validates the current time.
    processPhotocellAndValidate(): Reads and validates light level data.
    processTempAndValdiate(): Reads and validates temperature data.
    processHumidAndValdiate(): Reads and validates humidity data.
    setupDisplay(): Initializes and sets up the LCD display.
    UpdateDisplay(): Updates the LCD display and serial output with current sensor readings.

Serial Output Format

The Arduino sends data over the serial port in the following format:

    Time: Current time in HH:MM:SS DD/MM format.
    Temperature: Temperature in degrees Celsius.
    Humidity: Humidity percentage.
    Light Level: Light intensity value from the photocell.

Example Serial Output:

  15:13:10 23/08 T: 24.5
  15:13:10 23/08 H: 60.0
  15:13:10 23/08 L: 512

Setup

    Upload Arduino Code: Use the Arduino IDE to upload the provided code to your Arduino board.
    Connect Sensors: Wire the DHT11 sensor, photocell, and RTC module to the Arduino as specified in the code.
    Connect LCD Display: Wire the I2C LCD display to the Arduino.
    Monitor Serial Output: Open the Serial Monitor in the Arduino IDE to view data output from the Arduino.

Usage

    Initialize Components: Ensure all components are correctly connected and powered.
    Observe Display: The LCD will show real-time data for temperature, humidity, and light intensity.
    Log Data: Serial output can be captured using the Arduino IDE's Serial Monitor or an external script for further processing.

Troubleshooting

    LCD Display Issues: Ensure the I2C connections are properly made and the correct I2C address is used.
    Sensor Readings: Verify sensor connections and calibration. Ensure sensors are functional and properly connected.
    Serial Output: If data is not appearing, check the serial connection and verify the baud rate matches the Arduino’s settings.

License

This project is open-source and licensed under the MIT License.
