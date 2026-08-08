import time
from turtle import Turtle, Screen
from my_snake.snake import Snake

my_screen = Screen()
snake = Snake()

my_screen.screensize(canvwidth=600, canvheight=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()




def input_handler():
    my_screen.onkey(snake.dir_right, "d")
    my_screen.onkey(snake.dir_up, "w")
    my_screen.onkey(snake.dir_left, "a")
    my_screen.onkey(snake.dir_down, "s")



is_game_running = True

while is_game_running:

    while snake.long > len(snake.snake_dots):
        snake.add_dot()

    snake.move()
    snake.align()
    my_screen.update()
    time.sleep(0.1)
    input_handler()
    


my_screen.exitonclick()
