# import the Turtle module
import turtle
# import Random module
import random

class Food:

    def __init__(self, shape, size, width, height):
        self.food = turtle.Turtle()
        self.food.shape(shape)
        self.FOOD_SIZE = size
        self.food.shapesize(self.FOOD_SIZE / 20) 
        self.width = width
        self.height = height
        self.food_pos = self.get_random_food_pos()
        self.food.penup()

    def food_collision(self, snake_pos):
        if self.get_distance(snake_pos[-1], self.food_pos) < 20:
            self.food_pos = self.get_random_food_pos()
            self.food.goto(self.food_pos)
            return True

        return False

    def get_random_food_pos(self):
        x = random.randint( - self.width / 2 + self.FOOD_SIZE, self.width / 2 - self.FOOD_SIZE)
        y = random.randint( - self.height / 2 + self.FOOD_SIZE, self.height / 2 - self.FOOD_SIZE)

        return (x,y)

    def get_distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5