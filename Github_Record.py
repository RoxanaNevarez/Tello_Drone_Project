# importing time and cv2 modules
import time, cv2
# importing Thread function from threading library
from threading import Thread
# importing Tello function from djitellopy library
from djitellopy import Tello

# assigning tello variable to Tello() function
tello = Tello()

# connecting tello to PyCharm so it can execute code commands
tello.connect()

# assigning keepRecording variable to True(boolean)
keepRecording = True
# turning on drone's video stream
tello.streamon()
# must be typed after streamon() every time
frame_read = tello.get_frame_read()

# defining function videoRecorder
def videoRecorder():
    # the primary focus is to unpack the height and width from the frame shape captured once reading the image
    # length might be the ignored value in this case
    height, width, _ = frame_read.frame.shape
    # assigning variable video to cv2 module commanding VideoWriter action
    #
    video = cv2.VideoWriter('Drone_Recording.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    # while keepRecording remains assigned to True, the code within the while loop will execute
    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()
"""
# drone will take off
tello.takeoff()
# drone will move up 40cm
tello.move_up(40)
# drone will rotate CCW 360 degrees
tello.rotate_counter_clockwise(360)
# drone will land
tello.land()
"""
# keepRecording variable will be assigned to False (drone won't record anymore)
keepRecording = False
recorder.join()