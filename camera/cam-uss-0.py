from picamera import PiCamera
from time import sleep
import time
import datetime
import RPi.GPIO as GPIO

def getDateString():
  dt = datetime.datetime.now();y = dt.year - 2000 ;hr = dt.hour
  if hr < 10:
    hr = "0" + str(hr)
    me = dt.minute
  if me < 10:
    me = "0" + str(me)
  timestring = str(y) + str(dt.month) + str(dt.day)+"-"+str(hr)+str(me)+"."+str(dt.second)
  return timestring

def camPict():
  filename = getDateString()
  filename = filename + ".jpg"	
  camera = PiCamera()
  #camera.resolution = (1024, 768)
  camera.rotation = 180
  camera.start_preview()
  # Camera warm-up time
  sleep(1)
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
    time.sleep(1)
    print ("Calculating distance")
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO)==0:
      pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
      pulse_end_time = time.time()
      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print ("Distance:",distance,"cm")
    if (distance < 100):
      camPict()

  finally:
    GPIO.cleanup()

def main():
  count = 0
  while(count == 0):
    ussScan()

if __name__ == '__main__':
	main()





