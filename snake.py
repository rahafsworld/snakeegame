from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Direction constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(20000, 20000)  # Move segments far off screen
            seg.hideturtle()  # Make them invisible
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake forward by moving the last segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # Prevent moving directly backwards
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # Prevent moving directly backwards
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # Prevent moving directly backwards
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # Prevent moving directly backwards
            self.head.setheading(RIGHT)
