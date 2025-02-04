from turtle import Turtle

STARTING_WIDTH = 1
STARTING_LEN = 1
STARTING_DIRECTION = "Up"

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(STARTING_WIDTH, STARTING_LEN)
        self.color("white")
        self.speed("slowest")
        self.goto(0, 0)
        self.y_direction = "Up"
        self.x_direction = "Right"

    def reverse_x(self, direction):
        self.x_direction = direction


    def move(self):
        x_cord = self.xcor()
        y_cord = self.ycor()

        if y_cord > 280 and self.y_direction == "Up":
            self.y_direction = "Down"
        elif y_cord < -280 and self.y_direction == "Down":
            self.y_direction = "Up"
        
        if self.x_direction == "Right":
            x_cord += 10
        elif self.x_direction == "Left":
            x_cord -= 10

        if self.y_direction == "Up":
            y_cord += 10
        elif self.y_direction == "Down":
            y_cord -= 10
        
        self.goto(x_cord, y_cord)