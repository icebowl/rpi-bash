from picamera import PiCamera
from time import sleep
from datetime import datetime

import time
import RPi.GPIO as GPIO
camera = PiCamera()

def getDateString():
  now = datetime.now()
  #print("now =", now)
  dt_string = now.strftime("%d-%m-%Y~%H:%M:%S")
  #print("date and time =", dt_string)    
  return dt_string
 
def camPict():
  filename = getDateString()
  filename = "/home/pi/photos/" + filename + ".jpg"	

  #camera.resolution = (1920, 1080)
  camera.rotation = 180
  #camera.preview.resolution = (1920, 1080)
  camera.start_preview()
  # Camera warm-up time
  sleep(0.5)
  camera.capture(filename)
  camera.stop_preview()

def ussScan():
  try:
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 7
    PIN_ECHO = 11
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    #print ("Waiting for sensor to settle")
    time.sleep(0.25)
    #print ("Calculating distance")
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO)==0:
      pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
      pulse_end_time = time.time()
      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print (" ",distance,end="")
    if (distance < 300):
      camPict()

  finally:
    GPIO.cleanup()

def main():
  count = 0
  while(count == 0):
    ussScan()

if __name__ == '__main__':
	main()





