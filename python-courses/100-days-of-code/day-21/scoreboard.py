from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.pencolor("white")
        self.display_score()

    def change_score(self, amount):
        self.score += amount
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align="center",
            font=("Arial", 12, "normal"),
        )
        
    def game_over(self):
        self.goto(0,0)
        self.write(
            arg=f"GAME OVER",
            move=False,
            align="center",
            font=("Arial", 24, "normal"),
        )
