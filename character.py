import turtle


class Character:
    def __init__(self) -> None:
        self.character = turtle.Turtle()

    def draw(self, xCord=0, yCord=0):
        self.character.color("white")
        # self.character.shape("square")
        self.character.shapesize(stretch_wid=2, stretch_len=2)
        self.character.penup()
        self.character.goto(xCord, yCord)
        self.character.stamp()

    def moveLeft(self, distance):
        y = self.character.ycor()
        y += distance
        self.character.forward(90)

    def moveRight(self, distance):
        y = self.character.ycor()
        y -= distance
        self.character.sety(y)

    def moveDown(self, distance):
        x = self.character.xcor()
        x -= distance
        self.character.sety(x)

    def moveUp(self, distance):
        x = self.character.xcor()
        x += distance
        self.character.sety(x)
