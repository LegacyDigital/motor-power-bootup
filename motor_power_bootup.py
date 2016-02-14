
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

print "Sleeping..."
time.sleep(200)

print "Powering on..."
GPIO.output(7, True)





