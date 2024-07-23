from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s=Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.tracer(0)


paddle_r= Paddle((380,0))
paddle_l= Paddle((-380,0))
ball= Ball()


scoreboard=Scoreboard()

scoreboard.center_line()
scoreboard.show_score()


s.listen()
s.onkey(paddle_r.up, "Up")
s.onkey(paddle_r.down, "Down")

s.onkey(paddle_l.up, "w")
s.onkey(paddle_l.down, "s")

is_on=True

game_is_on=True
while game_is_on:
        
    time.sleep(0.04)
    s.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.reflect_wall()
        
    if ball.distance(paddle_l)<50 and ball.xcor()<-370 or ball.distance(paddle_r)<50 and ball.xcor()>370:
        ball.reflect_paddle()

    if ball.xcor()>380 or ball.xcor()<-380:
        ball.fd(20)

        if ball.xcor() > 370:
            scoreboard.update_score("L")
        else:
            scoreboard.update_score("R")

        scoreboard.show_score()

        time.sleep(0.9)   
        ball.home()
        ball.change_direction()
            



s.exitonclick()
