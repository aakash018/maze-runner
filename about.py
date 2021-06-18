import turtle

import utils.makeButton as makeButton

FONT_SIZE = 20


def write(obj, Text, cordX, cordY, FontSize=FONT_SIZE):
    FONT = ('Courier', FontSize, 'bold')
    obj.color("white")
    obj.hideturtle()
    obj.penup()
    obj.goto(cordX, cordY)
    obj.write(
        Text, font=FONT)


def aboutPage():
    makeButton.button(20, "BACK", 550, 330)

    lore = turtle.Turtle()
    write(lore, "This is a simple game, based a little on the movie “MAZE RUNNER”,", -600, 300)
    write(lore, "created for ARC PythonBytes 2021: Fun with Animation competition", -600, 270)

    maze = turtle.Turtle()
    write(maze, "It uses “Recursive Backtracker Maze Generation” for the generation", -600, 200)
    write(maze, "of every in-game mazes. Every maze generated will be different with", -600, 170)
    write(maze, "only one end route and no any dead ends.", -600, 140)

    enjoy = turtle.Turtle()
    write(enjoy, "Enjoy the game....", -600, 70, FONT_SIZE + 10)

    creator = turtle.Turtle()
    write(creator, "Created By:", -600, 0, FONT_SIZE + 5)
    write(creator, "Aakash Khanal", -600, -40, FONT_SIZE)
    write(creator, "Bibek Chand", -600, -80, FONT_SIZE)
    write(creator, "Bigyan Dahal", -600, -120, FONT_SIZE)
    write(creator, "Manish Gyawali", -600, -160, FONT_SIZE)

    write(creator, "Code at: https://github.com/aakash018/maze-runner", -
          600, -250, FONT_SIZE)
