from turtle import Turtle
FONT = ("Courier", 18, "normal")
GAME_OVER_FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

    def increase_level(self):
        self.level += 1

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)

