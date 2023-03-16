import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

MQ_PIN = 17 # pin 11 of pi

# Define the function to read the sensor value
def read_mq():
    GPIO.setup(MQ_PIN, GPIO.OUT)
    GPIO.output(MQ_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(MQ_PIN, GPIO.IN)

    while(GPIO.input(MQ_PIN) == GPIO.LOW):
        continue

    t1 = time.time()
    while(GPIO.input(MQ_PIN) == GPIO.HIGH):
        continue
    t2 = time.time()

    return (t2-t1)*1000000

# Define the main function to read and print the sensor value
def loop():
    while True:
        val = read_mq()
        print("MQ135 value: %d" % val)
        time.sleep(1)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        pass

GPIO.cleanup()

