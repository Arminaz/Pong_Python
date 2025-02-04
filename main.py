from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600, startx=-600, starty=50)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()

l_paddle = Paddle(-380, 0)
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

r_paddle = Paddle(380, 0)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True

ball = Ball()

while game_on:
    if ball.xcor() > 380 or ball.xcor() < -380:
        game_on = False
    ball.move()
    
    # Check if ball hit the paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 340:
        ball.reverse_x("Left")
    elif ball.distance(l_paddle) <= 50 and ball.xcor() < -340:
        ball.reverse_x("Right")


screen.exitonclick()