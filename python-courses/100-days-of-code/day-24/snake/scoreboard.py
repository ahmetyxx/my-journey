from ast import With
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score= self.get_highscore()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def get_highscore(self):
        with open("data.txt") as data:
            return int(data.read())
        
    def set_highscore(self,new_score):
        with open("data.txt", mode="w") as data:
            data.write(str(new_score))
            self.high_score=new_score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score>self.high_score:
            self.set_highscore(self.score)
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
