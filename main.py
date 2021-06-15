import turtle
from turtle import *

from character import Character

# * STYLE VARIABLES
BGCOLOR = "#0E0F1E"
BUTTONBG = "#1F3049"


# * SCREEN SIZE
WIDTH = 900
HEIGHT = 600

# * SCREN INIT
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgpic("./assets/images/bg.png")


# * WELCOME SCREEN START BUTTON
FONT_SIZE = 36
FONT = ('Courier', FONT_SIZE, 'bold')

start_button = Turtle()
start_button.hideturtle()
start_button.pencolor("white")
start_button.color(BUTTONBG)
start_button.shape('square')
start_button.shapesize(stretch_wid=5, stretch_len=20)
start_button.penup()
start_button.goto(0, 0)
start_button.stamp()
start_button.color('white')
# center vertically based on font size
start_button.goto(0, 0 - FONT_SIZE/2 - 10)
start_button.write("START", align='center', font=FONT)

# * Start button click


def test():
    print("sdadadadad")


def onClick(clickedX, clickedY):
    character = Character()
    if(clickedX > -200 and clickedX < 200 and clickedY > -50 and clickedY < 50):
        screen.clear()
        screen.bgcolor(BGCOLOR)
        character = Turtle()
        character.shape("square")
        character.color("white")

    screen.listen()
    screen.onkeypress(lambda: character.sety(character.ycor() + 10), "w")
    screen.onkeypress(lambda: character.sety(character.ycor() - 10), "s")
    screen.onkeypress(lambda: character.setx(character.xcor() - 10), "a")
    screen.onkeypress(lambda: character.setx(character.xcor() + 10), "d")


onscreenclick(onClick)


# * GAME MAIN FUNCTION
def main():
    screen.update()


while True:
    main()
