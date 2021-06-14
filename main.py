import turtle
from turtle import *

# * SCREEN SIZE
WIDTH = 900
HEIGHT = 600

# * SCREN INIT
screen = Screen()


# * WELCOME SCREEN START BUTTON
FONT_SIZE = 36
FONT = ('Courier', FONT_SIZE, 'bold')

start_button = Turtle()
start_button.hideturtle()
start_button.pencolor("white")
start_button.color('#1F3049')
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


def onClick(clickedX, clickedY):
    if(clickedX > -200 and clickedX < 200 and clickedY > -50 and clickedY < 50):
        print("button is being clicked")


onscreenclick(onClick)


# * GAME MAIN FUNCTION
def main():
    screen.setup(WIDTH, HEIGHT)
    screen.bgpic("./assets/images/bg.png")


while True:
    main()
