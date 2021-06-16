from turtle import *

import maze.main as mazeMaker

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


# * Character Moment Functions

def moveUp(character):
    nextXforCharacter = character.xcor()
    nextYforCharacter = character.ycor() + 25
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
    else:
        return


def moveDown(character):
    nextXforCharacter = character.xcor()
    nextYforCharacter = character.ycor() - 25
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
    else:
        return


def moveLeft(character):
    nextXforCharacter = character.xcor() - 25
    nextYforCharacter = character.ycor()
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
    else:
        return


def moveRight(character):
    nextXforCharacter = character.xcor() + 25
    nextYforCharacter = character.ycor()
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
    else:
        return


# * Start button clic


def onClick(clickedX, clickedY):
    if(clickedX > -200 and clickedX < 200 and clickedY > -50 and clickedY < 50):
        screen.clear()
        screen.bgcolor(BGCOLOR)
        mazeMaker.drawMaze()
        character = Turtle()
        character.shape("square")
        character.color("white")
        character.penup()
        character.goto(-277.5, 302.5 - 25)
        character.pendown()
        screen.onkeypress(lambda: moveUp(character), "w")
        screen.onkeypress(lambda: moveDown(character), "s")
        screen.onkeypress(lambda: moveLeft(character), "a")
        screen.onkeypress(lambda: moveRight(character), "d")
        screen.listen()


onscreenclick(onClick)


# * GAME MAIN FUNCTION
def main():
    screen.update()


while True:
    main()
