from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()

my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("snake game v2")
my_screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")

is_game_on = True

while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food)<15:
        food.refresh()
        scoreboard.change_score(1)
        snake.add_segment()
    if snake.snake_head.xcor()>280 or snake.snake_head.xcor()<-280 or snake.snake_head.ycor()>280 or snake.snake_head.ycor()<-280:
        is_game_on=False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment==snake.snake_head:
            pass
        elif snake.snake_head.distance(segment)<10:
            is_game_on=False
            scoreboard.game_over()

my_screen.exitonclick()
