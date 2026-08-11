from turtle import Turtle
import random as r
import time

BALL_SPEED=5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5,0.5)
        self.shape("square")
        self.color("white")
        self.target_player= r.randint(-1,1)
        time.sleep(2)
        self.throw_ball()
        
    def throw_ball(self):
        self.seth(r.randint(30,70)*self.target_player)
        
    def move(self):
        self.fd(BALL_SPEED)
        time.sleep(0.01)
        
    def bounce(self):
        self.seth(360-self.heading())
       
    def paddle_collision(self,paddle):
        for seg in paddle.paddle_segments:
            if  self.distance(seg)<20:
                self.seth(180-self.heading()+r.randint(5,20))
                break
            
        
        
        