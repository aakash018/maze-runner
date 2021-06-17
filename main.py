from turtle import *

import maze.main as mazeMaker
import utils.makeButton as makeButton

# * STYLE VARIABLES
BGCOLOR = "#0E0F1E"
BUTTONBG = "#1F3049"


# * SCREEN SIZE
WIDTH = 900
HEIGHT = 600

# * SCREN INIT
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BGCOLOR)
screen.bgpic("./assets/images/bg.png")


# * WELCOME SCREEN START BUTTON
FONT_SIZE = 36
FONT = ('Courier', FONT_SIZE, 'bold')

makeButton.button(FONT_SIZE, "START", 0, 0, 5, 20)

# * WELCOM SCREEN ABOUT US BUTTON
makeButton.button(FONT_SIZE - 20, "About", 0, -100)


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

    if((nextXforCharacter, nextYforCharacter) == mazeMaker.getEndCords()):
        screen.clear()
        screen.bgcolor(BGCOLOR)
        winingMessage = Turtle()
        winingMessage.hideturtle()
        winingMessage.color("white")
        winingMessage.write("You escaped the maze...",
                            align="center", font=FONT)
        makeButton.button(FONT_SIZE - 20, "RESTART NEW MAZE", 0, -150, 1.5, 20)

        onscreenclick(onRestartClick)

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
def startGame():
    screen.clear()
    screen.bgcolor(BGCOLOR)
    mazeMaker.drawMaze()
    character = Turtle()
    character.shape("square")
    character.color("white")
    character.penup()
    # character.goto(-277.5, 302.5 - 25)
    character.goto(mazeMaker.getStartCords())
    screen.onkeypress(lambda: moveUp(character), "w")
    screen.onkeypress(lambda: moveDown(character), "s")
    screen.onkeypress(lambda: moveLeft(character), "a")
    screen.onkeypress(lambda: moveRight(character), "d")
    screen.listen()


def onClick(clickedX, clickedY):
    FONT = ('Courier', 20, 'bold')
    COLOR = "white"

    # ? IF ABOUT ME IS PRESSES
    if(clickedX > -100 and clickedX < 101 and clickedY > -116 and clickedY < -85):
        screen.clear()
        screen.bgcolor(BGCOLOR)
        # name1 = Turtle()
        # name1.hideturtle()
        # name1.color(COLOR)
        # name1.write("Aakash Khanal", align='center', font=FONT)

        # name2 = Turtle()
        # name2.hideturtle()
        # name2.color(COLOR)
        # name2.write("Manish", align='center', font=FONT)

    print(clickedX, clickedY)
    # ? IF START BUTTON IS PRESSES
    if(clickedX > -200 and clickedX < 200 and clickedY > -50 and clickedY < 50):
        startGame()


def onRestartClick(clickedX, clickedY):
    if(clickedX > -200 and clickedX < 205 and clickedY > -166 and clickedY < -134):
        print("clicked")
        mazeMaker.resetWallsCords()
        mazeMaker.resetSpacesCords()
        startGame()


onscreenclick(onClick)


# * GAME MAIN FUNCTION
def main():
    screen.update()


while True:
    main()
