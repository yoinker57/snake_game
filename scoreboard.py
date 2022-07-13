from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")


class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = ALIGMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()