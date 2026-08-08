from re import X
from tkinter import Y
from turtle import Turtle


class Snake:
    def __init__(self):
        self.long = 3
        self.snake_dots = []
        self.previous_dot = ""
        self.movement_direction = 0
        self.speed = 20
        self=head_previous_pos=""

    def add_dot(self):
        jhan = Turtle()
        jhan.color("white")
        jhan.shape("square")
        jhan.penup()
        jhan.speed(3)
        if len(self.snake_dots) == 0:
            jhan.setpos(0, 0)  # veya istediğin başlangıç konumu
        else:
            x,y=self.snake_dots[-1].pos()
            jhan.setpos(x-20,y)

        self.snake_dots.append(jhan)
        self.previous_dot = jhan


    
    def align(self):
        previous=self.head_previous_pos
        for dot in self.snake_dots:
            xd, yd = dot.pos()
            xp, yp = previous
            if self.snake_dots.index(dot) != 0:
                previous=dot.pos()
                dot.setpos(xp,yp)
            else:
                self.snake_dots[0].setheading(self.movement_direction)
            
            # if len(self.snake_dots)==self.snake_dots.index(dot)+1:
            #     self.previous_dot=dot

    def move(self):
        self.head_previous_pos=self.snake_dots[0].pos()
        self.snake_dots[0].fd(self.speed)

    def set_direction(self, new_direction: int):
        if abs(self.movement_direction - new_direction) == 180:
            return
        self.movement_direction = new_direction

    def dir_right(self):
        self.set_direction(0)
        
    def dir_up(self):
        self.set_direction(90)
    def dir_left(self):
        self.set_direction(180)
    def dir_down(self):
        self.set_direction(270)
        
    
        