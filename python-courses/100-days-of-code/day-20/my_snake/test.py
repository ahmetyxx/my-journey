from turtle import Turtle, Screen

jhan=Turtle()
my_screen=Screen()
my_screen.listen()
def aşa():
    jhan.setheading(270)
for _ in range(90):
    jhan.fd(10)
    
    my_screen.onkey(aşa,"w")
    print(jhan.distance(20,20))
    



my_screen.exitonclick()
