from . import *

class GameObject(turtle.Turtle):
	def __init__(self, shape, color, scalefactor):
		super().__init__()
		self.shape(shape)
		self.shapesize(stretch_wid=scalefactor, stretch_len=scalefactor)
		self.color(color)
		self.pu()
		self.speed(0)