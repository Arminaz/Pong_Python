from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

paddles = {
    "paddle_1": {"position": (350, 0), "up_key": "Up", "down_key": "Down"},
    "paddle_2": {"position": (-350, 0), "up_key": "w", "down_key": "s"},
}

for paddle_name, paddle_info in paddles.items():
    paddle = Paddle(*paddle_info["position"])
    paddle.up_key = paddle_info["up_key"]
    paddle.down_key = paddle_info["down_key"]
    screen.onkey(paddle.go_up, paddle.up_key)
    screen.onkey(paddle.go_down, paddle.down_key)
    locals()[paddle_name] = paddle

game_on = True

while game_on:
    screen.update()


screen.exitonclick()