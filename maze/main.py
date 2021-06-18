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

# trap coordinates
trap1Cords = []
trap2Cords = []

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
    # trap debug view
    trap1 = GameObject("square", "blue", 1)
    trap2 = GameObject("square", "purple", 1)

    # trap game mode view
    # trap1 = GameObject("square", BGCOLOR, 1)
    # trap2 = GameObject("square", BGCOLOR, 1)
    for i in range(GRIDHEIGHT):
        for j in range(GRIDWIDTH):
            wall.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            space.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            start.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            stop.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            trap1.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            trap2.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
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
            if(grid[i][j] == "T"):
                trap1.stamp()
                spacesCordsInScreen.append((space.xcor(), space.ycor()))
                trap1Cords.append((space.xcor(), space.ycor()))
            if(grid[i][j] == "U"):
                trap2.stamp()
                spacesCordsInScreen.append((space.xcor(), space.ycor()))
                trap2Cords.append((space.xcor(), space.ycor()))

    wall.hideturtle()
    space.hideturtle()
    start.hideturtle()
    stop.hideturtle()
    trap1.hideturtle()
    trap2.hideturtle()


def resetTrapCords():
    trap1Cords.clear()
    trap2Cords.clear()


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


def getTrap1Cords():
    return trap1Cords


def getTrap2Cords():
    return trap2Cords


def setTrap1Cords(cords):
    trap1Cords.remove(cords)


def setTrap2Cords(cords):
    trap2Cords.remove(cords)


if __name__ == '__main__':
    drawMaze()
