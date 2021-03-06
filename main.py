import datetime
import threading
import winsound
from random import shuffle

from about import aboutPage

try:
    import winsound
except ModuleNotFoundError:
    import os

from turtle import *

from playsound import playsound

import help
import libs.timer as timer
import maze.main as mazeMaker
import utils.makeButton as makeButton

# * STYLE VARIABLES
BGCOLOR = "#0E0F1E"
BUTTONBG = "#1F3049"
PLAYERSIZE = 25

# * SCREEN SIZE
WIDTH = 1280
HEIGHT = 720

gameMode = ""

# * SCREN INIT
screen = Screen()
# screen.setup(WIDTH, HEIGHT)
screen.title("Maze Runner")
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.tracer(0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)


FONT_SIZE = 36
FONT = ('Courier', FONT_SIZE, 'bold')

# timer
timerCounter = 0
timerObj = Turtle()
timerObj.pu()
timerObj.color("black")
timerObj.goto(500, 270)
timerObj.color("white")
timerObj.hideturtle()

timerRunning = True


def timer():
    def f():
        global timerCounter
        if timerRunning:
            timerObj.clear()
            timerObj.write("Timer : " + str(datetime.timedelta(seconds=timerCounter)),
                           align="center", font=('Courier', 20, 'bold'))
            timerCounter += 1
            screen.ontimer(f, 1000)
    f()


def homeScreen():
    # * Stop Previous
    winsound.PlaySound(None, winsound.SND_PURGE)

    # * Sound
    winsound.PlaySound("./assets/music/theme.wav",
                       winsound.SND_LOOP + winsound.SND_ASYNC)

    screen.bgcolor(BGCOLOR)
    screen.bgpic("./assets/images/bg3.png")
    # * WELCOME SCREEN START BUTTON

    makeButton.button(FONT_SIZE - 10, "Single Player", 0, 0, 4, 20)

    makeButton.button(FONT_SIZE - 10, "Multiplayer", 0, -100, 4, 20)

    # * WELCOM SCREEN ABOUT US BUTTON
    makeButton.button(FONT_SIZE - 20, "Help", 0, -200)
    makeButton.button(FONT_SIZE - 20, "About", 0, -250)
    makeButton.button(FONT_SIZE - 20, "Quit", 0, -300)


homeScreen()
# * Sound
try:
    winsound.PlaySound("./assets/music/theme.wav",
                       winsound.SND_LOOP + winsound.SND_ASYNC)
except:
    os.system("aplay ./assets/music/theme.wav &")


# * Character Moment Functions

def trapPlayer(char, nextX, nextY):
    if((nextX, nextY) in mazeMaker.getTrap1Cords()):
        playsound("./assets/music/blue_trap.wav", False)
        mazeMaker.setTrap1Cords((nextX, nextY))
        char.goto(mazeMaker.getStartCords())
    if((nextX, nextY) in mazeMaker.getTrap2Cords()):
        playsound("./assets/music/pink_trap.wav", False)
        mazeMaker.setTrap2Cords((nextX, nextY))
        spaceCords = mazeMaker.getSpacesCords()
        shuffle(spaceCords)
        char.goto((spaceCords[0][0], spaceCords[0][1]))


def set_interval(func, sec):
    def func_wrap():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrap)
    t.start()
    return t

# * Character Moment Functions


def moveUp(character):
    nextXforCharacter = character.xcor()
    nextYforCharacter = character.ycor() + PLAYERSIZE
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
        trapPlayer(character, nextXforCharacter, nextYforCharacter)
    else:
        return


def moveDown(character, playerType=""):
    global gameMode, timerRunning, timerCounter
    nextXforCharacter = character.xcor()
    nextYforCharacter = character.ycor() - 25
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    # ? Game End Logic

    if((nextXforCharacter, nextYforCharacter) == mazeMaker.getEndCords()):
        global timerCounter
        timerRunning = False
        timerObj.clear()
        savedTimer = timerCounter
        timerCounter = 0
        conversion = datetime.timedelta(seconds=savedTimer)
        converted_time = str(conversion)
        screen.clear()
        screen.bgcolor(BGCOLOR)
        playsound("./assets/music/end_laugh.mp3", False)
        if(gameMode == "single"):
            winingMessage = Turtle()
            winingMessage.hideturtle()
            winingMessage.color("white")
            winingMessage.write("You escaped the maze...",
                                align="center", font=FONT)
            winingMessage.pu()
            winingMessage.goto(0, -80)
            winingMessage.write(f'Time taken is {converted_time}',
                                align="center", font=('Courier', FONT_SIZE - 10, 'bold'))
            makeButton.button(
                FONT_SIZE - 20, "RESTART NEW MAZE", 0, -150, 1.5, 20)

            makeButton.button(FONT_SIZE - 20, "Home", 0, -200, 1.5, 20)

        if(gameMode == "multi"):
            if(playerType == "player1"):
                winingMessage = Turtle()
                winingMessage.hideturtle()
                winingMessage.color("white")
                winingMessage.write("Yellow escaped the maze and WON...",
                                    align="center", font=FONT)
                makeButton.button(
                    FONT_SIZE - 20, "RESTART NEW MAZE", 0, -150, 1.5, 20)
                makeButton.button(FONT_SIZE - 20, "Home", 0, -200, 1.5, 20)

            if(playerType == "player2"):
                winingMessage = Turtle()
                winingMessage.hideturtle()
                winingMessage.color("white")
                winingMessage.write("Purple escaped the maze and WON...",
                                    align="center", font=FONT)
                makeButton.button(
                    FONT_SIZE - 20, "RESTART NEW MAZE", 0, -150, 1.5, 20)
                makeButton.button(FONT_SIZE - 20, "Home", 0, -200, 1.5, 20)

        onscreenclick(onGameEndScreenClick)

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
    else:
        return


def moveLeft(character):
    nextXforCharacter = character.xcor() - PLAYERSIZE
    nextYforCharacter = character.ycor()
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
        trapPlayer(character, nextXforCharacter, nextYforCharacter)
    else:
        return


def moveRight(character):
    nextXforCharacter = character.xcor() + PLAYERSIZE
    nextYforCharacter = character.ycor()
    # print(mazeMaker.getWallsCords())
    # print((nextXforCharacter + 0.5, nextYforCharacter + 0.5))

    if((nextXforCharacter, nextYforCharacter) in mazeMaker.getSpacesCords()):
        character.setx(nextXforCharacter)
        character.sety(nextYforCharacter)
        trapPlayer(character, nextXforCharacter, nextYforCharacter)
    else:
        return

# * Start button clic


def startSingleGame():
    global timerCounter
    screen.clear()
    screen.tracer(0)
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('./assets/music/in_game_music.wav',
                       winsound.SND_LOOP + winsound.SND_ASYNC)
    screen.bgcolor(BGCOLOR)
    makeButton.button(20, "EXIT", 500, 330)
    onscreenclick(onHelpClick)
    mazeMaker.resetTrapCords()
    mazeMaker.resetSpacesCords()
    mazeMaker.resetWallsCords()
    mazeMaker.drawMaze()
    character = Turtle()
    character.shape("square")
    character.color("white")
    character.penup()
    # character.goto(-277.5, 302.5 - 25)
    character.goto(mazeMaker.getStartCords())

    # timer
    timerRunning = True
    timer()

    screen.onkeypress(lambda: moveUp(character), "w")
    screen.onkeypress(lambda: moveDown(character), "s")
    screen.onkeypress(lambda: moveLeft(character), "a")
    screen.onkeypress(lambda: moveRight(character), "d")
    screen.listen()


def startMultiGame():
    screen.clear()
    screen.tracer(0)

    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('./assets/music/in_game_music.wav',
                       winsound.SND_LOOP + winsound.SND_ASYNC)
    screen.bgcolor(BGCOLOR)
    makeButton.button(20, "EXIT", 500, 330)
    onscreenclick(onHelpClick)
    mazeMaker.resetTrapCords()
    mazeMaker.resetSpacesCords()
    mazeMaker.resetWallsCords()
    mazeMaker.drawMaze()

    character1 = Turtle()
    character1.shape("square")
    character1.color("yellow")
    character1.penup()

    character2 = Turtle()
    character2.shape("square")
    character2.color("purple")
    character2.penup()
    # character.goto(-277.5, 302.5 - 25)
    character1.goto(mazeMaker.getStartCords())
    character2.goto(mazeMaker.getStartCords())

    screen.onkeypress(lambda: moveUp(character1), "w")
    screen.onkeypress(lambda: moveDown(character1, "player1"), "s")
    screen.onkeypress(lambda: moveLeft(character1), "a")
    screen.onkeypress(lambda: moveRight(character1), "d")

    screen.onkeypress(lambda: moveUp(character2), "Up")
    screen.onkeypress(lambda: moveDown(character2, "player2"), "Down")
    screen.onkeypress(lambda: moveLeft(character2), "Left")
    screen.onkeypress(lambda: moveRight(character2), "Right")
    screen.listen()


def onClick(clickedX, clickedY):
    global gameMode, timerRunning, timerCounter
    print(clickedX, clickedY)
    # ? IF MULTI PLAYER ME IS PRESSES
    if(clickedX > -200 and clickedX < 202 and clickedY > -144 and clickedY < -60):
        gameMode = "multi"
        startMultiGame()

    # ? IF SInGLE BUTTON IS PRESSES
    if(clickedX > -200 and clickedX < 200 and clickedY > -50 and clickedY < 50):
        gameMode = "single"
        timerRunning = True
        a = 0
        startSingleGame()

    # ? IF Help BUTTON IS PRESSED
    if(clickedX > -100 and clickedX < 100 and clickedY > -218 and clickedY < -184):
        screen.clear()
        screen.tracer(0)
        screen.bgcolor(BGCOLOR)
        help.helpPage()

        onscreenclick(onHelpClick)

    # ? If ABOUT BUTTON IS PRESSED
    if(clickedX > -100 and clickedX < 100 and clickedY > -267 and clickedY < -235):
        screen.clear()
        screen.tracer(0)
        screen.bgcolor(BGCOLOR)
        aboutPage()

        onscreenclick(onHelpClick)

    # ? On Quit
    if(clickedX > -100 and clickedX < 100 and clickedY > -316 and clickedY < -285):
        screen.bye()


def onGameEndScreenClick(clickedX, clickedY):
    global timerRunning, timerCounter
    # * HOME
    timerRunning = False
    timerObj.clear()
    timerCounter = 0
    if(clickedX > -200 and clickedX < 205 and clickedY > -280 and clickedY < -180):
        screen.clear()
        screen.tracer(0)
        homeScreen()
        onscreenclick(onClick)

    if(clickedX > -200 and clickedX < 205 and clickedY > -166 and clickedY < -134):
        print(gameMode)
        if(gameMode == "single"):
            # mazeMaker.resetWallsCords()
            # mazeMaker.resetSpacesCords()
            # mazeMaker.resetTrapCords()
            timerRunning = True
            startSingleGame()
        if(gameMode == "multi"):
            # mazeMaker.resetWallsCords()
            # mazeMaker.resetSpacesCords()
            # mazeMaker.resetTrapCords()
            startMultiGame()


def onHelpClick(clickedX, clickedY):
    global timerRunning, timerCounter
    print(clickedX, clickedY)
    if(clickedX > 400 and clickedX < 602 and clickedY > 315 and clickedY < 350):
        timerRunning = False
        timerObj.clear()
        timerCounter = 0
        screen.clear()
        screen.tracer(0)
        homeScreen()
        onscreenclick(onClick)


onscreenclick(onClick)


# * GAME MAIN FUNCTION
def main():
    screen.update()


while True:
    main()
