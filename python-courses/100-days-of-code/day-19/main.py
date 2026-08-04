from turtle import Turtle, Screen
import random as r



my_screen = Screen()

my_screen.setup(500,400)
user_bet=my_screen.textinput("make your bet","which turtle will won?")
colors=["red","orange","black","purple","pink","yellow","green","blue"]

for i in range(6):
    jhan=Turtle()
    jhan.shape("turtle")
    color=r.choice(colors)
    jhan.color(color)
    jhan.penup()
    jhan.goto(-230,-70+30*i)
    colors.remove(color)














def move_forward():
    jhan.forward(10)


def move_backward():
    jhan.back(10)


def turn_counter_clockwise():
    jhan.left(10)


def turn_clockwise():
    jhan.right(10)
    
# my_screen.onkey(move_forward,"w")
# my_screen.onkey(move_backward,"s")
# my_screen.onkey(turn_clockwise,"d")
# my_screen.onkey(turn_counter_clockwise,"a")
# my_screen.listen()


my_screen.exitonclick()
