# DHT11
'''
Steps for using DHT11
- create library folder on desktop of RasPi
- git clone https://github.com/adafruit/Adafruit_Python_DHT
- <sudo python setup.py install> from the cloned folder

- sensor = Adafruit_DHT.DHT11
'''
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

# RFID
'''
Enable SPI in RasPi
- sudo raspi-config
- select “P4 SPI"
- <sudo reboot> restart RasPi
- <lsmod | grep spi> checking if SPI is enabled or not

gettting RasPi python ready
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install python3-dev python3-pip
- sudo pip3 install spidev
- sudo pip3 install mfrc522
- 
'''
# RFID Read
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()

# RFID Write
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()

# 