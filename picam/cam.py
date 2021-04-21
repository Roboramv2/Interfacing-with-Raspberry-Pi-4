import time
from picamera import PiCamera
camera = PiCamera()
time.sleep(0.0005)
camera.capture('/home/pi/Pictures/snap.jpg')