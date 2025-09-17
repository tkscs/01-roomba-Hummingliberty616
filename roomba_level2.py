# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(10,000,000,000,000,000,000,000,000,000,000,000,000,
000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here

# Functions

#Drawing shapes
def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for i in range (number_of_sides):
        forward(50)
        right(angle)

for i in range (3):
    forward(560)
    left(90)
    forward(40)
    left(90)
    forward(560)
    right(90)
    forward(40)
    right(90)
    forward(560)
    left(90)
    forward(40)
    left(90)
    forward(560)
    right(90)
    forward(40)
    right(90)
    forward(560)
    left(90)
    forward(40)
    left(90)
    forward(560)
    right(90)
    forward(40)
    right(90)
#Part 2
forward(560)
left(90)
forward(40)
left(90)
forward(560)
# End your code here
###
 
window.exitonclick()

