import datetime
import time
from turtle import *

screen = Screen()

a = 0
timerObj = Turtle()
timerObj.pu()
timerObj.goto(500, 270)
timerObj.color("white")
timerObj.hideturtle()

timerRunning = True


def timer():
    def f():
        global a, count, timerRunning
        if timerRunning:
            if a == 2:
                timerRunning = False
                timerObj.clear()
            else:
                timerObj.clear()
                timerObj.write("Timer : " + str(datetime.timedelta(seconds=a)),
                               align="center", font=('Courier', 20, 'bold'))
                a += 1
                screen.ontimer(f, 1000)
    f()


timer()

done()
