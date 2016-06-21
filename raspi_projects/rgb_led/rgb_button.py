import RPi.GPIO as GPIO
import time
import itertools

GPIO.setmode(GPIO.BCM)

pins = {"r":14, "g":15, "b":18}
 
for pin in pins.values():
	GPIO.setup(pin, GPIO.OUT)

def setcolor(color):
	for pin in pins.keys():
		GPIO.output(pins.get(pin), (color == pin))


GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

triggered=False

iterator=itertools.cycle(pins)

while (True):
	time.sleep(0.1)
	
	if (not triggered and not GPIO.input(3)):
		triggered = True		
		print("click")
	elif (triggered and GPIO.input(3)):
		setcolor(next(iterator))
		triggered = False
		print("unclick")


