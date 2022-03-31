# import Turtle module
import turtle

class Snake:

    def __init__(self, shape):
        self.snake = turtle.Turtle()
        self.snake.shape(shape)
        self.snake_pos = [[0, 0], [20, 0], [40, 0], [60,0]]
        self.snake.penup()

    def draw_snake(self):
        for sp in self.snake_pos:
            self.snake.goto(sp[0], sp[1])
            self.snake.stamp()

    def move_snake(self):
        pass