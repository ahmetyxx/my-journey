from turtle import Screen
import turtle
from player import Player
from trafic_manager import Manager
import time

screen=Screen()
screen.setup(600,600)
screen.title("turtle crossing")
screen.colormode(255)
screen.colormode(255)
screen.tracer(0)
screen.listen()


player= Player(0,-258)
manager=Manager(600,600)

screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")


is_game_on=True
setup=False

for _ in range(100):
    manager.open_strips()
    manager.draw_cars()
    manager.move_cars()
    

while is_game_on:

    manager.open_strips()
    screen.update()
    time.sleep(0.1)
    manager.draw_cars()
    manager.move_cars()
    manager.garbage_killer()
    print(len(turtle.turtles()))


screen.exitonclick()

