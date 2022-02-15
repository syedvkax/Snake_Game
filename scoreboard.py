from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align=ALIGN, font=FONT)
