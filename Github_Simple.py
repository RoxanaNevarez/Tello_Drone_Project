# imports Tello commands from djitellopy library
from djitellopy import Tello

# tello variable is assigned to Tello class from tello.py
tello = Tello()

# tello will connect to PyCharm and will be ready to receive any incoming code
tello.connect()

# tello will lift from the ground
tello.takeoff()

# tello will move left 30cm
tello.move_left(30)

# tello will rotate 90 degrees counter clockwise
tello.rotate_counter_clockwise(90)

# tello will move forward 30cm
tello.move_forward(30)

# tello will land
tello.land()
