from random import shuffle, randrange
import turtle

from MazeRunner.GameObject import GameObject
from MazeRunner.MazeGenerator import MazeGenerator

# Grid generator
generator = MazeGenerator()
generator.write('Block.txt')

# Global vars

WINWIDTH = 625
WINHEIGHT = 625
TITLE = "MazeRunner"

GRIDWIDTH = 25
GRIDHEIGHT = 25
GRIDXORIG = -302.5
GRIDYORIG = 302.5

SCALE = 25

# Screen stufss
screen = turtle.Screen()
screen.title(TITLE)
screen.setup(WINWIDTH, WINHEIGHT)

# Game Objects
wall = GameObject("square", "black", 1)
space = GameObject("square", "white", 1)

# Read generated grid from MazeGenerator
f = open('Block.txt', 'r')
grid = f.readlines()

for i in range(GRIDHEIGHT):
    for j in range(GRIDWIDTH):
        wall.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
        space.goto(GRIDXORIG + (j*SCALE), GRIDYORIG - (i*SCALE))
        if(grid[i][j] == "X"):
            wall.stamp()
        if(grid[i][j] == " "):
            space.stamp()

turtle.done()