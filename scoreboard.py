from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scr = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.increase_score()

    def increase_score(self):
        self.scr += 1
        self.clear()
        self.write(f"Score: {self.scr} ", False, align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. ", False, align="center", font=("Arial", 25, "normal"))