# import Turtle module
import turtle
# import food
import food

class Snake():

    def __init__(self, shape, screen, width, height):
        self.snake = turtle.Turtle()
        self.snake.shape(shape)
        self.snake_pos = [[0, 0], [20, 0], [40, 0], [60,0]]
        self.snake.penup()
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.DELAY = 400
        self.food = food.Food("circle", 10, self.WIDTH, self.HEIGHT)

    def draw_snake(self):
        for sp in self.snake_pos:
            self.snake.goto(sp[0], sp[1])
            self.snake.stamp()

    def move_snake(self):
        self.snake.clearstamps()

        new_head = self.snake_pos[-1].copy()
        new_head[0] += 10

        if new_head in self.snake_pos or new_head[0] < - self.WIDTH / 2 or new_head[0] > self.WIDTH / 2 \
            or new_head[1] < - self.HEIGHT / 2 or new_head[1] > self.HEIGHT / 2:
            turtle.bye()
        else:

            self.snake_pos.append(new_head)

            if not self.food.food_collision(self.snake_pos):
                self.snake_pos.pop(0)

            self.draw_snake()

            self.screen.update()

            turtle.ontimer(self.move_snake, self.DELAY)