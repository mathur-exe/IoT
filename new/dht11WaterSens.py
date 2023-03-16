import Adafruit_DHT
import time

# Set up the sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  #pin 7 on pi

while True:
    # Try to get a reading from the sensor
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    # If the reading was successful, print the values
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
    else:
        print("Failed to read sensor data")

    # Wait a little bit before taking the next reading
    time.sleep(2)
