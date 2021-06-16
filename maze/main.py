from random import randrange, shuffle

from .MazeRunner.GameObject import GameObject
from .MazeRunner.MazeGenerator import MazeGenerator

# Grid generator
generator = MazeGenerator()
generator.write('Block.txt')

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

# * Wall Cordinate
wallsCordsInScreen = []
spacesCordsInScreen = []

# Screen stufss
# screen = turtle.Screen()
# screen.title(TITLE)
# screen.setup(WINWIDTH, WINHEIGHT)

# Read generated grid from MazeGenerator
f = open('Block.txt', 'r')
grid = f.readlines()


def drawMaze():
    # Game Objects
    wall = GameObject("square", BUTTONBG, 1)
    space = GameObject("square", BGCOLOR, 1)
    start = GameObject("square", "red", 1)
    stop = GameObject("square", "green", 1)
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
            if(grid[i][j] == "P"):
                stop.stamp()
                spacesCordsInScreen.append((space.xcor(), space.ycor()))
    wall.hideturtle()
    space.hideturtle()
    start.hideturtle()
    stop.hideturtle()


def getWallsCords():
    return wallsCordsInScreen


def getSpacesCords():
    return spacesCordsInScreen


if __name__ == '__main__':
    drawMaze()