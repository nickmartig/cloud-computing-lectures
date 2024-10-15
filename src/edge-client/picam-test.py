from picamera2 import Picamera2
from time import sleep

# Initialize the camera
picam2 = Picamera2()
picam2.start()

# Allow the camera some time to adjust settings
sleep(2)

# Capture an image
picam2.capture_file("image.jpg")
print("Image captured and saved as image.jpg")
