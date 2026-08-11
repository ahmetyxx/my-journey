from turtle import Screen
from paddle import Paddle
from ball import Ball
import random

import paddle


screen=Screen()
screen.setup(1000 ,500)
screen.bgcolor("black")
screen.title("pong game")
screen.listen()
screen.tracer(0)

paddle1=Paddle(x_cor=-450,y_cor=0,paddle_long=5)
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")

paddle2=Paddle(x_cor=450,y_cor=0,paddle_long=5)
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

ball=Ball()




is_game_on=True
paddle1.paddle_segments

while is_game_on:
    
    ball.move()
    print(ball.xcor())
    if ball.ycor()>230 or ball.ycor()<-230:
        screen.tracer(0)
        ball.bounce()
        
    if ball.xcor()>420:
        ball.paddle_collision(paddle2)
    
    if ball.xcor()<-420:
        ball.paddle_collision(paddle1)
    screen.update()
 
    
    






screen.exitonclick()
