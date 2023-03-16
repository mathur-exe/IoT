library for ultrasonic and gas sensor and servo motor and raindropsensor

sudo apt-get install python-rpi.gpio
data pin connection is in code


ground is pin number 39 
5v vcc is pin 2
for all 3

and vcc for raindropsensor is pin1 of pi that is 3.3v
and ground pin to pin 39 of pi


library for dht11
Pin 1 is VCC (Power Supply) connected to pin 1 of pi
Pin 2 is DATA (The data signal) connected according to code
Pin 3 is NULL (Do not connect)
Pin 4 is GND (Ground) connected to pin 6 of pi

connected a 10k ohm resistor accros data pin and vcc pin of dht11(pin 1,2)
https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
