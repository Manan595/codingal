import turtle
import time
def forward():
    turtle.forward(move_speed)

def backward():
    turtle.backward(move_speed)

def left():
    turtle.left(move_speed)

def right():
    turtle.right(move_speed)

screen=turtle.Screen()
screen.setup(500,500)

screen.bgpic('dancefloor.jpg')
screen.addshape('robot-icon-small.gif')
screen.turtle('robot-icon-small.gif')
move_speed=20
turn_speed=50

turtle.penup()
turtle.speed(0)
turtle.home()

time.sleep(1)

for i in range(18):
    left()
for i in range(10):
    forward
time.sleep(0.5)

for i in range(10):
    backward()
time.sleep(0.5)

for i in range(18):
    right()