from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, LEFT, RIGHT, DOWN = 90, 180, 0, 270


class Snake:
    # each time we initialize a snake object, a 3 segment snake is created
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create a 3 segment snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # get the position and add a new segment at that position of the snake body
    def add_segment(self, position):
        new_segment = Turtle(shape="square")    # turtle shape = "square"
        new_segment.penup()                     # turtle penup = True
        new_segment.goto(position)              # turtle position = (x=0, y += 20)
        new_segment.color("white")              # turtle color = "white"
        self.segments.append(new_segment)       # append every new segment to snake_body

    def reset(self):
        # since every snake on hitting the wall or tail, remains on the screen
        # So we send them off the screen
        for seg in self.segments:
            seg.goto(1000, 1000)
        # we clear the snake segments and create a new 3 segment snake
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # get the position of the last segment and sent it to add_segment function
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # movement of the snake segments. Starts moving from the last segment to the first segment
    def move(self):
        # segments = 3,2,1
        for seg_num in range(len(self.segments) - 1, 0, -1):  # seg_num = 3
            new_x = self.segments[seg_num - 1].xcor()  # x_cor of 2
            new_y = self.segments[seg_num - 1].ycor()  # y_cor of 2
            self.segments[seg_num].goto(new_x, new_y)  # seg 3 goes to the position of seg 2

            # basically, current_segment goes to the position of the segment before it
            # seg 3 goes to seg 2; seg 2 goes to seg 1

        self.head.forward(MOVE_DISTANCE)                   # first segment goes forward

    # when up arrow key is pressed, snake moves up = North
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # self.change_direction += 1

    # when left arrow key is pressed, snake moves left = West
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # when right arrow key is pressed, snake moves right = East
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # when down arrow key is pressed, snake moves down = South
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
