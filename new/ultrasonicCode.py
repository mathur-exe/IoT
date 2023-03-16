import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set up the pins for the ultrasonic sensor
TRIG = 23  #pin 16 on pi
ECHO = 24  #pin 18 on pi
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        # Send a pulse to the ultrasonic sensor
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for the echo to be received
        while GPIO.input(ECHO) == False:
            pulse_start = time.time()

        while GPIO.input(ECHO) == True:
            pulse_end = time.time()

        # Calculate the distance
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        # Print the distance to the console
        print("Distance: ", distance/100, "meter")

        # Wait a little bit before sending the next pulse
        time.sleep(0.5)

except KeyboardInterrupt:
    # Clean up the GPIO pins
    GPIO.cleanup()

