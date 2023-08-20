from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        self.turn = 0
        for _ in range(3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            xcor = -20*self.turn
            new_turtle.goto(xcor, 0)
            self.turn += 1
            self.snake.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            previous_seg = self.snake[seg_num-1]
            new_x = previous_seg.xcor()
            new_y = previous_seg.ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
