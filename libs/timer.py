import time
import turtle


def timer(COLOR):
    timer_text = turtle.Turtle()
    timer_text.hideturtle()
    timer_text.color(COLOR)
    timer_text.goto(0, 100)

    start = time.time()
    while True:
        timer_text.clear()
        timer_text.write(f'{int(time.time() - start)} sec',
                         font=("Courier", 30))
