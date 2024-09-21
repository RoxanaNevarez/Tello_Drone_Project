#Early stages of learning Python programming to control drone

# recall syntax to import a function from a library: from <library> import <function>
# imports Tello commands from djitellopy library
from djitellopy import Tello

# tello variable is assigned to Tello class from tello.py
tello = Tello()

# everything below this point has to do with knowing dot notation
# for dot notation, that requires knowing classes and user-defined functions

# recall syntax for classes:

# class <class_definition>(object):
     #perform logic below

# recall syntax for user-defined functions: 

# def <function_name>(<parameters:optional>):
     #perform logic below

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
