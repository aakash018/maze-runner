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

# Screen stufss
# screen = turtle.Screen()
# screen.title(TITLE)
# screen.setup(WINWIDTH, WINHEIGHT)

# Game Objects

# Read generated grid from MazeGenerator
f = open('Block.txt', 'r')
grid = f.readlines()


def drawMaze():
    wall = GameObject("square", BUTTONBG, 1)
    space = GameObject("square", BGCOLOR, 1)
    for i in range(GRIDHEIGHT):
        for j in range(GRIDWIDTH):
            wall.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            space.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
            if(grid[i][j] == "X"):
                wall.stamp()
                wallsCordsInScreen.append((wall.xcor(), wall.ycor()))
            if(grid[i][j] == " "):
                space.stamp()
    # turtle.done()


def getWallsCords():
    return wallsCordsInScreen


if __name__ == '__main__':
    drawMaze()
