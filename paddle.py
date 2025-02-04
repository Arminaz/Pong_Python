from turtle import Turtle

STARTING_WIDTH = 5
STARTING_LEN = 1


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(STARTING_WIDTH, STARTING_LEN)
        self.color("white")
        self.speed("fastest")
        self.goto(xpos, ypos)


    def go_up(self):
        if self.ycor() < 180:
            self.sety(self.ycor()+20)


    def go_down(self):
        if self.ycor() > -180:
            self.sety(self.ycor()-20)