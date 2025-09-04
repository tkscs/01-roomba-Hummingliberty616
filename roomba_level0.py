# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Winston <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
forward(150)
left(90)
forward(40)
left(90)
forward(150)
 
 
# End your code here
###
 
window.exitonclick()
