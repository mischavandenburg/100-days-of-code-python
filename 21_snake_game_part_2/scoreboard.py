from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.sety(300)
        self.write_score(self.score)

    def write_score(self, score):
        self.score = score
        self.clear()
        score_to_write = f"Current score: {self.score}"
        self.write(score_to_write, align="center", font=('Courier', 25, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 25, "bold"))
