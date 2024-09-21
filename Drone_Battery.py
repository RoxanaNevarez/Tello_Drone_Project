# importing Tello function from djitellopy library
from djitellopy import Tello

# assigning tello variable to Tello() function
tello = Tello()

# connecting tello to PyCharm so it can execute code commands
tello.connect()

# assigning read_battery variable to tello's get battery command
read_battery = tello.get_battery()

# prints battery percentage of battery in tello
print(read_battery)

