from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.penup()
        self.color(self.create_color())
        self.shape("square")
        self.seth(180)
        self.shapesize(stretch_len=2,stretch_wid=0.5)
        self.setpos(x_cor,y_cor)
        
        
    def create_color(self):
        return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )