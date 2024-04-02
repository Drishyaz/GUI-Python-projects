from turtle import Turtle
import random


class Food(Turtle):
    # once we inherit the Turtle class, we can use its attributes and methods as its own
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)          # we halved the len and width
        self.speed("fastest")
        self.refresh()

    # if snake collides with food, the food teleports to another random location
    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(x=random_x, y=random_y)
