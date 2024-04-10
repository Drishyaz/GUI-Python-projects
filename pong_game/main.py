from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.tracer(0)                            # turns off the animation
screen.listen()
screen.title("My Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

ball = Ball()
line = Ball().center_line()                 # draws a center line in the game board
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    ball.move()
    # after turning off, you have to manually update the screen
    screen.update()
    # the animation delay changes according to the ball's moving speed
    time.sleep(ball.move_speed)
    # paddle movements
    screen.onkey(key="Up", fun=r_paddle.move_up)
    screen.onkeypress(key="w", fun=l_paddle.move_up)
    screen.onkey(key="Down", fun=r_paddle.move_down)
    screen.onkeypress(key="s", fun=l_paddle.move_down)
    # Detect ball's collision with top and bottom edge
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect ball's collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        # # Speed up the ball everytime it hits a paddle
        # ball.x_move += 5
        # ball.y_move += 5

    # Detect when paddle misses: ball spawns at center and moves in opposite direction
    if ball.xcor() > 380:           # when left paddle misses
        ball.to_center()
        scoreboard.r_point()

    elif ball.xcor() < -380:        # when right paddle misses
        ball.to_center()
        scoreboard.l_point()

screen.exitonclick()
