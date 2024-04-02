from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open("data.txt", "r") as f:
            self.highscore = int(f.read())

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    # updates the scoreboard on the screen
    def update_score(self):
        # clear the score screen, so they don't overlap
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # Update the high score and reset the score
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", "w") as f:
            f.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # increases the score whenever the snake collides with food
    def increase_score(self):
        self.score += 1                 # first increase the score by 1
        self.update_score()             # now update the score screen
