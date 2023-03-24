from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score import Score

s = Screen()
s.setup(800, 600)
s.bgcolor('black')
s.title('The pong game!')
s.listen()
s.tracer(0)
score = Score()


paddle1 = Paddle(-900, 0)
s.onkeypress(fun=paddle1.move_up, key='w')
s.onkeypress(fun=paddle1.move_down, key='s')

paddle2 = Paddle(900, 0)
s.onkeypress(fun=paddle2.move_up, key='Up')
s.onkeypress(fun=paddle2.move_down, key='Down')

ball = Ball()

on = True


while on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce()
    elif ball.distance(paddle1) < 50 and ball.xcor() < -880 or ball.distance(paddle2) < 50 and ball.xcor() > 880:
        ball.v_bounce()
    if ball.xcor() < -900:
        ball.reset_pos()
        ball.v_bounce()
        score.p2_score += 1
        score.new_point()

    elif ball.xcor() > 900:
        ball.reset_pos()
        ball.v_bounce()
        score.p1_score += 1
        score.new_point()
    if score.p1_score == 5 or score.p2_score == 5:
        break


score.gameover()













s.exitonclick()
