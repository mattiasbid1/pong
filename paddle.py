from turtle import Turtle
import time

UP = 90
DOWN = 270


class Paddle:

    def __init__(self, size=3, location="left"):
        self.size = size
        self.location = location
        self.paddle_body = []
        self.speed = 0.002
        self.heading = UP
        self.make_paddle()

    def make_paddle(self):
        if self.location == "left":
            x_cor = -580
        else:
            x_cor = 580

        y_cor = int(round((self.size / 2)) * -20)

        for part in range(self.size):
            part = Turtle()
            part.shape("square")
            part.color("white")
            part.penup()
            part.goto(x_cor, y_cor)
            y_cor += 20
            part.setheading(self.heading)
            self.paddle_body.append(part)

    def move_paddle(self):
        if self.paddle_body[-1].ycor() > 380 or self.paddle_body[0].ycor() < -380:
            self.reverse()

        for part in self.paddle_body:
            part.setheading(self.heading)
            part.forward(10)
        time.sleep(self.speed)

    def reverse(self):
        if self.heading == UP:
            self.heading = DOWN
        else:
            self.heading = UP

    def up(self):
        self.heading = UP

    def down(self):
        self.heading = DOWN
