import time
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1024, 768)
time.sleep(1)

#capture images using the camera class
camera.capture('/home/pi/Pictures/snap.jpg')

#resize and capture
camera.capture('/home/pi/Pictures/resized.jpg', resize=(320, 240))

