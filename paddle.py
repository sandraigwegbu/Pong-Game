from turtle import Turtle


class Paddle(Turtle):
	# Create the paddles
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.turtlesize(stretch_len=5)
		self.penup()
		self.goto(position)
		self.setheading(90)

	# Move the paddles
	def paddle_up(self):
		self.forward(20)

	def paddle_down(self):
		self.backward(20)
