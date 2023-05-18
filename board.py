from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.goto(0, -380)
        self.board_paint()

    def board_paint(self):
        self.setheading(90)
        while self.ycor() < 380:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
