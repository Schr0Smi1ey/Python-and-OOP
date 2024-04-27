# pip install opencv-contrib-python


# Importing the OpenCV module
import cv2

# Opening the default camera (0) for capturing video
cam = cv2.VideoCapture(0)

# Continuously capturing frames from the camera
while True:
    # Reading a frame from the camera
    _, frame = cam.read()
    
    # Displaying the frame in a window named 'my cam'
    cv2.imshow('my cam', frame)
    
    # Waiting for a key press with a delay of 1 millisecond
    cv2.waitKey(1)
