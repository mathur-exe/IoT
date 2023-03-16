import RPi.GPIO as GPIO
import time

# Set up the GPIO pin:
RAIN_PIN = 18 #pin 12 of pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_PIN, GPIO.IN)

while True:
    # Read the digital value from the raindrop sensor:
    rain_value = GPIO.input(RAIN_PIN)

    # If the raindrop sensor is wet (i.e., the digital value is low), print a message:
    if rain_value == GPIO.LOW:
        print('It\'s raining!')
    else:
        print('It\'s not raining.')

    # Wait for 1 second before reading again:
    time.sleep(1)
