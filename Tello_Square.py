#Objective: Tello drone flies in an upright square circuit

# importing time and cv2 modules
import time, cv2
# importing Thread function from threading library
from threading import Thread
# importing Tello function from djitellopy library
from djitellopy import Tello

tello = Tello()
tello.connect()

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
    # assigning variable video to cv2 module commanding VideoWriter action (takes a video)
    #
    video = cv2.VideoWriter('Tello_Square.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    # while keepRecording remains assigned to True, the code within the while loop will execute
    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()
# battery will be printed before tello flies
tello.get_battery()
# tello will take off
tello.takeoff()

# tello will move upwards an additional 125cm
tello.move_up(125)

# tello scans the room
tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(90)
tello.rotate_clockwise(90)

# tello completes the square
tello.move_forward(125)
tello.flip_forward()
tello.move_down(125)
tello.move_back(120)
tello.flip_back()
# tello flips to the right
tello.flip_right()

# tello will adjust itself to end near its original starting point
tello.rotate_counter_clockwise(90)
tello.flip_left()
tello.move_right(35)
tello.move_forward(50)
tello.land()

# tello will end video streaming after landing
keepRecording = False
recorder.join()
tello.streamoff()
tello.end()

