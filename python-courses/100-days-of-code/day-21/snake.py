from turtle import Turtle

MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def create_snake(self):

        for i in range(3):
            jhan = Turtle(shape="square")
            jhan.penup()
            jhan.color("white")
            self.segments.append(jhan)
            jhan.setx(-(self.segments.index(jhan) * 20))

    def add_segment(self):
        jhan = Turtle(shape="square")
        jhan.penup()
        jhan.color("white")
        jhan.goto(self.segments[-1].position())
        self.segments.append(jhan)
        

    def up(self):
        if self.snake_head.heading()!=DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading()!=UP:
            self.snake_head.seth(DOWN)

    def right(self):
        if self.snake_head.heading()!=LEFT:
            self.snake_head.seth(RIGHT)

    def left(self):
        if self.snake_head.heading()!=RIGHT:   
            self.snake_head.seth(LEFT)
