import turtle
from os import makedirs

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


def helpPage():

    makeButton.button(20, "BACK", 500, 330)

    lore = turtle.Turtle()
    write(lore, "You are traped inside a maze by some unknown power. Try", -600, 330)
    write(lore, "to escape the maze and survive. Beware there may be", -600, 300)
    write(lore, "traps in your way you can’t see.", -600, 270)

    title = turtle.Turtle()
    write(title, "HOW TO PLAY", -600, 200, FONT_SIZE + 10)

    traps = turtle.Turtle()
    write(traps, "You can't see traps and there are two types of it:", -600, 200 - 20)
    write(traps, "The Mist: It will teleport you to any point in the map.", -600, 170 - 20)
    write(traps, "The Return: Takes you the the starting point", -600, 140 - 20)

    single = turtle.Turtle()
    write(single, "Single Player", -600, 100 - 30 - 20, FONT_SIZE + 10)
    write(single, "Your goal is to reach to the green point at bottom right corner.", -
          600, 70 - 30 - 20, FONT_SIZE)
    write(single, "Use W, A, S, D for controls", -600, 40 - 60 - 20, FONT_SIZE)

    multi = turtle.Turtle()
    write(multi, "Multi Player", -600, -120, FONT_SIZE + 10)
    write(multi, "Your goal is to reach to the green point at bottom right corner.", -600, -180, FONT_SIZE)
    write(multi, "Controls: W, A, S, D - Yellow", -600, -210, FONT_SIZE)
    write(multi, "Up, Down, Left, Right arrow - Purple", -450, -240, FONT_SIZE)
    write(multi, "Try to beat your opponent for survival", -600, -270, FONT_SIZE)
