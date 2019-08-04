# lights.py

import time
import RPi.GPIO as GPIO

chan_list = [4,9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setwarnings(False)

a = 4

if a < 5:
   print('Turning on the Green Light')
   GPIO.output(4, True)
   time.sleep(2)
   GPIO.output(4, False)
elif a >= 5:
   print('Turning on the White Light')
   GPIO.output(9, True)
   time.sleep(2)
   GPIO.output(9, False)
else:
    print("I'm not turning on any lights.")
    
GPIO.cleanup()
    


