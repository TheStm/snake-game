from turtle import Turtle, Screen
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(0 - i * 20)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            xpos = self.segments[seg - 1].xcor()
            ypos = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=xpos, y=ypos)
        self.head.fd(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def is_wall_hit(self):
        if self.segments[0].xcor() >= 280 or self.segments[0].xcor() <= -281 or self.segments[0].ycor() >= 281 or\
                self.segments[0].ycor() <= -280:
            return True

    def grow(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setposition(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())
        self.segments.append(new_segment)

    def is_tail_hit(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True

