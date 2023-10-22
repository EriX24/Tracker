from turtle import Turtle, Screen
from secrets import code
import pygame

# Init Pygame
pygame.init()

# Get how many projectiles the user wants to send.
is_int = False
use = False
while not is_int:
    try:
        projectiles = int(input("How many projectiles do you want to send? "))
        if projectiles < 1:
            print("It can not be 0 or lower.")
        elif projectiles == code:
            use = True
        elif projectiles > 50:
            print("It can not be above 50.")
        else:
            is_int = True
    except ValueError:
        print("Please input a number.")

# "display" turtle code
display = Turtle(visible=False)
display.penup()
display.goto(200, 150)
display.color("white")
display.write(projectiles, move=False, align='left', font=('Arial', 20, 'normal'))

# "aim" tutle code
aim = Turtle()
aim.shape("triangle")
aim.color("red")
aim.shapesize(stretch_wid=0.5, stretch_len=0.5)
aim.penup()
aim.speed(1000000000000000000000)

# "screen" code
screen = Screen()
screen.bgpic('pictures/background.png')
screen.update()
screen.setup(500, 400)
screen.title("Tracker")


# Functions for moving
def up():
    aim.setheading(90)
    aim.forward(20)


def down():
    aim.setheading(270)
    aim.forward(20)


def left():
    aim.setheading(180)
    aim.forward(20)


def right():
    aim.setheading(0)
    aim.forward(20)


# Function for launching projectiles
def deploy():
    global projectiles
    # Made the "aborted" to be a number above 50
    if projectiles == 737:
        print("You already aborted the mission!!!")
    elif projectiles > 0:
        # Reduce projectiles
        projectiles -= 1
        # Make the explosion
        aim.dot(25, (0, 0, 0))
        aim.dot(10, "yellow")
        # Tell the user the result
        ping = pygame.mixer.Sound('sounds/ping.mp3')
        ping.play()
        print("Deployed!!!")
        # Code for the display, again
        display.clear()
        display.write(projectiles, move=False, align='left', font=('Arial', 20, 'normal'))
    elif projectiles <= 0:
        print("You have no more projectiles.")


# ???
def deploy_other():
    global use
    if use:
        # Change data for "use"
        use = False
        # Make the BOOM
        aim.dot(75, (0, 0, 0))
        aim.dot(30, "yellow")
        aim.dot(10, "red")
        # Tell the user the result
        boom = pygame.mixer.Sound('sounds/boom.mp3')
        boom.play()
        print("BOOM!!!")
    else:
        pass


# Abort the mission!!
def abort():
    global projectiles, use
    if projectiles != 737 and projectiles > 0:
        # Delete all projectiles
        projectiles = 737
        # Clear all effects
        display.clear()
        aim.clear()
        # Change the background and size of screen
        screen.bgpic('pictures/abort.png')
        screen.update()
        screen.setup(700, 350)
        # ???
        use = False
        # Hide aim
        aim.hideturtle()
        # Tell the user
        print("Aborted mission!!!")
        alarm = pygame.mixer.Sound('sounds/alarm.wav')
        alarm.play()
    elif projectiles == 737:
        print("You already aborted the mission!!!")
    elif projectiles <= 0:
        print("You already ran out of projectiles! There is no need to abort the mission!")


# More "screen" code
screen.listen()
screen.onkey(up, "w")  # This will call the up function if the "W" arrow key is pressed
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(deploy, "e")
screen.onkey(deploy_other, "q")
screen.onkey(abort, "space")

# The "mainloop"
screen.mainloop()
