import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = {"r":14, "g":15, "b":18}
 
for pin in pins.values():
	GPIO.setup(pin, GPIO.OUT)

def setcolor(color):
	for pin in pins.keys():
		GPIO.output(pins.get(pin), (pin in color))

setcolor("rb")
			
#while True:
#	for color in pins:
#		setcolor(color)
#		time.sleep(1)


