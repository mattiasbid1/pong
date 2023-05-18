from turtle import Turtle
import random
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(random.randint(0, 360))
        self.ball_speed = 0.001

    def move(self):
        if self.ycor() > 380 or self.ycor() < -380:
            self.bounce()
        self.forward(10)
        time.sleep(self.ball_speed)

    def bounce(self, paddle_mod=False):
        if paddle_mod:
            ball_heading = (180 - self.heading()) % 360
        else:
            ball_heading = 360 - self.heading()
        self.ball_speed *= 0.95
        self.setheading(ball_heading)

    def respawn(self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 360))
        self.ball_speed = 0.001
