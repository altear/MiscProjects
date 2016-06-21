import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

triggered=False

while (True):
	time.sleep(0.1)
	
	if (triggered and not GPIO.input(3)):
		triggered = True
		print("click")
	elif (not triggered and GPIO.input(3)):
		triggered = False
		print("unclick")


