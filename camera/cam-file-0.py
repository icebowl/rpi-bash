#65536.py cwc
from datetime import datetime
from picamera import PiCamera
from time import sleep

def getDateString():
	now =datetime.now()
	nowYear = str(now.year);nowSeconds = str(now.second)
	dateTimeString =  nowYear[2:4]+str(now.month)+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+nowSeconds[0:2]
	print(dateTimeString)
	return dateTimeString
def camPict():
	filename = getDateString()
	filename = filename + ".jpg"	
	camera = PiCamera()
	#camera.resolution = (1024, 768)
	camera.rotation = 180
	camera.start_preview()
	# Camera warm-up time
	#sleep(1)
	camera.capture(filename)
	camera.stop_preview()
	 
def main():
	camPict()

if __name__ == '__main__':
	main()

