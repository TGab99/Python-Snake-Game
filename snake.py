# import Turtle module
import turtle
# import food
import food

class Snake():

    directions = {
        "up": (0, 20),
        "down": (0, -20),
        "right": (20, 0),
        "left": (-20, 0)
    }

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
        self.direction = "up"

    def draw_snake(self):
        for sp in self.snake_pos:
            self.snake.goto(sp[0], sp[1])
            self.snake.stamp()

    def move_snake(self):
        self.snake.clearstamps()

        new_head = self.snake_pos[-1].copy()
        new_head[0] += self.directions[self.direction][0]
        new_head[1] += self.directions[self.direction][1]

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

    def set_direction(self, dir):
        if(dir == "up"):
            if(self.direction != "down"):
                self.direction = "up"

        if(dir == "down"):
            if(self.direction != "up"):
                self.direction = "down"

        if(dir == "right"):
            if(self.direction != "left"):
                self.direction = "right"

        if(dir == "left"):
            if(self.direction != "right"):
                self.direction = "left"

    def bind_direction_keys(self):
        self.screen.onkey(lambda: self.set_direction("up"), "Up")
        self.screen.onkey(lambda: self.set_direction("down"), "Down")
        self.screen.onkey(lambda: self.set_direction("right"), "Right")
        self.screen.onkey(lambda: self.set_direction("left"), "Left")
        