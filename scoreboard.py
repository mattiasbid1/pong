from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, location="left"):
        super().__init__()
        self.location = location
        self.hideturtle()
        self.penup()
        self.color("White")
        self.set_location()
        self.score = 0
        self.set_score()

    def set_location(self):
        if self.location == "left":
            self.goto(-100, 300)
        else:
            self.goto(100, 300)

    def set_score(self):
        self.clear()
        self.write(self.score, align="center", font=("Helvetica Neue", 52, "bold"))


    def goal(self):
        self.score += 1
        self.set_score()