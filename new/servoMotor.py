import RPi.GPIO as GPIO
import time

#connect to pin 12 of pi(gpio 18)
# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Create a PWM object for the servo
pwm = GPIO.PWM(18, 50)  # 50 Hz frequency

# Set the initial position of the servo
pwm.start(7.5)  # 7.5% duty cycle (middle position)

try:
    while True:
        # Move the servo to the left
        pwm.ChangeDutyCycle(10)  # 10% duty cycle
        time.sleep(1)

        # Move the servo to the right
        pwm.ChangeDutyCycle(5)  # 5% duty cycle
        time.sleep(1)

        # Move the servo back to the middle
        pwm.ChangeDutyCycle(7.5)  # 7.5% duty cycle
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up the GPIO pins
    pwm.stop()
    GPIO.cleanup()
