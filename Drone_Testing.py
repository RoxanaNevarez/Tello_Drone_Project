#Objective: testing motion commands of drone

# imports Tello commands from djitellopy library
from djitellopy import Tello

# assigning tello variable to Tello class from tello.py
tello = Tello()

# connecting tello to PyCharm, so it can receive any code/commands
tello.connect()
# PyCharm will get the battery percentage of the tello
tello.get_battery()
# PyCharm will print the battery percentage of the tello in the command prompt
print(tello.get_battery())

# tello will take off
tello.takeoff()
# tello will move left 30cm
tello.move_left(30)
# tello will rotate 90 degrees CCW
tello.rotate_counter_clockwise(90)
# tello will move forward 30cm
tello.move_forward(30)
# tello will move back 30cm
tello.move_back(30)
# tello will rotate 90 degrees CW
tello.rotate_clockwise(90)
# tello will move right 30cm
tello.move_right(30)
# tello will flip left
tello.flip_left()
# tello will land
tello.land()
