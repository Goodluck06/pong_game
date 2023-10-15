from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def bounce_y(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
    def bounce_x(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())