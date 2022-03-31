# import Turtle module
import turtle

class Snake():

    def __init__(self, shape, screen):
        self.snake = turtle.Turtle()
        self.snake.shape(shape)
        self.snake_pos = [[0, 0], [20, 0], [40, 0], [60,0]]
        self.snake.penup()
        self.screen = screen
        self.DELAY = 400

    def draw_snake(self):
        for sp in self.snake_pos:
            self.snake.goto(sp[0], sp[1])
            self.snake.stamp()

    def move_snake(self):
        self.snake.clearstamps()

        new_head = self.snake_pos[-1].copy()
        new_head[0] += 10

        self.snake_pos.append(new_head)

        self.snake_pos.pop(0)

        self.draw_snake()

        self.screen.update()

        turtle.ontimer(self.move_snake, self.DELAY)