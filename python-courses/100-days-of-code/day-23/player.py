from turtle import Turtle
from typing import Self

PLAYER_SPEED=10

class Player(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.color("black")
        self.setpos(x_cor,y_cor)
        
        
    def up(self):
        self.fd(PLAYER_SPEED)
    def down(self):
        self.bk(PLAYER_SPEED)
