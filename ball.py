from turtle import Turtle


class Ball(Turtle):
	def __init__(self):
		super().__init__("circle")
		self.color("white")
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.move_speed = 0.1

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def wall_bounce(self):
		self.y_move *= -1

	def paddle_bounce(self):
		self.x_move *= -1
		self.move_speed *= 0.8  # decrease move_speed to decrease time btwn screen updates (i.e. increase ball speed)

	def reset_position(self):
		self.goto(0, 0)
		self.move_speed = 0.1  # reset move_speed once position resets
		self.x_move *= -1
