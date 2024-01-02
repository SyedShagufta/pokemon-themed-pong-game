import random
from turtle import Turtle, Screen
import time
from ball import Ball
from paddle import Paddle
from score_board import Scoreboard

screen = Screen()

images = [
    "images/bg-1.png",
    "images/bg-2.png",
    "images/bg-3.png",
    "images/bg-4.png",
    "images/bg-5.png",
    "images/bg-6.png",
]

screen.bgpic(random.choice(images))
screen.title("Pong Game by Sofia 🎯💖")
screen.setup(width=800, height=600)
screen.tracer(0)

# create paddles
r_paddle = Paddle(350, 0, "#CB1112")
l_paddle = Paddle(-350, 0, "#07F1F7")

# create a ball
ball = Ball()

# create a scoreboard
score_board = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce the ball
        ball.bounce_y()

    # Detect the collision with the paddles
    if ball.distance(r_paddle) < 40 and r_paddle.xcor() > 340 or ball.distance(l_paddle) < 40 and l_paddle.xcor() < -340:
        ball.bounce_x()

    # Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect when the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
