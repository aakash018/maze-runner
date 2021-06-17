from turtle import *

BUTTONBG = "#1F3049"


def button(FONT_SIZE, TEXT, cordsX, cordsY, width=1.5, height=10):
    button = Turtle()
    button.hideturtle()
    button.pencolor("white")
    button.color(BUTTONBG)
    button.shape('square')
    button.shapesize(stretch_wid=width, stretch_len=height)
    button.penup()
    button.goto(cordsX,  cordsY)
    button.stamp()
    button.color('white')
    # center vertically based on font size
    button.goto(cordsX, cordsY - (FONT_SIZE)/2 - 8)
    button.write(TEXT, align='center',
                 font=('Courier', FONT_SIZE))
