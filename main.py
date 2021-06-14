from turtle import *

# * SCREEN SIZE
WIDTH = 900
HEIGHT = 600

# * SCREN INIT
screen = Screen()


# * WELCOME SCREEN START BUTTON
FONT_SIZE = 36
FONT = ('Courier', FONT_SIZE, 'bold')

textbox = Turtle()
textbox.hideturtle()
textbox.pencolor("white")
textbox.color('#1F3049')
textbox.shape('square')
textbox.shapesize(stretch_wid=5, stretch_len=20)
textbox.penup()
textbox.goto(0, 0)
textbox.stamp()
textbox.color('white')
textbox.goto(0, 0 - FONT_SIZE/2 - 10)  # center vertically based on font size
textbox.write("START", align='center', font=FONT)


# * GAME MAIN FUNCTION
def main():
    screen.setup(WIDTH, HEIGHT)
    screen.bgpic("./assets/images/bg.png")


while True:
    main()
