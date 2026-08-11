from turtle import Turtle

PADDLE_SPEED=40

class Paddle:
    def __init__(self,x_cor,y_cor,paddle_long:int):
        self.paddle_segments=[]
        self.create_paddle(x_cor,y_cor,paddle_long)
    
    
    def create_paddle(self, x_cor,y_cor,paddle_long:int):
        
        up=True
        for i in range(paddle_long):
            jhan=Turtle()
            jhan.penup()
            jhan.color("white")
            jhan.shape("square")
            jhan.setx(x_cor)
            if up: 
                jhan.sety(y_cor+10*i)
            else:
                jhan.sety(y_cor-10*i)
            up= not up
            self.paddle_segments.append(jhan)
            
    def up(self):
        for seg in self.paddle_segments:
            seg.seth(90)
            seg.fd(PADDLE_SPEED)
            
    def down(self):
        for seg in self.paddle_segments:
            seg.seth(270)
            seg.fd(PADDLE_SPEED)
            
   