from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pensize(20)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.center_line()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1           # reverses the direction

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9      # everytime the ball hits the paddle, its speed increases

    def to_center(self):
        self.goto(0, 0)
        self.move_speed = 0.1       # when the paddle missed, the move_speed is reset
        self.bounce_x()

    def center_line(self):
        self.shape("square")
        self.shapesize(stretch_wid=50, stretch_len=0.3)
