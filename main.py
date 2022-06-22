from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # tracer(0) turns off the animation
screen.listen()
scoreboard = Scoreboard()

# Create the left and right paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Get the paddles to respond to the users' key presses
screen.onkeypress(key="Up", fun=r_paddle.paddle_up)
screen.onkeypress(key="Down", fun=r_paddle.paddle_down)

screen.onkeypress(key="w", fun=l_paddle.paddle_up)
screen.onkeypress(key="s", fun=l_paddle.paddle_down)

ball = Ball()

game_is_on = True
while game_is_on:
	screen.update()  # updates the screen when tracer(0) is in use
	ball.move()
	time.sleep(ball.move_speed)

	# Detect ball collision with wall
	if ball.ycor() > 285 or ball.ycor() < -285:
		ball.wall_bounce()

	# Detect collision with paddles
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.paddle_bounce()

	# Detect R paddle misses
	if ball.xcor() > 380:
		time.sleep(1)
		ball.reset_position()
		scoreboard.l_point()

	# Detect L paddle misses
	if ball.xcor() < -380:
		time.sleep(1)
		ball.reset_position()
		scoreboard.r_point()


screen.exitonclick()
