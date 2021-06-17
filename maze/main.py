from random import randrange, shuffle

from .MazeRunner.GameObject import GameObject
from .MazeRunner.MazeGenerator import MazeGenerator

# Global vars

WINWIDTH = 625
WINHEIGHT = 625
TITLE = "MazeRunner"
BGCOLOR = "#0E0F1E"
BUTTONBG = "#1F3049"

GRIDWIDTH = 25
GRIDHEIGHT = 25
GRIDXORIG = -302.5
GRIDYORIG = 302.5

SCALE = 25


# * Start End Cords
startCords = None
endBlockCords = None
# Read generated grid from MazeGenerator

# * Wall Cordinate
wallsCordsInScreen = []
spacesCordsInScreen = []


# Grid generator
generator = MazeGenerator()


def drawMaze():
    generator.write('Block.txt')
    f = open('Block.txt', 'r')
    grid = f.readlines()
    global startCords, endBlockCords
    # Game Objects
    wall = GameObject("square", BUTTONBG, 1)
    space = GameObject("square", BGCOLOR, 1)
    start = GameObject("square", "#F9553E", 1)
    stop = GameObject("square", "#43DA6D", 1)
    for i in range(GRIDHEIGHT):
        for j in range(GRIDWIDTH):
            wall.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            space.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            start.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            stop.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            if(grid[i][j] == "X"):
                wall.stamp()
                wallsCordsInScreen.append((wall.xcor(), wall.ycor()))
            if(grid[i][j] == " "):
                space.stamp()
                spacesCordsInScreen.append((space.xcor(), space.ycor()))
            if(grid[i][j] == "S"):
                start.stamp()
                spacesCordsInScreen.append((space.xcor(), space.ycor()))
                startCords = (start.xcor(), start.ycor())
            if(grid[i][j] == "E"):
                stop.stamp()
                spacesCordsInScreen.append((space.xcor(), space.ycor()))
                endBlockCords = (stop.xcor(), stop.ycor())

    wall.hideturtle()
    space.hideturtle()
    start.hideturtle()
    stop.hideturtle()


def resetWallsCords():
    wallsCordsInScreen.clear()


def resetSpacesCords():
    spacesCordsInScreen.clear()


def getWallsCords():
    return wallsCordsInScreen


def getSpacesCords():
    return spacesCordsInScreen


def getStartCords():
    return startCords


def getEndCords():
    return endBlockCords


if __name__ == '__main__':
    drawMaze()
