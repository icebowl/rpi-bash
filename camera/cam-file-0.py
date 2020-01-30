#65536.py cwc
import random
import datetime
from picamera import PiCamera
from time import sleep

def getDateString():
	dt = datetime.datetime.now()
	y = dt.year - 2000 
	hr = dt.hour
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
	 
def main():
	camPict()

if __name__ == '__main__':
	main()

#python 65536.py > 191213-1302.txt
