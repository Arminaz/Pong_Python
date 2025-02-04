from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600, startx=-600, starty=50)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

l_paddle = Paddle(-380, 0)
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

r_paddle = Paddle(380, 0)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True

ball = Ball()
scoreboard = Scoreboard()

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check if Ball hits the wall on left or right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
    # Check if ball hit the paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 340:
        ball.reverse_x("Left")
    elif ball.distance(l_paddle) <= 50 and ball.xcor() < -340:
        ball.reverse_x("Right")


screen.exitonclick()