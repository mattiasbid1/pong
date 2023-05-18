from turtle import Screen
from board import Board
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball


def is_paddle_bounce(selected_paddle):
    for body in selected_paddle.paddle_body:
        if body.distance(ball) < 30:
            ball.bounce(paddle_mod=360)


def score_check():
    if ball.xcor() > 600:
        player_score.goal()
        ball.respawn()
    elif ball.xcor() < -600:
        ai_score.goal()
        ball.respawn()
    else:
        pass


is_active = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Pong")
screen.tracer(0)

board = Board()
player_paddle = Paddle()
ai_paddle = Paddle(location="right", size=12)
player_score = Scoreboard()
ai_score = Scoreboard(location="right")
ball = Ball()

screen.listen()
screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")

screen.update()

while is_active:
    player_paddle.move_paddle()
    ai_paddle.move_paddle()
    is_paddle_bounce(player_paddle)
    is_paddle_bounce(ai_paddle)
    ball.move()
    score_check()
    screen.update()

screen.exitonclick()
