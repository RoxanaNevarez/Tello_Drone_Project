#Objective: gaining practice with having drone take pictures

# cv2 module will be imported
import cv2
# Tello function will be imported from djitellopy library
from djitellopy import Tello
# assigning tello variable to Tello() function
tello = Tello()
# connecting tello to PyCharm, so it can receive all code commands
tello.connect()

# turning on drone's video stream
tello.streamon()
# must be followed by tello.get_frame_read() every time
frame_read = tello.get_frame_read()

# tello will fly up
tello.takeoff()
tello.move_up(130)

# saves image captured by drone into specified file (in this case Drone_Picture)
# frame_read.frame is always needed for any cv2 command
cv2.imwrite("Drone_Picture.png", frame_read.frame)

# tello will land on surface encountered
tello.land()
